# coding=utf-8

from wikilife_biz.utils.biz_service_builder import BizServiceBuilder
from wikilife_crawler.utils.service_builder import ServiceBuilder
from wikilife_data.utils.dao_builder import DAOBuilder
from wikilife_data.utils.db_conn import DBConn
from wikilife_utils.settings.settings_loader import SettingsLoader
import sys

def run(settings):
    service_builder = _create_service_builder(settings)
    crawler = service_builder.build_device_tweets_crawler()
    crawler.crawl()
    
def run_history_location(settings):
    service_builder = _create_service_builder(settings)
    history_location = service_builder.build_tweet_user_location()
    history_location.run()

def check_readers_meta_dependencies(settings):
    service_builder = _create_service_builder(settings)
    crawler = service_builder.build_device_tweets_crawler()
    crawler.check_readers_meta_dependencies()

def _create_service_builder(settings):
    logger = settings["LOGGER"]
    db_user = None
    db_pass = None
    db_conn = DBConn(settings["DB_SETTINGS"], db_user, db_pass)
    dao_builder = DAOBuilder(logger, db_conn)
    biz_service_builder = BizServiceBuilder(settings, logger, dao_builder)
    return ServiceBuilder(settings, logger, dao_builder, biz_service_builder)

def display_help():
    print "{env} run"
    print "{env} dep"

if __name__ == '__main__':
    env = str(sys.argv[1])
    cmd = str(sys.argv[2])
    settings = SettingsLoader().load_settings(env)
    
    if cmd == "run":
        run(settings)

    elif cmd == "dep":
        check_readers_meta_dependencies(settings)

    elif cmd == "help":
        display_help()
        
    elif cmd == "run_history_location":
        run_history_location(settings)
    else:
        print "Unknown command '%s', use:\n" %cmd
        display_help()
