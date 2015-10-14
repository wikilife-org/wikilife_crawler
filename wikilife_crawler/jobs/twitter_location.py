
import time


class TwitterLocation(object):

    def __init__(self, logger, twitter_srv):

        self._logger = logger
        self._twitter_srv = twitter_srv

    def run(self):
        #Get all users without location and from twitter crawler
        #run the method from the wikilifeBiz obtain_twitter_user_location
        
        while True:
            twitter_users = self._twitter_srv.get_twitter_users_with_no_location()
            for twitter_user in twitter_users:
                try:
                    self._twitter_srv.obtain_twitter_user_location(twitter_user[0], twitter_user[1])
                except:
                    time.sleep(10)
                time.sleep(7)




