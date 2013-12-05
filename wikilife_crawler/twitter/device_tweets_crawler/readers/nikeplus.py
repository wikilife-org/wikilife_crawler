# coding=utf-8

from wikilife_crawler.twitter.delegates.twitter_search_delegate import \
    TwitterSearchFilter
from wikilife_crawler.twitter.device_tweets_crawler.device_reader import \
    DeviceReader
from wikilife_crawler.twitter.device_tweets_crawler.node_parse_info import \
    NodeParseInfo
from wikilife_crawler.twitter.device_tweets_crawler.tweet_date_parser import \
    TweetDateParser
from wikilife_crawler.twitter.device_tweets_crawler.tweet_text_parser import \
    TweetTextParser
from wikilife_crawler.utils import patterns
from wikilife_utils.date_utils import DateUtils


class Nikeplus(DeviceReader):
    """
    The Nikeplus device track distance and elapsed time
    """

    def get_filter(self, since_id):
        q = "#nikeplus"
        filter = TwitterSearchFilter(q)
        filter.show_user = TwitterSearchFilter.SHOW_USER_TRUE
        filter.rpp = 100 #TODO tune
        filter.since_id = since_id
        
        return filter

    def get_start_end(self, item):
        duration = NodeParseInfo()
        duration.pattern = "(time of) " + patterns.TIME_PATTERN
        duration.pattern_value_index = 1
        duration.value_parser_type = TweetTextParser.TIME_IN_MINUTES_RIGHT
        duration_minutes = TweetTextParser.parse(item["text"], duration)
        start = TweetDateParser.from_datetime(item["created_at"])
        end = DateUtils.add_seconds(start, duration_minutes*60)

        return start, end

    def get_nodes_parse_info(self):
        """
        duration = NodeParseInfo()
        duration.node_namespace = "wikilife.exercise.exercise.exercise.running.duration.value-node"
        duration.pattern = "(time of) " + patterns.TIME_PATTERN
        duration.pattern_value_index = 1
        duration.value_parser_type = TweetTextParser.TIME_IN_MINUTES_RIGHT
        """

        distance = NodeParseInfo()
        distance.node_id = self._meta_ids["nodes"]["running"]
        distance.metric_id = self._meta_ids["metrics"]["distance"]
        distance.pattern =  patterns.REAL_PATTERN + " " + patterns.DISTANCE_UNITS_PATTERN
        distance.pattern_value_index = 0
        distance.pattern_unit_index = 1
        distance.value_parser_type = TweetTextParser.DISTANCE

        return [distance]
    