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


class RunKeeper(DeviceReader):
    """
    The RunKeeper device track distance of:
     running
     cycling/bike ride   
     walking
     hiking
     downhill skiing
     cross-country skiing
     snowboarding
     skating
     swimming
     mountain biking
     wheelchair
     elliptical
     other
    """

    def get_filter(self, since_id):
        q = "#RunKeeper"
        filter = TwitterSearchFilter(q)
        filter.show_user = TwitterSearchFilter.SHOW_USER_TRUE
        filter.rpp = 100 #TODO tune
        filter.since_id = since_id

        return filter

    def get_nodes_parse_info(self):

        distance_metric_id = self._meta_ids["metrics"]["distance"]
        
        exercise_id_map = {
            "run": {"node_id": self._meta_ids["nodes"]["running"], "metric_id": distance_metric_id},
            "bike ride": {"node_id": self._meta_ids["nodes"]["bikeride"], "metric_id": distance_metric_id},
            "walk": {"node_id": self._meta_ids["nodes"]["walking"], "metric_id": distance_metric_id},
            "hike": {"node_id": self._meta_ids["nodes"]["hike"], "metric_id": distance_metric_id},
            "ski": {"node_id": self._meta_ids["nodes"]["ski"], "metric_id": distance_metric_id},
            "snowboard": {"node_id": self._meta_ids["nodes"]["snowboard"], "metric_id": distance_metric_id},
            "skate": {"node_id": self._meta_ids["nodes"]["skate"], "metric_id": distance_metric_id},
            "swim": {"node_id": self._meta_ids["nodes"]["swim"], "metric_id": distance_metric_id},
            "elliptical": {"node_id": self._meta_ids["nodes"]["elliptical"], "metric_id": distance_metric_id}
        }

        nodes = []

        for key in exercise_id_map:
            item = exercise_id_map[key]
            node_id = item["node_id"]
            metric_id = item["metric_id"]
            node = NodeParseInfo()

            node.node_id = node_id
            node.metric_id = metric_id
            node.pattern =  patterns.REAL_PATTERN + " " + patterns.DISTANCE_UNITS_PATTERN + " " + key
            node.pattern_value_index = 0
            node.pattern_unit_index = 1
            node.value_parser_type = TweetTextParser.DISTANCE

            nodes.append(node)

        return nodes 
