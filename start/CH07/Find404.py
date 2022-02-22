#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Tuyen Vu

import os
#get current location/directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#promting for file 
file_name = input("What file do you want to review?")
#open file
f = open(os.path.join(__location__, file_name), "r")
#read file line by line
while True: 
    line = f.readline()
    if not line:
        break
    #if there is a 404, print it 
    if "404" in line:
        print(line.strip())
        
#close file
f.close()