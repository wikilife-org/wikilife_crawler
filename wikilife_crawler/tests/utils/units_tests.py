# coding=utf-8
import unittest
from wikilife_crawler.utils.units import Units

class UnitsTests(unittest.TestCase):
    
    MILES_KM = 1.609344
    LB_KG = 0.45359237
        
    def test_miles_to_km(self):
        assert Units.miles_to_km(100) == 160.9344

    def test_lb_to_kg(self):
        assert Units.lb_to_kg(100) == 45.359237

    def test_to_km(self):
        assert Units.to_km(100, "km") == 100.0
        assert Units.to_km(100, "mi") == 160.9344

    def test_to_kg(self):
        assert Units.to_kg(100, "kg") == 100.0
        assert Units.to_kg(100, "lb") == 45.359237
