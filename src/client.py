#!/usr/bin/env python3

"""
	client.py - UDP client that talks to a remote server on UDP PORT 9000 and sends a simple message and measure its perfomance
	Author: Zak Ziiaidin (zalkar@bennington.edu)
	Date: 3/30/2020
"""

import socket
import time
import sys

# server IP
UDP_ADDRESS = sys.argv[1]

# exposing port:9000
UDP_PORT = 9000

# generating dummy bytes to overload server's capacity fast
MESSAGE = "hello" 

# create a socket -DGRAM == UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set timeout
sock.settimeout(5)

while 1:
    # start timer
    start = time.time()

    # send out message to the server - no connect/close needed!
    sock.sendto(MESSAGE.encode(), (UDP_ADDRESS, UDP_PORT))

    # receiving some updated data
    data, addr = sock.recvfrom(1024) # 1024-byte buffer size

    # print received data
    print("{0} received: {1}".format(addr[0], data))
    
    # print elapsed time
    print("Time elapsed in seconds: ", time.time() - start)

    # wait five seconds and repeat
    time.sleep(5)