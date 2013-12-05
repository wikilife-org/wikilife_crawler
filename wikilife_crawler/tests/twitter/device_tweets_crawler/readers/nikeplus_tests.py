# coding=utf-8

from wikilife_crawler.tests.base_test import BaseTest
from wikilife_crawler.twitter.device_tweets_crawler.device_reader import \
    DeviceReaderException
from wikilife_crawler.twitter.device_tweets_crawler.readers.nikeplus import \
    Nikeplus
from wikilife_crawler.twitter.device_tweets_crawler.tweet_text_parser import \
    TweetTextParser
from wikilife_crawler.utils.times import Times
from wikilife_crawler.utils.units import Units


class NikeplusTests(BaseTest):

    reader = None

    def setUp(self):
        logger = self.get_logger()
        meta_mgr = self.get_dao_builder().build_live_meta_dao()
        self.reader = Nikeplus(logger, None, None, meta_mgr, None, None)

    def test_parse_nodes_basic(self):

        text = "vvvblanco: I just finished a 1,5 km run with a time of 15:45 with Nike+ GPS. #nikeplus"

        nodes = self.reader.parse_nodes(text)

        assert nodes != None
        assert len(nodes) == 1

        distance_node = nodes[0]
        assert distance_node["nodeId"] == 241561
        assert distance_node["value"] == 1.5

    def test_parse_nodes_bad_text_values(self):

        test_texts = ["nga802: のランを走り終えました。Nike+ GPSによるペースは6'09&quot;/km、タイムは39:07でした。 #nikeplus"]

        for text in test_texts:
            try:
                self.reader.parse_nodes(text)
                assert False

            except DeviceReaderException:
                assert True

    def test_parse_nodes(self):

        test_items = [
            {"text": "vvvblanco: I just finished a 1,5 km run with a time of 15:45 with Nike+ GPS. #nikeplus",
             "expected": {"distance_node_value": 1.5}},
            {"text": "jwdfrench: I just finished a 1.93 mi run with a time of 20:19 with Nike+ GPS. #nikeplus",
             "expected": {"distance_node_value": Units.miles_to_km(1.93)}},
            {"text": "sloggi1999: I just finished a 13,1 km run with a time of 1:19:02 with Nike+ GPS. #nikeplus",
             "expected": {"distance_node_value": 13.1}},
            {"text": "TheJakeErdely: I just finished a 4.23 mi run with a pace of 9'56&quot;/mi and a time of 42:02 with Nike+ GPS. #nikeplus",
             "expected": {"distance_node_value": Units.miles_to_km(4.23)}}
        ]

        for item in test_items:
            nodes = self.reader.parse_nodes(item["text"])
            assert nodes != None
            assert len(nodes) == 1

            distance_node = nodes[0]
            assert distance_node["value"] == round(item["expected"]["distance_node_value"], TweetTextParser.FLOAT_PRESICION)

    def test_parse_text(self):
        
        def to_str(min):
            return str(round(min, TweetTextParser.FLOAT_PRESICION))
        
        test_items = [
            {"text": "vvvblanco: I just finished a 1,5 km run with a time of 15:45 with Nike+ GPS. #nikeplus",
             "expected": "Running Distance 1.5 km"},
            {"text": "jwdfrench: I just finished a 1.93 mi run with a time of 20:19 with Nike+ GPS. #nikeplus",
             "expected": "Running Distance "+to_str(Units.miles_to_km(1.93))+" km"},
            {"text": "sloggi1999: I just finished a 13,1 km run with a time of 1:19:02 with Nike+ GPS. #nikeplus",
             "expected": "Running Distance 13.1 km"},
            {"text": "TheJakeErdely: I just finished a 4.23 mi run with a pace of 9'56&quot;/mi and a time of 42:02 with Nike+ GPS. #nikeplus",
             "expected": "Running Distance "+to_str(Units.miles_to_km(4.23))+" km"}
        ]

        for item in test_items:
            log_nodes = self.reader.parse_nodes(item["text"])
            text = self.reader.parse_text(log_nodes)
            
            assert text == item["expected"]
