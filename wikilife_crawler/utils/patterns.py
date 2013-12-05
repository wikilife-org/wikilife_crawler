# coding=utf-8

""" 
Common patterns 
"""
import re

NATURAL_PATTERN = '(\d+|\d+.\d+|\d+,\d+)'
"""
unit 1  
thousand latin 1.000
thousand english 1,000
"""

REAL_PATTERN = '(\d+|\d+.\d+|\d+,\d+|\d+.\d+,\d+|\d+,\d+.\d+)'
"""
unit int 1  
unit float latin 1,0  
unit float english 1.0  
thousand int latin 1.000
thousand int english 1,000
thousand float latin 1.000,0
thousand float english 1,000.0
"""

TIME_PATTERN = '(\d+:\d+:\d+|\d+:\d+)'
"""
0:0
0:00
00:0
00:00
...
00:00:00
"""

MINUTES_UNIT_PATTERN = '(min|minutes)'

TIME_PATTERN_DESCRIPTIVE = '(\d+h \d+m \d+s|\d+h \d+m|\d+m \d+s|\d+h|\d+m|\d+s)'
"""
0h
0m
0s
0h 0m
0m 0s
0h 0m 0s
"""

KM_UNIT_PATTERN = '(km|kilometers)'
KM_UNIT_PATTERN_C = re.compile(KM_UNIT_PATTERN, re.IGNORECASE)

MILE_UNIT_PATTERN = '(mi|miles)'
MILE_UNIT_PATTERN_C = re.compile(MILE_UNIT_PATTERN, re.IGNORECASE)

#DISTANCE_UNITS_PATTERN =  '(' + KM_UNIT_PATTERN + '|' + MILE_UNIT_PATTERN + ')'
DISTANCE_UNITS_PATTERN = '(km|kilometers|mi|miles)'


KG_UNIT_PATTERN = '(kg)' 
KG_UNIT_PATTERN_C = re.compile(KG_UNIT_PATTERN, re.IGNORECASE)

LB_UNIT_PATTERN = '(lb)' 
LB_UNIT_PATTERN_C = re.compile(LB_UNIT_PATTERN, re.IGNORECASE)

WEIGHT_UNITS_PATTERN =  '(kg|lb)'

