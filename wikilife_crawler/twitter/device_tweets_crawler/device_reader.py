# coding=utf-8

from abc import abstractmethod
from wikilife_crawler.twitter.device_tweets_crawler.tweet_date_parser import \
    TweetDateParser
from wikilife_crawler.twitter.device_tweets_crawler.tweet_text_parser import \
    TweetTextParser, TweetTextParserException
from wikilife_utils.formatters.date_formatter import DateFormatter
from wikilife_utils.logs.log_creator import LogCreator


class DeviceReaderException(Exception):
    pass


class DeviceReader(object):
    """
    Abstract class
    """

    _logger = None
    _meta_ids = None
    _meta_map = None
    _twitter_search_dlgt = None
    _twitter_reader_dao = None
    _meta_dao = None
    _twitter_user_srv = None
    _log_srv = None

    def __init__(self, logger, meta_ids, twitter_search_delegate, twitter_reader_dao, meta_dao, twitter_user_service, log_service):
        self._logger = logger
        self._meta_ids = meta_ids
        self._twitter_search_dlgt = twitter_search_delegate
        self._twitter_reader_dao = twitter_reader_dao
        self._meta_dao = meta_dao
        self._twitter_user_srv = twitter_user_service
        self._log_srv = log_service
        self._meta_map = self._get_meta_map(meta_ids)

    def _get_meta_map(self, meta_ids):
        meta_map = {}
        nodes = self._meta_ids["nodes"]
        metrics = self._meta_ids["metrics"]

        for node in nodes:
            node_id = nodes[node] 
            meta_map[node_id] = self._meta_dao.get_node_by_id(node_id)

        for metric in metrics:
            metric_id = metrics[metric] 
            meta_map[metric_id] = self._meta_dao.get_node_by_id(metric_id)

        return meta_map

    def _obtain_since_id(self):
        reader_name = self.get_name()

        if self._twitter_reader_dao.find_reader(reader_name)==None:
            self._twitter_reader_dao.create_reader(reader_name, 0)

        since_id = self._twitter_reader_dao.get_reader_since_id(reader_name)

        return since_id

    def _create_log(self, internal_user_id, text, nodes, start, end):
        """
        Create and save user log
        """
        source = "crawler.twitter.%s" %self.get_name()
        start_str = DateFormatter.to_datetime(start)
        end_str = DateFormatter.to_datetime(end)
        log = LogCreator.create_log(internal_user_id, start_str, end_str, text, source, nodes)
        self._log_srv.add_logs([log])

        return log

    def get_name(self):
        return self.__class__.__name__.lower()

    def read(self):
        #TODO handle multiple pages
        reader_name = self.get_name()
        self._logger.info("## Reading %s ----------------------------------------" %reader_name)
        filter = self.get_filter(self._obtain_since_id())
        result = self._twitter_search_dlgt.search(filter)
        result_items = result["statuses"]
        success_count = 0 
        warning_count = 0 
        error_count = 0 
        total_count = len(result_items)
        self._logger.info("%s tweets found" %total_count)

        for item in result_items:
            try:
                self._logger.info("processing tweet id: %s, text: %s" %(item["id_str"], item["text"]))
                twitter_user = self._twitter_user_srv.obtain_twitter_user(item["user"]["id_str"])
                nodes = self.parse_nodes(item["text"])
                text = self.parse_text(nodes)
                start, end = self.get_start_end(item)
                self._create_log(twitter_user["internal_id"], text, nodes, start, end)
                success_count += 1 

            except DeviceReaderException, e:
                warning_count += 1
                self._logger.warning(e)

            except Exception, e:
                error_count += 1
                #exc_type, exc_value, exc_traceback = sys.exc_info()
                #traceback.print_tb(exc_traceback)
                self._logger.exception("")

        if len(result_items)>0:
            #TODO es necesario incrementar en uno el since_id o el servicio de twitter toma desde el proximo ??? 
            self._twitter_reader_dao.set_reader_since_id(reader_name, result_items[0]["id"])

        self._logger.info("## End %s --- Total: %s, Success: %s, Warning: %s, Error: %s \n" %(reader_name, total_count, success_count, warning_count, error_count))

    def parse_text(self, log_nodes):
        """
        Original V3/tree:
        Having nodes: "wikilife.exercise.exercise.running.duration.value-node" and "wikilife.exercise.exercise.running.distance.value-node"
        with values 45 and 5, should return: "Running Duration 45 min Distance 5 km"
        Note: Nodes must have the same meta root. If not, must be two separate logs.
        """
        text = ""

        for log_node in log_nodes:
            node = self._meta_map[log_node["nodeId"]]
            metric = self._meta_map[log_node["metricId"]]
            node_name = node.name
            metric_name = metric.name
            metric_unit = metric.unit
            log_value = str(log_node["value"])
            text += "%s: %s %s %s, " %(node_name, metric_name, log_value, metric_unit)

        return text

    def parse_nodes(self, text):
        """
        Returns node(id,value) list

        Sample text value:
        FitInMyHeart: RT @wildfirefitness: Go Mo! RT @FitInMyHeart My fitbit #fitstats for 9/08/2011: 10,015 steps and 4.2 miles traveled. http://t.co/kaxvzju

        Sample return:
        [{'nodeId': 397, 'value': 10015}, {'nodeId': 399, 'value': 6.7592448000000012}]
        """

        nodes = []

        for info in self.get_nodes_parse_info():
            try:
                value = TweetTextParser.parse(text, info)
                #node = {"nodeId": info.node_id, "metricId": info.metric_id, "value": value}
                node = LogCreator.create_log_node(info.node_id, info.metric_id, value)
                nodes.append(node)

            except TweetTextParserException, e:
                self._logger.warning(e)

        if len(nodes)==0:
            raise DeviceReaderException("None %s nodes extracted from text: %s" %(self.get_name(), text))

        return nodes

    def get_start_end(self, item):
        """
        By default is an atomic time
        """
        start = TweetDateParser.from_datetime(item["created_at"])
        end = start
        return start, end

    @abstractmethod
    def get_filter(self, since_id):
        """
        Returns TwitterSearchFilter
        since_id is calculated by this class, but can be overrided in the concrete reader
        """
        raise NotImplementedError()

    @abstractmethod
    def get_nodes_info(self):
        """
        Returns parsing info for each node to be extracted from tweet 
    
        Sample impl:
        ===========
        
        steps = {}
        steps["node_namespace"] = "wikilife.exercise.exercise.walking.step"
        steps["pattern"] = r'(\d+,\d+) (steps)'
        steps["pattern_value_index"] = 0
        steps["pattern_unit_index"] = 1
        steps["value_parser_type"] = NodesParser.AMOUNT
        
        distance = {}
        distance["node_namespace"] = "wikilife.exercise.exercise.walking.step"
        distance["pattern"] = r'(\d+,\d+) (steps)'
        distance["value_group_index"] = 0
        distance["value_parser"] = NodesParser.DISTANCE
        
        return [steps, distance]
        """
        raise NotImplementedError()
