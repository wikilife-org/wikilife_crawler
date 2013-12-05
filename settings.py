# coding=utf-8

from os import path
import logging

#===================================
#   LOGGING
#===================================
LOGGER = logging.getLogger('wikilife_crawler')
hdlr = logging.FileHandler(path.join(path.dirname(__file__), "logs/wikilife_crawler.log"))
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
LOGGER.addHandler(hdlr)
LOGGER.setLevel(logging.INFO)

#===================================
#   TWITTER_READERS
#===================================

TWITTER_READERS = [
    "wikilife_crawler.twitter.device_tweets_crawler.readers.fitbit.Fitbit", 
    "wikilife_crawler.twitter.device_tweets_crawler.readers.micoach.MiCoach", 
    "wikilife_crawler.twitter.device_tweets_crawler.readers.nikeplus.Nikeplus", 
    "wikilife_crawler.twitter.device_tweets_crawler.readers.runkeeper.RunKeeper", 
    "wikilife_crawler.twitter.device_tweets_crawler.readers.withings.Withings" 
]

TWITTER_AUTH_TOKEN = "AAAAAAAAAAAAAAAAAAAAADN1RQAAAAAAmVtYyNrCtp59urnIfj5u1f5ZEV8%3DECQSxvLGArFNd0SqMtN7uoOLdmqf7A1prf0kzKYMGY"

#required by user_service builder, not used by crawler 
QUEUE_OPERS = {"host": "", "port": 0, "name": ""}


DB_SETTINGS = {
    "db_meta_live": {},
    "db_meta_edit": {},
    "db_users": {"name": "wikilife_users"},
    "db_logs": {"name": "wikilife_logs"},
    "db_processors": {"name": "wikilife_processors"},
    "db_crawler": {"name": "wikilife_crawler"},
    "db_apps": {"name": "wikilife_apps"},
    "db_admin": {"name": "wikilife_admin"},
    "db_location": {"name": "geonames"}
}


META_IDS = {
    "nodes": {
        "walking": 1011,
        "running": 814,
        "bikeride": 536,
        "hike": 620,
        "ski": 559,
        "snowboard": 878,
        "skate": 842,
        "swim": 921,
        "elliptical": 564, 
        "weight": 271245
    },
    "metrics": {
        "steps": 2345,
        "distance": 2344,
        "calories": 394,
        "current_weight": 271246
    }
}