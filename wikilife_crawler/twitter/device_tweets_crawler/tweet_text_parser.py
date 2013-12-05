# coding=utf-8

import re
from wikilife_crawler.utils.numbers import Numbers
from wikilife_crawler.utils.units import Units
from wikilife_crawler.utils.times import Times

class TweetTextParserException(Exception):
    pass

class TweetTextParser(object):
    
    FLOAT_PRESICION = 2
    CUSTOM = "custom"
    AMOUNT_NATURAL = "amount_natural"
    AMOUNT_REAL = "amount_real"
    DISTANCE = "distance"
    WEIGHT = "weight"
    TIME_IN_MINUTES_LEFT = "time_in_minutes_left"
    TIME_IN_MINUTES_RIGHT = "time_in_minutes_right"


    @classmethod
    def parse(cls, text, info):
        
        pattern = re.compile(info.pattern)
        match = pattern.search(text)
        
        if match!=None:
            
            groups = match.groups()
            raw_value = groups[info.pattern_value_index]
            value_parser_type = info.value_parser_type
            
            if value_parser_type==cls.AMOUNT_NATURAL:
                value = Numbers.parse_int(raw_value)

            elif value_parser_type==cls.AMOUNT_REAL:
                value = round(Numbers.parse_float(raw_value), cls.FLOAT_PRESICION)
            
            elif value_parser_type==cls.DISTANCE:
                raw_unit = groups[info.pattern_unit_index]
                value = round(Units.to_km(Numbers.parse_float(raw_value), raw_unit), cls.FLOAT_PRESICION)
            
            elif value_parser_type==cls.WEIGHT:
                raw_unit = groups[info.pattern_unit_index]
                value = round(Units.to_kg(Numbers.parse_float(raw_value), raw_unit), cls.FLOAT_PRESICION)
            
            elif value_parser_type==cls.TIME_IN_MINUTES_LEFT:
                value = round(Times.parse_minutes(raw_value, ":", True), cls.FLOAT_PRESICION)
            
            elif value_parser_type==cls.TIME_IN_MINUTES_RIGHT:
                value = round(Times.parse_minutes(raw_value, ":", False), cls.FLOAT_PRESICION)
            
            elif value_parser_type==cls.CUSTOM:
                value = info.custom_parser_closure(raw_value)
            
            else:
                raise TweetTextParserException("Invalid value_parser_type='" + info.value_parser_type + "'")
            
            return value
        
        else:
            raise TweetTextParserException("pattern='" + info.pattern + "' not match in text='" + str(text) + "'")
