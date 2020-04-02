#!/usr/bin/env python3
"""
        proxy.py - TCP server that serves as an upstream data filter
        for the UDP server in server.py
        Author: Quang Tran (quangtran@bennington.edu)
        Date: 4/2/2020

        Comment: After trying my best to try to find a way to mitigate
        this at the server level, I have come to the realization that
        this is not possible on UDP, since UDP is simply a datagram transport
        protocol - it cannot read connection header
        The comment that explained it for me:
            https://security.stackexchange.com/questions/91548/how-to-mitigate-udp-flood-attacks
        This file is an attempt at simulating an upstream proxy service that helps
        deal with incoming connection for the upstream server
"""

import socket

TCP_ADDRESS = '0.0.0.0' #listening to all ips
TCP_PORT = 9000
BUFFER_SIZE = 1024

#create a socket using TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket to the given address/port
sock.bind((TCP_ADDRESS, TCP_PORT))
