#!/usr/bin/env python3
# Sample script that reads from a file
# By Tuyen Vu




hackme_file = open("hackme.txt", "r")
file_contents = hackme_file.read()
hackme_file.close()
print(file_contents)
print("Here is someone to hack - information")

