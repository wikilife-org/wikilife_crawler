#!/bin/sh

#Crontab line
#PROD
#00,30 * *   *   *    /home/tornado/wikilife_backend/wikilife_crawler/wikilife_crawler/twitter/device_tweets_crawler/cron_script.sh prod run /home/tornado/wikilife_backend/wikilife_crawler > /dev/null 2>&1

#DEV
#00,30 * *   *   *    /home/masterdev/API2/wikilife_backend/wikilife_crawler/wikilife_crawler/twitter/device_tweets_crawler/cron_script.sh local run /home/masterdev/API2/wikilife_backend/wikilife_crawler > /dev/null 2>&1

cd $3

export PYTHONPATH=$PYTHONPATH:$PWD;
export PYTHONPATH=$PYTHONPATH:$PWD/../wikilife_utils;
export PYTHONPATH=$PYTHONPATH:$PWD/../wikilife_data;
export PYTHONPATH=$PYTHONPATH:$PWD/../wikilife_biz;

echo "wikilife_crawler DeviceTweetsCrawler env: $1, cmd: $2";
python wikilife_crawler/twitter/device_tweets_crawler/manage.py $1 $2;
