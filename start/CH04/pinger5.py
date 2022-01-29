#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By TUYEN VU 01/28/2022


import platform
import os
from datetime import datetime

def write_log(message):
    now =str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    f = open(script_folder[0] + "/pinger.log", "a")
    f.write(message)
    f.close()


for octet in range(254):
    # Assign IP address
    ip = "192.168.0.{0}".format(octet +1)
    # Call function
    exit_code = ping_address(ip)

    if exit_code == 0:
        write_log("{0} is online".format(ip))
        print("{0} is online".format(ip))
    else:
        write_log("{0} is offline".format(ip))