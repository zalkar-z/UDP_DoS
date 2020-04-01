#!/usr/bin/env python3

"""
	server.py - UDP server that listens on UDP port 9000
	Author: Zak Ziiaidin (zalkar@bennington.edu)
	Date: 3/30/2020
"""

import socket
import sys

# listening to any IP
UDP_ADDRESS = '0.0.0.0'

# UDP client
UDP_CLIENT = sys.argv[1]

# exposing port:9000
UDP_PORT = 9000

# create a socket -DGRAM == UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind our socker to the given address/port
sock.bind((UDP_ADDRESS, UDP_PORT))

# always listen
while 1:
    data, addr = sock.recvfrom(1024) # 1024-byte buffer size
    if (addr[0] == UDP_CLIENT):
        print("{0} received: {1}".format(addr[0], data))

        # sending the same data back
        sock.sendto(data, addr)
