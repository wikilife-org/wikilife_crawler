# coding=utf-8
import unittest
from wikilife_crawler.utils.numbers import Numbers

class NumbersTests(unittest.TestCase):
    
    def test_parse_int(self):
        
        str_value = "1"
        int_value = Numbers.parse_int(str_value)
        assert int_value == 1 
        
        str_value = "0"
        int_value = Numbers.parse_int(str_value)
        assert int_value == 0
         
        str_value = "-1"
        int_value = Numbers.parse_int(str_value)
        assert int_value == -1 
        
        #One thousand latin
        str_value = "1.000"
        int_value = Numbers.parse_int(str_value)
        assert int_value == 1000 
        
        #One thousand english
        str_value = "1,000"
        int_value = Numbers.parse_int(str_value)
        assert int_value == 1000
         
    def test_parse_float(self):
        
        #float english
        
        str_value = "1.0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 1.0 
        
        str_value = "0.0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 0.0
         
        str_value = "-1.0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == -1.0 
        
        str_value = "2.5"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 2.5
         
        str_value = "1.005"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 1.005 
        
        
        #float latin
        
        str_value = "1,0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 1.0 
        
        str_value = "0,0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 0.0
         
        str_value = "-1,0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == -1.0 
        
        str_value = "2,5"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 2.5 
        
        str_value = "1,005"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 1.005 
        
        
        #thousands english
        
        str_value = "1,000.0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 1000.0
        
        str_value = "4,000.5"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 4000.5
        
        
        #thousands latin
        
        str_value = "1.000,0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 1000.0
        
        str_value = "4.000,5"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 4000.5
        
        
        str_value = "1"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 1.0 
        
        str_value = "0"
        float_value = Numbers.parse_float(str_value)
        assert float_value == 0.0
         
        str_value = "-1"
        float_value = Numbers.parse_float(str_value)
        assert float_value == -1.0 
        
        
