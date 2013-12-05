# coding=utf-8

import time

REQUEST_INTERVAL = 3.0

class DeviceTweetsCrawler(object):
    """
    class DeviceTweetsCrawler pyDocs
    """

    _logger = None
    _meta_dao = None
    _readers = None

    def __init__(self, logger, meta_dao, readers):
        self._logger = logger
        self._meta_dao = meta_dao
        self._readers = readers

    def crawl(self):
        self._logger.info("#### Crawling start ====================")
        success_count = 0

        for reader in self._readers:
            start_time = time.time()

            try:
                reader.read()
                success_count += 1
            except Exception, e:
                self._logger.error(e)

            delta_time = time.time()-start_time
            if delta_time < REQUEST_INTERVAL:
                time.sleep(REQUEST_INTERVAL-delta_time)

        self._logger.info("#### Crawling end ==================== \n")
        return success_count==len(self._readers)

    def check_readers_meta_dependencies(self):
        print "Readers meta dependencies:"
        print "=========================="

        node_missing_count = 0
        metric_missing_count = 0

        for reader in self._readers:
            print "\n%s" %reader.get_name()
            print "-----------------------"

            for item in reader.get_nodes_parse_info():
                node = self._meta_dao.get_node_by_id(item.node_id)
                metric = self._meta_dao.get_node_by_id(item.metric_id)

                if node == None:
                    node_missing_count += 1
                    node_status = "missing"
                else:
                    node_status = "ok"

                if metric == None:
                    metric_missing_count += 1
                    metric_status = "missing"
                else:
                    metric_status = "ok"

                print "node(%s) : %s" %(item.node_id, node_status)
                print "metric(%s) : %s" %(item.metric_id, metric_status)

        print "\nMissing dependencies: Nodes: %s, Metrics: %s" %(node_missing_count, metric_missing_count)
