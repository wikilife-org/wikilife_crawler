# coding=utf-8
import unittest
from wikilife_crawler.utils.times import Times

class TimesTests(unittest.TestCase):
    
    def test_parse_h_m_s(self):
        str_value = "15:30:45"
        h, m, s = Times.parse_h_m_s(str_value)
        assert h == 15 
        assert m == 30 
        assert s == 45 
    
    def test_parse_h_m_s_hhmm(self):
        str_value = "15:30"
        h, m, s = Times.parse_h_m_s(str_value, ":", True)
        assert h == 15 
        assert m == 30 
        assert s == 0 
    
    def test_parse_h_m_s_mmss(self):
        str_value = "30:45"
        h, m, s = Times.parse_h_m_s(str_value, ":", False)
        assert h == 0 
        assert m == 30 
        assert s == 45 
    
    def test_parse_h_m_s_hh(self):
        str_value = "15"
        h, m, s = Times.parse_h_m_s(str_value, ":", True)
        assert h == 15 
        assert m == 0 
        assert s == 0 
    
    def test_parse_h_m_s_ss(self):
        str_value = "45"
        h, m, s = Times.parse_h_m_s(str_value, ":", False)
        assert h == 0 
        assert m == 0 
        assert s == 45
    
    def test_parse_h_m(self):
        str_value = "15:30"
        hms = Times.parse_h_m(str_value)
        assert hms[0] == 15 
        assert hms[1] == 30 

    def test_parse_m_s(self):
        str_value = "30:45"
        hms = Times.parse_m_s(str_value)
        assert hms[0] == 30 
        assert hms[1] == 45 

    def test_to_hours(self):
        assert Times.to_hours(1, 15, 30) == 1.25 + 30.0/3600.0 

    def test_to_minutes(self):
        assert Times.to_minutes(1, 15, 30) == 75.5 

    def test_to_seconds(self):
        assert Times.to_seconds(1, 15, 30) == 4530.0 

    def test_parse_hours(self):
        str_value = "1:15:30"
        hours = Times.parse_hours(str_value)
        assert hours == 1.25 + 30.0/3600.0 

    def test_parse_minutes(self):
        str_value = "1:15:30"
        minutes = Times.parse_minutes(str_value)
        assert minutes == 75.5 

    def test_parse_seconds(self):
        str_value = "1:15:30"
        seconds = Times.parse_seconds(str_value)
        assert seconds == 4530.0 

    def test_parse_time(self):
        assert Times.parse_time("1", Times.HOUR, Times.HOUR) == 1.0
        assert Times.parse_time("1", Times.HOUR, Times.MINUTE) == 60.0
        assert Times.parse_time("1", Times.HOUR, Times.SECOND) == 3600.0
        assert Times.parse_time("45", Times.MINUTE, Times.HOUR) == 0.75
        assert Times.parse_time("30", Times.SECOND, Times.MINUTE) == 0.5
        assert Times.parse_time("90", Times.SECOND, Times.HOUR) == 0.025

