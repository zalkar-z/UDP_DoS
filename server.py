#!/usr/bin/env python3

"""
	server.py - UDP server that listens on UDP port 9000 and prints what was sent to it.
	Author: Zak Ziiaidin (zalkar@bennington.edu)
	Date: 3/3/2020
"""

import socket

UDP_ADDRESS = '0.0.0.0'
# UDP_ADDRESS = '127.0.0.1'
UDP_PORT = 9000
# MESSAGE = sys.argv[1]

# create a socket -DGRAM == UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind our socker to the given address/port
sock.bind((UDP_ADDRESS, UDP_PORT))

# my fancy server logic
while 1:
    data, addr = sock.recvfrom(1024) # 1024-byte buffer size
    print("{0} received: {1}".format(addr[0], data))

    # sending updated data back
    sock.sendto(data, addr)
