#!/usr/bin/env python3

"""
	client.py - UDP client that talks to a remote server on UDP PORT 9000 and sends a simple message
	Author: Zak Ziiaidin (zalkar@bennington.edu)
	Date: 3/3/2020
"""

import socket
import sys

# UDP_ADDRESS = '10.10.117.73'
UDP_ADDRESS = '127.0.0.1'
UDP_PORT = 9000
MESSAGE = sys.argv[1]
# MESSAGE = "hello"

# create a socket -DGRAM == UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set timeout
sock.settimeout(5)

# send out message to the server - no connect/close needed!
sock.sendto(MESSAGE.encode(), (UDP_ADDRESS, UDP_PORT))
print("Sent message: '{0}' to {1}".format(MESSAGE, UDP_ADDRESS))

# receiving some updated data
data, addr = sock.recvfrom(1024) # 1024-byte buffer size
data = data.decode()
print("{0} received: {1}".format(addr[0], data))