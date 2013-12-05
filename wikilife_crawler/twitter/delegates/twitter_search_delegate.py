# coding=utf-8

from wikilife_crawler.twitter.delegates.base_twitter_delegate import \
    BaseTwitterDelegate, QueryString


class TwitterSearchDelegateException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class TwitterSearchFilter(object):
    """
    https://dev.twitter.com/docs/api/1/get/search
    """
    
    RESULT_TYPE_MIXED = "mixed"
    RESULT_TYPE_RECENT = "recent"
    RESULT_TYPE_POPULAR = "popular"
    SHOW_USER_TRUE = "true"
    SHOW_USER_FALSE = "false"
    
    def __init__(self, q, since_id=None, result_type=None, show_user=SHOW_USER_FALSE, geocode=None, lang=None, locale=None, page=None, rpp=None, until=None):
        self.q = q
        self.since_id = since_id
        self.geocode = geocode
        self.lang = lang
        self.locale = locale
        self.page = page
        self.result_type = result_type
        self.rpp = rpp
        self.show_user = show_user
        self.until = until


class TwitterSearchDelegate(BaseTwitterDelegate):
    """
    https://dev.twitter.com/docs/api/1.1/get/search/tweets
    """
    
    SEARCH_SERVICE_URL = "https://api.twitter.com/1.1/search/tweets.json"
    
    def search(self, filter):
        self._validate_search_filter(filter)

        #TODO code review: prefiero hacerlo a mano para tener más control, parámetro por parámetro y su matcheo, ej: qs.add_param_from_obj(filter, "q", "myObjPropname") 
        qs = QueryString()
        qs.add_param_from_obj(filter, "q")
        qs.add_param_from_obj(filter, "since_id")
        qs.add_param_from_obj(filter, "geocode")
        qs.add_param_from_obj(filter, "lang")
        qs.add_param_from_obj(filter, "locale")
        qs.add_param_from_obj(filter, "page")
        qs.add_param_from_obj(filter, "result_type")
        qs.add_param_from_obj(filter, "rpp")
        qs.add_param_from_obj(filter, "show_user")
        qs.add_param_from_obj(filter, "until")
        
        response = self.get(TwitterSearchDelegate.SEARCH_SERVICE_URL, qs)
        
        return response
    
    def _validate_search_filter(self, search_filter):
        #TODO improve validation
        if search_filter.q == None:
            raise TwitterSearchDelegateException("q param is required")
