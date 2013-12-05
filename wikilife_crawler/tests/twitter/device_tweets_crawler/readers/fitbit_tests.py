# coding=utf-8
from wikilife_crawler.utils.units import Units
from wikilife_crawler.twitter.device_tweets_crawler.device_reader import DeviceReaderException
from wikilife_crawler.tests.base_test import BaseTest
from wikilife_crawler.twitter.device_tweets_crawler.tweet_text_parser import TweetTextParser
from wikilife_crawler.twitter.device_tweets_crawler.readers.fitbit import Fitbit

class FitbitTests(BaseTest):
    
    reader = None
    
    def setUp(self):
        logger = self.get_logger()
        meta_mgr = self.get_dao_builder().build_live_meta_dao()
        self.reader = Fitbit(logger, None, None, meta_mgr, None, None)
    
    def test_parse_nodes_basic(self):
        
        text = "FitInMyHeart: RT @wildfirefitness: Go Mo! RT @FitInMyHeart My fitbit #fitstats for 9/08/2011: 10,015 steps and 4.2 miles traveled. http://t.co/kaxvzju"
        
        nodes = self.reader.parse_nodes(text)
        
        assert nodes != None
        assert len(nodes) == 2
        
        step_node = nodes[0]
        assert step_node["nodeId"] == 398
        assert step_node["value"] == 10015
        
        distance_node = nodes[1]
        assert distance_node["nodeId"] == 400
        assert distance_node["value"] == round(Units.miles_to_km(4.2), TweetTextParser.FLOAT_PRESICION)

    def test_parse_nodes_bad_text_values(self):
        
        test_texts = [
            "jensmccabe: RT @johnknapp: Using #fitstats and complex math, I can safely say @theculprit has longer legs than @jensmccabe. Scott's stride = 3.32' &amp; Jen's = 2.42'. :-)",
            "Matilda444: searched #fitstats and found mine are not too shabby!!!",  
            "Matilda444:"]  
    
        for text in test_texts:
            try:
                self.reader.parse_nodes(text)
                assert False

            except DeviceReaderException:
                assert True

    def test_parse_nodes(self):
        
        test_items = [
            {"text": "FitInMyHeart: RT @wildfirefitness: Go Mo! RT @FitInMyHeart My fitbit #fitstats for 9/08/2011: 10,015 steps and 4.2 miles traveled. http://t.co/kaxvzju",  
             "expected": {"step_node_value": 10015, "distance_node_value": Units.miles_to_km(4.2)}},
             
            {"text": "otownteacher2: My avg. daily fitbit #fitstats for last week: 0 steps and 0 miles traveled. http://t.co/aSOsgTl2",  
             "expected": {"step_node_value": 0, "distance_node_value": Units.miles_to_km(0)}},
                      
            {"text": "otownteacher2: My avg. daily fitbit #fitstats for last week: 1 steps and 1 miles traveled. http://t.co/aSOsgTl2",  
             "expected": {"step_node_value": 1, "distance_node_value": Units.miles_to_km(1)}},
                      
            {"text": "otownteacher2: My avg. daily fitbit #fitstats for last week: 1,500 steps and 1.5 miles traveled. http://t.co/aSOsgTl2",  
             "expected": {"step_node_value": 1500, "distance_node_value": Units.miles_to_km(1.5)}},
                      
            {"text": "otownteacher2: My avg. daily fitbit #fitstats for last week: 1,500 steps and 1,000.5 miles traveled. http://t.co/aSOsgTl2",  
             "expected": {"step_node_value": 1500, "distance_node_value": Units.miles_to_km(1000.5)}},
                      
            {"text": "racheldallaire: My avg. daily fitbit #fitstats for last week: 752 steps and 0.3 miles traveled. http://t.co/b5Ki7ME",  
             "expected": {"step_node_value": 752, "distance_node_value": Units.miles_to_km(0.3)}}
        ]
        
        for item in test_items:
            nodes = self.reader.parse_nodes(item["text"])
            assert nodes != None
            assert len(nodes) == 2
            
            step_node = nodes[0]
            assert step_node["value"] == item["expected"]["step_node_value"]
            
            distance_node = nodes[1]
            assert distance_node["value"] == round(item["expected"]["distance_node_value"], TweetTextParser.FLOAT_PRESICION)

    def test_parse_text(self):

        def to_str(min):
            return str(round(min, TweetTextParser.FLOAT_PRESICION))


        step_unit = "steps"
        distance_unit = "kilometres"

        test_items = [
            {"text": "FitInMyHeart: RT @wildfirefitness: Go Mo! RT @FitInMyHeart My fitbit #fitstats for 9/08/2011: 10,015 steps and 4.2 miles traveled. http://t.co/kaxvzju",  
             "expected": "Walking Step 10015 "+step_unit+" Distance "+to_str(Units.miles_to_km(4.2))+" "+distance_unit},

            {"text": "otownteacher2: My avg. daily fitbit #fitstats for last week: 0 steps and 0 miles traveled. http://t.co/aSOsgTl2",  
             "expected": "Walking Step 0 "+step_unit+" Distance "+to_str(Units.miles_to_km(0))+" "+distance_unit},

            {"text": "otownteacher2: My avg. daily fitbit #fitstats for last week: 1 steps and 1 miles traveled. http://t.co/aSOsgTl2",  
             "expected": "Walking Step 1 "+step_unit+" Distance "+to_str(Units.miles_to_km(1))+" "+distance_unit},

            {"text": "otownteacher2: My avg. daily fitbit #fitstats for last week: 1,500 steps and 1.5 miles traveled. http://t.co/aSOsgTl2",  
             "expected": "Walking Step 1500 "+step_unit+" Distance "+str(round(Units.miles_to_km(1.5), TweetTextParser.FLOAT_PRESICION))+" "+distance_unit},

            {"text": "otownteacher2: My avg. daily fitbit #fitstats for last week: 1,500 steps and 1,000.5 miles traveled. http://t.co/aSOsgTl2",  
             "expected": "Walking Step 1500 "+step_unit+" Distance "+str(round(Units.miles_to_km(1000.5), TweetTextParser.FLOAT_PRESICION))+" "+distance_unit},

            {"text": "racheldallaire: My avg. daily fitbit #fitstats for last week: 752 steps and 0.3 miles traveled. http://t.co/b5Ki7ME",  
             "expected": "Walking Step 752 "+step_unit+" Distance "+str(round(Units.miles_to_km(0.3), TweetTextParser.FLOAT_PRESICION))+" "+distance_unit}
        ]

        for item in test_items:
            log_nodes = self.reader.parse_nodes(item["text"])
            text = self.reader.parse_text(log_nodes)

            assert text == item["expected"]

