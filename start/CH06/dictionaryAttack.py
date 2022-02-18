#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Tuyen vu 


#import library 
import crypt

#ask user for hashtype and salt
hash_and_salt = "$6$2GNslvs9eZPMAu6c$"
#ask user for entire hash
full_hash ="$6$2GNslvs9eZPMAu6c$EPthEfw.41gVx5ITGpI54EyEMjfuxNhrdJwnWyHpNyd8U50vWawnDPEEbzUsKdwtz2Ta9HQc9bOJ6on4oUFP8."
#open top10.txt
f = open("start/CH06/top10.txt","r")
guesses = f.readlines()
f.close()
#loop for each line in dictionary file 
for guess in guesses:
    guess = guess.strip()
    print(guess)
    # hash passwd guess with provide salt
    #compare results to full hash 
    #iff match, say so and quit 
