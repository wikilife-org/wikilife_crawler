# coding=utf-8
from wikilife_crawler.twitter.delegates.twitter_search_delegate import \
    TwitterSearchFilter
from wikilife_crawler.twitter.device_tweets_crawler.device_reader import \
    DeviceReader
from wikilife_crawler.twitter.device_tweets_crawler.node_parse_info import \
    NodeParseInfo
from wikilife_crawler.twitter.device_tweets_crawler.tweet_text_parser import \
    TweetTextParser
from wikilife_crawler.utils import patterns


class Withings(DeviceReader):
    """
    The Withings device track current weight and desired weight 
    """

    def get_filter(self, since_id):
        q = "#withings"
        filter = TwitterSearchFilter(q)
        filter.show_user = TwitterSearchFilter.SHOW_USER_TRUE
        filter.rpp = 100 #TODO tune
        filter.since_id = since_id
        
        return filter

    def get_nodes_parse_info(self):
        
        weight = NodeParseInfo()
        weight.node_id = self._meta_ids["nodes"]["weight"]
        weight.metric_id = self._meta_ids["metrics"]["current_weight"]
        weight.pattern = ": " + patterns.REAL_PATTERN + "(| )" + patterns.WEIGHT_UNITS_PATTERN
        weight.pattern_value_index = 0
        weight.pattern_unit_index = 2
        weight.value_parser_type = TweetTextParser.WEIGHT

        return [weight]
