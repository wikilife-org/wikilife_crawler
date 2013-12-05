# coding=utf-8

import dateutil.parser


class TweetDateParser(object):
    """
    Standard wikilife date parser
    """

    @staticmethod
    def from_datetime(str_value):
        """
        str_value: String formatted datetime
        Returns: Date
        Raises:
        """
        return dateutil.parser.parse(str_value)
