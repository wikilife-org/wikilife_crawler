# coding=utf-8
from wikilife_crawler.utils import patterns
import re

class Units(object):

    MILES_KM = 1.609344
    LB_KG = 0.45359237
    
    @classmethod
    def miles_to_km(cls, miles_value):
        """
        returns km_value
        """
        return miles_value*cls.MILES_KM
    
    @classmethod
    def lb_to_kg(cls, lb_value):
        """
        returns kg_value
        """
        return lb_value*cls.LB_KG
    
    @classmethod
    def to_km(cls, value, unit):
        if re.match(patterns.MILE_UNIT_PATTERN_C, unit):
            value = cls.miles_to_km(value)

        return value
    
    @classmethod
    def to_kg(cls, value, unit):
        if re.match(patterns.LB_UNIT_PATTERN_C, unit):
            value = cls.lb_to_kg(value)

        return value
