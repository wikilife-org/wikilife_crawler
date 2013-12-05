# coding=utf-8
import unittest
import re
from wikilife_crawler.utils import patterns

class PatternsTests(unittest.TestCase):
    
    def test_natural_pattern(self):
        cp = re.compile(patterns.NATURAL_PATTERN)
        
        assert re.match(cp, "1")
        assert re.match(cp, "1.0000")
        assert re.match(cp, "1,0000")
        assert not re.match(cp, "abc")

    def test_real_pattern(self):
        cp = re.compile(patterns.REAL_PATTERN)
        
        assert re.match(cp, "1")
        assert re.match(cp, "1.0000")
        assert re.match(cp, "1,0000")
        assert re.match(cp, "1,0")
        assert re.match(cp, "1.0")
        assert re.match(cp, "1.0000,0")
        assert re.match(cp, "1,0000.0")
        assert not re.match(cp, "abc")
        
    def test_time_pattern(self):
        cp = re.compile(patterns.TIME_PATTERN)
        
        assert re.match(cp, "0:0")
        assert re.match(cp, "0:00")
        assert re.match(cp, "00:0")
        assert re.match(cp, "00:00")
        assert re.match(cp, "00:00:00")
        assert not re.match(cp, "0")

    def test_minutes_unit_pattern(self):
        cp = re.compile(patterns.MINUTES_UNIT_PATTERN)
        
        assert re.match(cp, "min")
        assert re.match(cp, "minutes")
        assert not re.match(cp, " min")
        assert not re.match(cp, " minutes")
        assert not re.match(cp, "hours")
        assert not re.match(cp, "seconds")

    def test_time_pattern_descriptive(self):
        cp = re.compile(patterns.TIME_PATTERN_DESCRIPTIVE)
  
        assert re.match(cp, "0h")
        assert re.match(cp, "0m")
        assert re.match(cp, "0s")
        assert re.match(cp, "00h")
        assert re.match(cp, "00m")
        assert re.match(cp, "00s")
        assert re.match(cp, "0m 0s")
        assert re.match(cp, "00m 00s")
        assert re.match(cp, "0h 0m")
        assert re.match(cp, "00h 00m")
        assert re.match(cp, "0h 0m 0s")
        assert re.match(cp, "00h 00m 00s")
        assert not re.match(cp, "0")
        
    def test_km_unit_pattern(self):
        cp = re.compile(patterns.KM_UNIT_PATTERN)
        
        assert re.match(cp, "km")
        assert not re.match(cp, "abc")
        assert not re.match(cp, "0")
        
    def test_mile_unit_pattern(self):
        cp = re.compile(patterns.MILE_UNIT_PATTERN)
        
        assert re.match(cp, "mi")
        assert re.match(cp, "miles")
        assert not re.match(cp, "abc")
        assert not re.match(cp, "0")
        
    def test_distance_units_pattern(self):
        cp = re.compile(patterns.DISTANCE_UNITS_PATTERN)
        
        assert re.match(cp, "km")
        assert re.match(cp, "mi")
        assert re.match(cp, "miles")
        assert not re.match(cp, "abc")
        assert not re.match(cp, "0")
    
    def test_kg_unit_pattern(self):
        cp = re.compile(patterns.KG_UNIT_PATTERN)
        
        assert re.match(cp, "kg")
        assert not re.match(cp, "abc")
        assert not re.match(cp, "0")
        
    def test_lb_unit_pattern(self):
        cp = re.compile(patterns.LB_UNIT_PATTERN)
        
        assert re.match(cp, "lb")
        assert not re.match(cp, "abc")
        assert not re.match(cp, "0")
        
    def test_weight_units_pattern(self):
        cp = re.compile(patterns.WEIGHT_UNITS_PATTERN)
        
        assert re.match(cp, "kg")
        assert re.match(cp, "lb")
        assert not re.match(cp, "abc")
        assert not re.match(cp, "0")
