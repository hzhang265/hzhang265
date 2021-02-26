#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_hzhang265.py 
Author: "Matthew Zhang"
The python code in this file (a1_hzhang265.py) is original work written by
"Matthew Zhang". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    '''
    This function will evenly divide the year by 4, 400, if any of the results were true, it further checks if the year can be divided by 100. If not divisible by 100,
    it is a leap year.
    '''
    year = int(obj)
    return (year % 4 == 0 or year % 400 == 0) and (year % 100 != 0)


def sanitize(obj1,obj2):
    '''
    Take user raw data and convert them into integer-only format.
    obj2 is the allowed data, obj1 is the raw data.
    '''
    results = ''
    formatted = obj1.replace('/', '').replace('-', '').replace('.', '')
    for char in formatted:
        if char in obj2:
            results += char
    return results

def size_check(obj, intobj):
    '''
    Takes two arguments: 1st the sanitized data, 2nd an int obj to check the length of input number string. Returns boolean.
    '''
    status = None
    if len(obj) == intobj:
        status = True
    else:
        status = False
    return status

def range_check(obj1, obj2):
    '''
    Takes 2 arguments, first the sanitized data, second a tuple that checks the range of obj1. Returns boolean.
    '''
    status = None
    if obj1 >= obj2[0] and obj1 <= obj2[1]:
        status = True
    else:
        status = False
    
    return status
    
def usage():    
    '''
    Print error message when there is no 2 system argument.
    '''
    status = 'Usage: a1_hzhang265.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD'
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)  
