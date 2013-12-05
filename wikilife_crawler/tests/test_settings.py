from os import path
import socket

#===================================
#   LOGGING CONFIGURATION
#===================================

import logging
logger = logging.getLogger('test_wikilife_crawler')
hdlr = logging.FileHandler(path.join(path.dirname(__file__), "logs/test_wikilife_crawler.log"))
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

#===================================
#   MONGO CONFIGURATION
#===================================
PROD_SERVER = "api1"
DEV_SERVER = "dev2"

HOST = socket.gethostname()

if HOST == PROD_SERVER:
    MONGO_HOST = 'db1'
    MONGO_PORT = 27017
elif HOST == DEV_SERVER:
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017
else:
    #LOCAL DEV
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017

print "wikilife_crawler.test_settings"
