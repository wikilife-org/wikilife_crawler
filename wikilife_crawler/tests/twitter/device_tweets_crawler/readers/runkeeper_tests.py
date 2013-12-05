# coding=utf-8

from wikilife_crawler.tests.base_test import BaseTest
from wikilife_crawler.twitter.device_tweets_crawler.readers.runkeeper import RunKeeper


class RunKeeperTests(BaseTest):

    reader = None

    def setUp(self):
        logger = self.get_logger()
        meta_mgr = self.get_dao_builder().build_live_meta_dao()
        self.reader = RunKeeper(logger, None, None, meta_mgr, None, None)

    def test_parse_nodes_run(self):
        text = "Just posted a 5.66 km run with @runkeeper. Check it out! http://t.co/O8Fvew5y #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 241561
        assert nodes[0]["value"] == 5.66

    def test_parse_nodes_bikeride(self):
        text = "Just completed a 20.42 km bike ride with @runkeeper. Check it out! http://t.co/eY1utQCT #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 250039
        assert nodes[0]["value"] == 20.42

    def test_parse_nodes_walk(self):
        text = "Just completed a 4.59 km walk with @runkeeper. Check it out! http://t.co/ohmPdztP #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 400
        assert nodes[0]["value"] == 4.59

    def test_parse_nodes_hiking(self):
        text = "Just completed a 10.5 km hike - Really nice morning. Cool weather, Hiking w/ hub, little jogging up a ... http://t.co/pNPJMvNf #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 250025
        assert nodes[0]["value"] == 10.5

    def test_parse_nodes_downhillskiing(self):
        text = "Just completed a 10.73 km ski run with @runkeeper. Check it out! http://t.co/tUioj8Oh #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 250028
        assert nodes[0]["value"] == 10.73
    
    """    
    def test_parse_nodes_crosscountryskiing(self):
        text = ""
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 
        assert nodes[0]["value"] == 0
    """    
        
    def test_parse_nodes_snowboarding(self):
        text = "Just completed a 1.00 km snowboard ride with @runkeeper. Check it out! http://t.co/Vn0UFvia #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 250043
        assert nodes[0]["value"] == 1.0
        
    def test_parse_nodes_skating(self):
        text = "Just completed a 14.02 km skate - First time skating this year! http://t.co/M4Yr5sYi #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 406674
        assert nodes[0]["value"] == 14.02
        
    def test_parse_nodes_swim(self):
        text = "Just posted a 1.34 km swim - Wow! http://t.co/eEtQ7QmZ #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 250019
        assert nodes[0]["value"] == 1.34
        
    """
    def test_parse_nodes_mountainbiking(self):
        text = ""
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 
        assert nodes[0]["value"] == 0
    
    def test_parse_nodes_wheelchair(self):
        text = "Just completed a 12.28 km chair ride with @runkeeper. Check it out! http://t.co/2VAz8ybq #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 
        assert nodes[0]["value"] == 12.28
    """
        
    def test_parse_nodes_elliptical(self):
        text = "Just posted a 8.56 km elliptical workout - Awesome! . http://t.co/JdMjbdk0 #RunKeeper"
        nodes = self.reader.parse_nodes(text)
        assert nodes != None
        assert len(nodes) == 1
        assert nodes[0]["nodeId"] == 250022
        assert nodes[0]["value"] == 8.56
        