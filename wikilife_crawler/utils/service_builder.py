# coding=utf-8

from wikilife_crawler.twitter.delegates.twitter_search_delegate import \
    TwitterSearchDelegate
from wikilife_crawler.twitter.device_tweets_crawler.device_tweets_crawler import \
    DeviceTweetsCrawler
from wikilife_crawler.twitter.device_tweets_crawler.reader_builder import \
    ReaderBuilder
from wikilife_crawler.jobs.twitter_location import TwitterLocation


class ServiceBuilder(object):

    _settings = None
    _logger = None
    _dao_bldr = None
    _biz_srv_bldr = None

    def __init__(self, settings, logger, dao_builder, biz_service_builder):
        self._settings = settings
        self._logger = logger
        self._dao_bldr = dao_builder
        self._biz_srv_bldr = biz_service_builder

    def build_device_tweets_crawler(self):
        meta_ids = self._settings["META_IDS"]
        reader_class_fullname_list = self._settings["TWITTER_READERS"]
        twitter_search_dlgt = TwitterSearchDelegate(self._settings["TWITTER_AUTH_TOKEN"])
        meta_dao = self._dao_bldr.build_live_meta_dao()
        twitter_reader_dao = self._dao_bldr.build_twitter_reader_dao()
        log_srv = self._biz_srv_bldr.build_log_service()
        twitter_user_srv = self._biz_srv_bldr.build_twitter_user_service()
        reader_builder = ReaderBuilder(self._logger, meta_ids, twitter_search_dlgt, twitter_reader_dao, meta_dao, twitter_user_srv, log_srv)
        readers = reader_builder.build_reader_list(reader_class_fullname_list)

        return DeviceTweetsCrawler(self._logger, meta_dao, readers)

    def build_tweet_user_location(self):
        twitter_user_srv = self._biz_srv_bldr.build_twitter_user_service()

        return TwitterLocation(self._logger,  twitter_user_srv)
