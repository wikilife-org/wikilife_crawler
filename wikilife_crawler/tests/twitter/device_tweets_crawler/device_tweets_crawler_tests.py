# coding=utf-8

from wikilife_data.managers.meta.meta_manager import MetaManager
from wikilife_data.managers.template.template_manager import TemplateManager
from wikilife_data.managers.profile.profile_manager import ProfileManager
from wikilife_data.managers.logs.log_manager import LogManager
from wikilife_data.managers.users.user_manager import UserManager
from wikilife_data.managers.crawler.twitter.twitter_reader_manager import TwitterReaderManager
from wikilife_data.managers.crawler.twitter.twitter_user_manager import TwitterUserManager
from wikilife_crawler.twitter.delegates.twitter_search_delegate import TwitterSearchDelegate
from wikilife_crawler.twitter.device_tweets_crawler.device_tweets_crawler import DeviceTweetsCrawler
from wikilife_crawler.twitter.device_tweets_crawler.readers.fitbit import Fitbit
from wikilife_crawler.twitter.device_tweets_crawler.readers.micoach import MiCoach
from wikilife_crawler.twitter.device_tweets_crawler.readers.nikeplus import Nikeplus
from wikilife_crawler.twitter.device_tweets_crawler.readers.runkeeper import RunKeeper
from wikilife_crawler.twitter.device_tweets_crawler.readers.withings import Withings
from wikilife_crawler.twitter.device_tweets_crawler.readers.zeo import Zeo
from wikilife_crawler.tests.base_test import BaseTest
from wikilife_crawler.tests.test_utils import TestUtils

class DeviceTweetsCrawlerTests(BaseTest):
    
    db = None
    tpl_mgr = None
    profile_mgr = None
    user_mgr = None
    
    def setUp(self):
        self.db = self.get_conn().test_device_tweet_crawler
        self.drop_sequences(self.db)
        self.db.profile.drop()
        self.db.template.drop()
        self.db.twitter_readers.drop()
        self.db.twitter_users.drop()
        self.db.meta.drop()
        self._import_meta()
        
        self.tpl_mgr = TemplateManager(self.get_logger(), self.db)
        self.tpl_mgr.create_template(ProfileManager.TEMPLATE_NAMESPACE, TestUtils.get_profile_tpl())
        self.profile_mgr = ProfileManager(self.get_logger(), self.db, self.tpl_mgr)
        self.user_mgr = UserManager(self.profile_mgr)
    
    def tearDown(self):
        self.drop_sequences(self.db)
        self.db.meta.drop()
        self.db.profile.drop()
        self.db.template.drop()
        self.db.twitter_readers.drop()
        self.db.twitter_users.drop()
    
    def test_crawl(self):
        logger = self.get_logger()
        db = self.db
        
        twitter_search_dlgt = TwitterSearchDelegate()
        twitter_reader_mgr = TwitterReaderManager(logger, db)
        twitter_user_mgr = TwitterUserManager(self.user_mgr)
        meta_mgr = MetaManager(logger, db)
        log_mgr = LogManager(logger, db, meta_mgr, self.profile_mgr, self.user_mgr)
        
        fitbit = Fitbit(logger, twitter_search_dlgt, twitter_reader_mgr, twitter_user_mgr, meta_mgr, log_mgr)
        withings = Withings(logger, twitter_search_dlgt, twitter_reader_mgr, twitter_user_mgr, meta_mgr, log_mgr)
        nikeplus = Nikeplus(logger, twitter_search_dlgt, twitter_reader_mgr, twitter_user_mgr, meta_mgr, log_mgr)
        zeo = Zeo(logger, twitter_search_dlgt, twitter_reader_mgr, twitter_user_mgr, meta_mgr, log_mgr)
        micoach = MiCoach(logger, twitter_search_dlgt, twitter_reader_mgr, twitter_user_mgr, meta_mgr, log_mgr)
        runkeeper = RunKeeper(logger, twitter_search_dlgt, twitter_reader_mgr, twitter_user_mgr, meta_mgr, log_mgr)
        
        readers = [fitbit, withings, nikeplus, zeo, micoach, runkeeper]
        
        crawler = DeviceTweetsCrawler(logger, readers)
        success = crawler.crawl()
        
        assert success==True
    
    
    """ Helpers """
    
    def _import_meta(self):
        real_meta = self.get_conn().wikilife.meta
        test_meta = self.db.meta
        test_meta.drop()
        
        for item in real_meta.find():
            test_meta.save(item)
        
