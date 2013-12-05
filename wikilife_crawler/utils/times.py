# coding=utf-8
from wikilife_crawler.utils.numbers import Numbers

class Times(object):
    
    HOUR = "hours" 
    MINUTE = "minutes" 
    SECOND = "seconds" 
    
    @classmethod
    def parse_time(cls, raw_value, input_unit, output_unit):
        """
        Converts a string value representing hours, minutes or seconds specified by the input_unit parameter (Times.HOUR, Times.MINUTE, Times.SECOND) to a decimal value in hours, minutes or seconds specified by the output_unit parameter (Times.HOUR, Times.MINUTE, Times.SECOND).
        parse_time("1", Times.HOUR, Times.HOUR) >> 1.0
        parse_time("1", Times.HOUR, Times.MINUTE) >> 60.0
        parse_time("1", Times.HOUR, Times.SECOND) >> 3600.0
        parse_time("45", Times.MINUTE, Times.HOUR) >> 0.75
        parse_time("30", Times.SECOND, Times.MINUTE) >> 0.5
        parse_time("90", Times.SECOND, Times.HOUR) >> 0.025
        """
        
        value = Numbers.parse_int(raw_value)
        h = 0
        m = 0
        s = 0
        
        if input_unit==cls.HOUR:
            h = value
        elif input_unit==cls.MINUTE:
            m = value
        elif input_unit==cls.SECOND:
            s = value
        else:
            raise Exception("Invalid input_unit")
        
        if output_unit==cls.HOUR:
            value = cls.to_hours(h, m, s)
        elif output_unit==cls.MINUTE:
            value = cls.to_minutes(h, m, s)
        elif output_unit==cls.SECOND:
            value = cls.to_seconds(h, m, s)
        else:
            raise Exception("Invalid output_unit")
        
        return value
    
    @classmethod
    def parse_hours(cls, raw_value, separator=":", left_unit_anchor=True):
        """
        Converts a time string with format hh:mm:ss to hours in decimal system
        """
        
        h, m, s = cls.parse_h_m_s(raw_value, separator, left_unit_anchor)
        return cls.to_hours(h, m, s) 

    @classmethod
    def parse_minutes(cls, raw_value, separator=":", left_unit_anchor=True):
        """
        Converts a time string with format hh:mm:ss to minutes in decimal system
        """
        
        h, m, s = cls.parse_h_m_s(raw_value, separator, left_unit_anchor)
        return cls.to_minutes(h, m, s) 
    
    @classmethod
    def parse_seconds(cls, raw_value, separator=":", left_unit_anchor=True):
        """
        Converts a time string with format hh:mm:ss to seconds in decimal system
        """
        
        h, m, s = cls.parse_h_m_s(raw_value, separator, left_unit_anchor)
        return cls.to_seconds(h, m, s) 
    
    @classmethod
    def parse_h_m_s(cls, raw_value, separator=":", left_unit_anchor=True):
        """
        Converts a time string with format hh:mm:ss to a tuple (h, m, s)
        Supports hh:mm, mm:ss, hh, ss,  using left_unit_anchor parameter
        """
        
        tmp = raw_value.split(separator)
        
        units_len = len(tmp)
        
        if units_len==3:
            h = Numbers.parse_int(tmp[0])
            m = Numbers.parse_int(tmp[1])
            s = Numbers.parse_int(tmp[2])
        
        elif units_len==2:
            
            if left_unit_anchor:
                h = Numbers.parse_int(tmp[0])
                m = Numbers.parse_int(tmp[1])
                s = 0
            else:
                h = 0
                m = Numbers.parse_int(tmp[0])
                s = Numbers.parse_int(tmp[1])

        elif units_len==1:
            
            if left_unit_anchor:
                h = Numbers.parse_int(raw_value)
                m = 0
                s = 0
            else:
                h = 0
                m = 0
                s = Numbers.parse_int(raw_value)

        else:
            raise Exception("Invalid time format")
        
        return (h, m, s)
    
    @classmethod
    def parse_h_m(cls, raw_value, separator=":"):
        """
        Converts a time string with format hh:mm to a tuple (h, m)
        """
        
        tmp = raw_value.split(separator)
        
        h = Numbers.parse_int(tmp[0])
        m = Numbers.parse_int(tmp[1])
        
        return (h, m)
    
    @classmethod
    def parse_m_s(cls, raw_value, separator=":"):
        """
        Converts a time string with format mm:ss to a tuple (m, s)
        """
        tmp = raw_value.split(separator)
        
        m = Numbers.parse_int(tmp[0])
        s = Numbers.parse_int(tmp[1])
        
        return (m, s)
    
    @classmethod
    def to_hours(cls, h=0, m=0, s=0):
        """
        Converts h,m,s sexagesimal values to decimal hours
        """
        
        return h + m/60.0 + s/3600.0 

    @classmethod
    def to_minutes(cls, h=0, m=0, s=0):
        """
        Converts h,m,s sexagesimal values to decimal minutes
        """
        
        return h*60.0 + m + s/60.0 

    @classmethod
    def to_seconds(cls, h=0, m=0, s=0):
        """
        Converts h,m,s sexagesimal values to decimal seconds
        """
        
        return h*3600.0 + m*60.0 + s 
