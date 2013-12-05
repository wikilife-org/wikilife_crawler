# coding=utf-8
from wikilife_crawler.utils.units import Units
from wikilife_crawler.tests.base_test import BaseTest
from wikilife_data.managers.meta.meta_manager import MetaManager
from wikilife_crawler.twitter.device_tweets_crawler.tweet_text_parser import TweetTextParser
from wikilife_crawler.twitter.device_tweets_crawler.readers.micoach import MiCoach
from wikilife_crawler.utils.times import Times

class MiCoachTests(BaseTest):
    reader = None
    
    def setUp(self):
        logger = self.get_logger()
        meta_mgr = self.get_dao_builder().build_live_meta_dao()
        self.reader = MiCoach(logger, None, None, meta_mgr, None, None)
    
    def test_parse_nodes_basic(self):
        
        text = "completed today's miCoach free workout - 4.1 kilometers / 08:09 pace / 33:23 min / 359 cal."
        
        nodes = self.reader.parse_nodes(text)
        
        assert nodes != None
        assert len(nodes) == 2
                
        distance_node = nodes[0]
        assert distance_node["nodeId"] == 241561
        assert distance_node["value"] == 4.1

        calories_node = nodes[1]
        assert calories_node["nodeId"] == 250017
        assert calories_node["value"] == 359
    
    def test_parse_nodes(self):
        
        test_items = [
            {"text": "completed today's miCoach free workout - 4.1 kilometers / 08:09 pace / 33:23 min / 359 cal.",  
             "expected": {"duration_node_value": Times.to_minutes(0, 33, 23), "distance_node_value": 4.1, "calories_node_value": 359}},
            {"text": "completed today's miCoach free workout - 3.02 miles / 10:58 pace / 33:9 min / 352 cal.",  
             "expected": {"duration_node_value": Times.to_minutes(0, 33, 9), "distance_node_value": Units.miles_to_km(3.02), "calories_node_value": 352}},
            {"text": "HebdenBen: completed today's miCoach free workout - 4.58 miles / 10:49 pace / 49:35 min / 740 cal.",  
             "expected": {"duration_node_value": Times.to_minutes(0, 49, 35), "distance_node_value": Units.miles_to_km(4.58), "calories_node_value": 740}},
            {"text": "Siggi05: completed today's miCoach free workout - 8.5 kilometers / 05:47 pace / 49:8 min / 806 cal.",  
             "expected": {"duration_node_value": Times.to_minutes(0, 49, 8), "distance_node_value": 8.5, "calories_node_value": 806}}
        ]
        
        for item in test_items:
            nodes = self.reader.parse_nodes(item["text"])
            assert nodes != None
            assert len(nodes) == 2
            
            distance_node = nodes[0]
            assert distance_node["value"] == round(item["expected"]["distance_node_value"], TweetTextParser.FLOAT_PRESICION)

            calories_node = nodes[1]
            assert calories_node["value"] == item["expected"]["calories_node_value"]

    def test_parse_text(self):

        distance_unit = "km"
        calories_unit = "cal"

        test_items = [
            {"text": "completed today's miCoach free workout - 4.1 kilometers / 08:09 pace / 33:30 min / 359 cal.",  
             "expected": "Running Distance 4.1 "+distance_unit + " Calories Burned 359 " + calories_unit},
            {"text": "completed today's miCoach free workout - 3.02 miles / 10:58 pace / 33:15 min / 352 cal.",  
             "expected": "Running Distance "+str(round(Units.miles_to_km(3.02), TweetTextParser.FLOAT_PRESICION))+" "+distance_unit + " Calories Burned 352 " + calories_unit}
        ]

        for item in test_items:
            log_nodes = self.reader.parse_nodes(item["text"])
            text = self.reader.parse_text(log_nodes)

            assert text == item["expected"]
