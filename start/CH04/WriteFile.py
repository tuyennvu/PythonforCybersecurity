#!/usr/bin/env python3
# Sample script that writes to a file
# By TUYEN VU 01/28/2022

#open file for writing
hackme_file = open("hackme.txt", "w")

#write to the file
hackme_file.write("What is your name?\n")
hackme_file.write("What is your farvorite color?\n")
hackme_file.write("What was your frist pet's name?\n")
hackme_file.write("What is you rmother's maiden name?\n")
hackme_file.write("What elementary school did you attend?\n")

#close file
hackme_file.close()

