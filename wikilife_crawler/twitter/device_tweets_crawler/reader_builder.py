# coding=utf-8

class ReaderBuilderException(Exception):
    pass

class ReaderBuilder(object):

    def __init__(self, logger, meta_ids, twitter_search_delegate, twitter_reader_dao, meta_dao, twitter_user_service, log_service):
        self._logger = logger
        self._meta_ids = meta_ids
        self._twitter_search_dlgt = twitter_search_delegate
        self._twitter_reader_dao = twitter_reader_dao
        self._meta_dao = meta_dao
        self._twitter_user_srv = twitter_user_service
        self._log_srv = log_service

    def build_reader(self, reader_class_fullname):
        ReaderClass = self._get_class(reader_class_fullname)
        reader = ReaderClass(self._logger, self._meta_ids, self._twitter_search_dlgt, self._twitter_reader_dao, self._meta_dao, self._twitter_user_srv, self._log_srv)

        return reader

    def build_reader_list(self, reader_class_fullname_list):
        readers = []

        for class_fullname in reader_class_fullname_list:
            reader = self.build_reader(class_fullname)
            readers.append(reader)

        return readers

    def _get_class(self, kls):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        
        for comp in parts[1:]:
            m = getattr(m, comp)

        return m
