# coding=utf-8

from wikilife_crawler.tests.base_test import BaseTest
from wikilife_crawler.twitter.device_tweets_crawler.readers.withings import Withings


class WithingsTests(BaseTest):

    reader = None

    def setUp(self):
        logger = self.get_logger()
        meta_mgr = self.get_dao_builder().build_live_meta_dao()
        self.reader = Withings(logger, None, None, meta_mgr, None, None)

    def test_parse_nodes_basic(self):
        
        text = "orimekko: My weight: 71.1 kg. 1.1 kg to go.  #withings http://withings.jp"

        nodes = self.reader.parse_nodes(text)
        
        assert nodes != None
        assert len(nodes) == 1
        
        weight_node = nodes[0]
        assert weight_node["nodeId"] == 1140
        assert weight_node["value"] == 71.1
        
    
    def NO_test_parse_nodes_no_value_unit_space(self):
        
        text = "tknx04: 今日の体重: 52.55Kg, 体脂肪率: 5.64% http://t.co/d5kX41Tk #withings http://t.co/GtVSJ3OZ"

        nodes = self.reader.parse_nodes(text)
        
        assert nodes != None
        assert len(nodes) == 1
        
        distance_node = nodes[0]
        assert distance_node["value"] == 52.55

        """
        "text": "oishi: My weight: 54.2 kg. #withings http://withings.jp",
        "text": "tknx04: 今日の体重: 52.55Kg, 体脂肪率: 5.64% http://t.co/d5kX41Tk #withings http://t.co/GtVSJ3OZ",
        "text": "oishi: My weight: 54.1 kg. #withings http://withings.jp",
        "text": "lcahlander: I am down 10 pounds in 4 weeks. #Digifit #myfitnesspal #lifetimefitness #Withings",
        "text": "Umibell: 私の体重 : 53.9 kg. あと 1.9 kg 減らすべきです。 こんなもんだぜ(｀_´)ゞ！ http://t.co/Tt5ical #withings http://withings.jp",
        "text": "tomoakisugiyama: キャー！(((゜д゜;)))  66.9kg！ #withings http://withings.jp",
        "text": "orimekko: My weight: 72 kg. 2.1 kg to go.  #withings http://withings.jp",
        "text": "orimekko: My weight: 71.1 kg. 1.1 kg to go.  #withings http://withings.jp",
        """
 
    def test_parse_text_basic(self):
        tweet_text = "orimekko: My weight: 71.1 kg. 1.1 kg to go.  #withings http://withings.jp"
        log_nodes = self.reader.parse_nodes(tweet_text)
        text = self.reader.parse_text(log_nodes)
        assert text == "Weight Current 71.1 kg"

