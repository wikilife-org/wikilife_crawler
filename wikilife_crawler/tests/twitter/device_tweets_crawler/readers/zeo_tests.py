# coding=utf-8

from wikilife_crawler.tests.base_test import BaseTest
from wikilife_crawler.twitter.device_tweets_crawler.readers.zeo import Zeo
from wikilife_crawler.utils.times import Times


class ZeoTests(BaseTest):

    reader = None

    def setUp(self):
        logger = self.get_logger()
        meta_mgr = self.get_dao_builder().build_live_meta_dao()
        self.reader = Zeo(logger, None, None, meta_mgr, None, None)

    def test_parse_nodes_basic(self):
        text = "Damons_Sleep: I slept 7h 03m on Sep 13. #ZQ: 88. Deep: 1h 54m. REM: 1h 17m. Awake: 4m. http://t.co/4X6GtkR #Zeo #sleepdata"
        nodes = self.reader.parse_nodes(text)

        assert nodes != None
        assert len(nodes) == 3

        deep_node = nodes[0]
        assert deep_node["nodeId"] == 241563 
        assert deep_node["value"] == Times.to_minutes(1, 54, 0)

        rem_node = nodes[1]
        assert rem_node["nodeId"] == 241565
        assert rem_node["value"] == Times.to_minutes(1, 17, 0)

        awake_node = nodes[2]
        assert awake_node["nodeId"] == 241567
        assert awake_node["value"] == Times.to_minutes(0, 4, 0)

    def test_parse_nodes(self):
        test_items = [
            {"text": "Damons_Sleep: I slept 7h 03m on Sep 13. #ZQ: 88. Deep: 1h 54m. REM: 1h 17m. Awake: 4m. http://t.co/4X6GtkR #Zeo #sleepdata",  
             "expected": {"duration_node_value": Times.to_minutes(7, 3, 0), "deep_node_value": Times.to_minutes(1, 54, 0), "rem_node_value": Times.to_minutes(1, 17, 0), "awake_node_value": Times.to_minutes(0, 4, 0)}},

            {"text": "jlEcth: I slept 4h 58m on Sep 13. #ZQ: 47. Deep: 37m. REM: 59m. Awake: 1h 07m. http://t.co/hYBelTZ #Zeo #sleepdata",  
             "expected": {"duration_node_value": Times.to_minutes(4, 58, 0), "deep_node_value": Times.to_minutes(0, 37, 0), "rem_node_value": Times.to_minutes(0, 59, 0), "awake_node_value": Times.to_minutes(1, 7, 0)}},

            {"text": "jlEcth: I slept 4h 58m on Sep 13. #ZQ: 47. Deep: 37m. REM: 59m. Awake: 1h 07m. http://t.co/hYBelTZ #Zeo #sleepdata",  
             "expected": {"duration_node_value": Times.to_minutes(4, 58, 0), "deep_node_value": Times.to_minutes(0, 37, 0), "rem_node_value": Times.to_minutes(0, 59, 0), "awake_node_value": Times.to_minutes(1, 7, 0)}}
        ]
        
        for item in test_items:
            nodes = self.reader.parse_nodes(item["text"])
            assert nodes != None
            assert len(nodes) == 3
            
            deep_node = nodes[0]
            assert deep_node["value"] == item["expected"]["deep_node_value"]
            
            rem_node = nodes[1]
            assert rem_node["value"] == item["expected"]["rem_node_value"]
            
            awake_node = nodes[2]
            assert awake_node["value"] == item["expected"]["awake_node_value"]

    def test_parse_text(self):
        deep_unit = "minutes"
        rem_unit = "minutes"
        awake_unit = "minutes"
        
        test_items = [
            {"text": "Damons_Sleep: I slept 7h 03m on Sep 13. #ZQ: 88. Deep: 1h 54m. REM: 1h 17m. Awake: 4m. http://t.co/4X6GtkR #Zeo #sleepdata",  
             "expected": "Sleep Deep " +str(Times.to_minutes(1, 54, 0)) + " " + deep_unit + " Rem " +str(Times.to_minutes(1, 17, 0)) + " " + rem_unit +  " Awake " +str(Times.to_minutes(0, 4, 0)) + " " + awake_unit},

            {"text": "jlEcth: I slept 4h 58m on Sep 13. #ZQ: 47. Deep: 37m. REM: 59m. Awake: 1h 07m. http://t.co/hYBelTZ #Zeo #sleepdata",  
             "expected": "Sleep Deep " +str(Times.to_minutes(0, 37, 0)) + " " + deep_unit + " Rem " +str(Times.to_minutes(0, 59, 0)) + " " + rem_unit +  " Awake " +str(Times.to_minutes(1, 7, 0)) + " " + awake_unit},

            {"text": "jlEcth: I slept 4h 58m on Sep 13. #ZQ: 47. Deep: 37m. REM: 59m. Awake: 1h 07m. http://t.co/hYBelTZ #Zeo #sleepdata",  
             "expected": "Sleep Deep " +str(Times.to_minutes(0, 37, 0)) + " " + deep_unit + " Rem " +str(Times.to_minutes(0, 59, 0)) + " " + rem_unit +  " Awake " +str(Times.to_minutes(1, 7, 0)) + " " + awake_unit}
        ]
        
        for item in test_items:
            log_nodes = self.reader.parse_nodes(item["text"])
            text = self.reader.parse_text(log_nodes)

            assert text == item["expected"]
