# coding=utf-8

'''
Device out of market


from wikilife_crawler.twitter.device_tweets_crawler.device_reader import DeviceReader
from wikilife_crawler.twitter.delegates.twitter_search_delegate import TwitterSearchFilter
from wikilife_crawler.twitter.device_tweets_crawler.node_parse_info import NodeParseInfo
from wikilife_crawler.twitter.device_tweets_crawler.tweet_text_parser import TweetTextParser
from wikilife_crawler.utils.numbers import Numbers
from wikilife_crawler.utils import patterns
from wikilife_crawler.utils.times import Times
from wikilife_crawler.twitter.device_tweets_crawler.tweet_date_parser import TweetDateParser
from wikilife_utils.date_utils import DateUtils

class Zeo(DeviceReader):
    """
    The Zeo device track sleep, slept hours and hours in REM status
    """

    def get_filter(self, since_id):
        q = "#Zeo #sleepdata"
        filter = TwitterSearchFilter(q)
        filter.show_user = TwitterSearchFilter.SHOW_USER_TRUE
        filter.rpp = 100 #TODO tune
        filter.since_id = since_id

        return filter

    def get_category(self):
        return "physiological"

    def get_start_end(self, item):
        #TODO reuse
        def custom_parser(raw_value):
            #TODO TweetTextParser.TIME_IN_MINUTES_DESCRIPTIVE_LEFT >> Times.parse_descriptive()

            h = 0
            m = 0

            if "h" in raw_value:
                tmp = raw_value.split("h")
                h = Numbers.parse_int(tmp[0])
                if "m" in raw_value:
                    tmp = tmp[1].split("m")
                    m = Numbers.parse_int(tmp[0].strip())
            else:
                tmp = raw_value.split("m")
                m = Numbers.parse_int(tmp[0])

            value = Times.to_minutes(h, m, 0)
            return value
        
        duration = NodeParseInfo()
        duration.node_namespace = "wikilife.physiological.sleep.duration.value-node"
        duration.pattern = "(I slept) " + patterns.TIME_PATTERN_DESCRIPTIVE
        duration.pattern_value_index = 1
        duration.value_parser_type = TweetTextParser.CUSTOM
        duration.custom_parser_closure = custom_parser

        duration_minutes = TweetTextParser.parse(item["text"], duration)
        start = TweetDateParser.from_datetime(item["created_at"])
        end = DateUtils.add_seconds(start, duration_minutes*60)

        return start, end

    def get_nodes_parse_info(self):

        def custom_parser(raw_value):
            #TODO TweetTextParser.TIME_IN_MINUTES_DESCRIPTIVE_LEFT >> Times.parse_descriptive()

            h = 0
            m = 0

            if "h" in raw_value:
                tmp = raw_value.split("h")
                h = Numbers.parse_int(tmp[0])
                if "m" in raw_value:
                    tmp = tmp[1].split("m")
                    m = Numbers.parse_int(tmp[0].strip())
            else:
                tmp = raw_value.split("m")
                m = Numbers.parse_int(tmp[0])

            value = Times.to_minutes(h, m, 0)
            return value

        """
        duration = NodeParseInfo()
        duration.node_namespace = "wikilife.physiological.sleep.duration.value-node"
        duration.pattern = "(I slept) " + patterns.TIME_PATTERN_DESCRIPTIVE
        duration.pattern_value_index = 1
        duration.value_parser_type = TweetTextParser.CUSTOM
        duration.custom_parser_closure = custom_parser
        """
        
        deep = NodeParseInfo()
        deep.node_id = 241563
        deep.pattern = "(Deep:) " + patterns.TIME_PATTERN_DESCRIPTIVE
        deep.pattern_value_index = 1
        deep.value_parser_type = TweetTextParser.CUSTOM
        deep.custom_parser_closure = custom_parser

        rem = NodeParseInfo()
        rem.node_id = 241565
        rem.pattern = "(REM:) " + patterns.TIME_PATTERN_DESCRIPTIVE
        rem.pattern_value_index = 1
        rem.value_parser_type = TweetTextParser.CUSTOM
        rem.custom_parser_closure = custom_parser

        awake = NodeParseInfo()
        awake.node_id = 241567
        awake.pattern = "(Awake:) " + patterns.TIME_PATTERN_DESCRIPTIVE
        awake.pattern_value_index = 1
        awake.value_parser_type = TweetTextParser.CUSTOM
        awake.custom_parser_closure = custom_parser

        return [deep, rem, awake]
'''