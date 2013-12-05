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


class Fitbit(DeviceReader):
    """ 
    The Fitbit device track steps and distance 
    """

    def get_filter(self, since_id):
        q = "#fitstats"
        filter = TwitterSearchFilter(q)
        filter.show_user = TwitterSearchFilter.SHOW_USER_TRUE
        filter.rpp = 100 #TODO tune
        filter.since_id = since_id 

        return filter

    def get_nodes_parse_info(self):
        
        steps = NodeParseInfo()
        #steps.node_namespace = "wikilife.exercise.exercise.exercise.walking.step.value-node"
        steps.node_id = self._meta_ids["nodes"]["walking"]
        steps.metric_id = self._meta_ids["metrics"]["steps"]
        steps.pattern = patterns.NATURAL_PATTERN + " (steps)"
        steps.pattern_value_index = 0
        steps.value_parser_type = TweetTextParser.AMOUNT_NATURAL

        distance = NodeParseInfo
        #distance.node_namespace = "wikilife.exercise.exercise.exercise.walking.distance.value-node"
        distance.node_id = self._meta_ids["nodes"]["walking"]
        distance.metric_id = self._meta_ids["metrics"]["distance"]
        distance.pattern =  patterns.REAL_PATTERN + " " + patterns.DISTANCE_UNITS_PATTERN
        distance.pattern_value_index = 0
        distance.pattern_unit_index = 1
        distance.value_parser_type = TweetTextParser.DISTANCE

        return [steps, distance]
