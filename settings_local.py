# coding=utf-8        

#===================================
#  LOCAL DEV ENVIRONMENT SETTINGS
#===================================
#Tornado run on local developer machine (localhost)

from settings import *


# The following will be used for any DB that does not EXPLICITLY override these values.
DB_SETTINGS = {
    "db_meta_live": {},
    "db_meta_edit": {},
    "db_users": {"name": "wikilife_users_v4"},
    "db_logs": {"name": "wikilife_logs_v4"},
    "db_processors": {"name": "wikilife_processors_v4"},
    "db_crawler": {"name": "wikilife_crawler_v4"},
    "db_apps": {"name": "wikilife_apps_v4"},
    "db_admin": {"name": "wikilife_admin_v4"},
    "db_location": {"name": "geonames"}
}

DB_SETTINGS_DEFAULT = {
    "host": "localhost",
    "port": 27017,
}

DB_SETTINGS["db_meta_live"]["uri"] = "http://174.129.230.61:7474/db/data/"

DB_SETTINGS["db_location"]["port"] = 5432
DB_SETTINGS["db_location"]["user"] = "postgres"
DB_SETTINGS["db_location"]["pass"] = "admin"



QUEUE_LOGS = {"host": "localhost", "port": 5672, "name": "log_queue"}
QUEUE_OPERS = {"host": "localhost", "port": 5672, "name": "oper_queue"}

TWITTER_READERS = [
    "wikilife_crawler.twitter.device_tweets_crawler.readers.fitbit.Fitbit", 
    "wikilife_crawler.twitter.device_tweets_crawler.readers.micoach.MiCoach", 
    "wikilife_crawler.twitter.device_tweets_crawler.readers.nikeplus.Nikeplus", 
    "wikilife_crawler.twitter.device_tweets_crawler.readers.runkeeper.RunKeeper", 
    "wikilife_crawler.twitter.device_tweets_crawler.readers.withings.Withings"
]