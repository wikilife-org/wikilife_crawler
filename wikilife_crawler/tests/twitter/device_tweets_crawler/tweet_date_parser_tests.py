# coding=utf-8

from wikilife_crawler.tests.base_test import BaseTest
from wikilife_crawler.twitter.device_tweets_crawler.tweet_date_parser import TweetDateParser

class TweetDateParserTests(BaseTest):

    def test_from_datetime(self):
        raw_dt_str = "Thu, 06 Sep 2012 21:01:38 +0000"
        print "raw dt: %s" %raw_dt_str

        dt_year = 2012
        dt_month = 9
        dt_day = 6
        dt_hour = 21
        dt_minute = 1
        dt_second = 38
        
        dt = TweetDateParser.from_datetime(raw_dt_str)
        print "parsed dt: %s" %dt
        
        assert dt.year == dt_year
        assert dt.month == dt_month
        assert dt.day == dt_day
        assert dt.hour == dt_hour
        assert dt.minute == dt_minute
        assert dt.second == dt_second
