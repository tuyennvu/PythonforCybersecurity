#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Tuyen Vu  02/05/2022

# promt for message
start_message = input("What is the message to encrypt/decrypt? ")
start_message = start_message.lower()
end_message = ""

# loop each letter
for letter in start_message: 
    # convert to ASCII number
    ascii_num = ord(letter)

    # check if it is a letter
    if ascii_num >= 97 and ascii_num <= 122:

        # Add 13
        ascii_num = ascii_num + 13
        # check if past "z"
        if ascii_num > 122:
            ascii_num -= 26
        # convert to ASCII character
        end_message += chr(ascii_num)

# print out results
print(end_message)
