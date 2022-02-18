#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Tuyen vu 


#import library 
import crypt
from unittest import result

def test_password(hash_and_salt, full_hash, guess):
    hashed_guess = crypt.crypt(guess, hash_and_salt)
    #compare results to full hash
    if hashed_guess == full_hash:
        #if match, say so and quit
        return True
    return False

#ask user for entire hash
#full_hash = "$6$2GNslvs9eZPMAu6c$EPthEfw.41gVx5ITGpI54EyEMjfuxNhrdJwnWyHpNyd8U50vWawnDPEEbzUsKdwtz2Ta9HQc9bOJ6on4oUFP8."
full_hash = input("What hash do you want to crack? ")
#separate hashtype and salt from hash
pieces = full_hash.split("$")
hash_and_salt = "$" + pieces[1]+ "$" + pieces[2] + "$"
#open top10.txt
f = open("start/CH06/top10.txt","r")
guesses = f.readlines()
f.close()
#loop for each line in dictionary file 
for guess in guesses:
    guess = guess.strip()
    #print(guess)
    # hash passwd guess with provide salt
    result = test_password(hash_and_salt, full_hash, guess)
    if result:
        print("Password found: '{0}'". format(guess))
        break