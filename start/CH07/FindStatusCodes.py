#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By 

import os
import re
#get current location/directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#promting for file 
file_name = input("What file do you want to review?")
#open file
f = open(os.path.join(__location__, file_name), "r")
#read file contents
access_log = f.readlines()


        
#close file
f.close()


#setup regex pattern
status_code_pattern = r'\s(\d{3})\s'
#create status code dictionary 
status_code_dict = {}
#parse log line by line
for line in access_log:
    #regex search
    m= re.search( status_code_pattern, line)
    if m:
        #print out match 
        status_code = m.group()
        #if status code is in dictionary, then increment
        if status_code in status_code_dict:
            status_code_dict[status_code] +=1
        #otherwiseee, add status code to dictionary
        else:
            status_code_dict[status_code] = 1

print(status_code_dict)


#Sort by most frequently accessed