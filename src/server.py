#!/usr/bin/env python3

"""
	server.py - UDP server that listens on UDP port 9000
	Author: Zak Ziiaidin (zalkar@bennington.edu)
	Date: 3/30/2020
"""

import socket
import sys
import iptc
import time

MAX_PACKET_LIMIT = 10
MAX_TIME_INTERVAL = 20

# listening to any IP
UDP_ADDRESS = '0.0.0.0'

# UDP client
#UDP_CLIENT = sys.argv[1]

# exposing port:9000
UDP_PORT = 9000

# create a socket -DGRAM == UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind our socker to the given address/port
sock.bind((UDP_ADDRESS, UDP_PORT))

# actually implementing a rate limiting algorithm that allows for retroactive
# removal from firewall is too hard so i'll just ban them all
#   key: ip addr
#   value: [packets sent in last MAX_TIME_INTERVAL, time last checked]
ip_limit = {}

#list of all blacklisted ips
ip_blacklist = set()

# always listen
while 1:
    """
    Token Bucket Rate Limiting Algorithm
        https://stackoverflow.com/questions/667508/whats-a-good-rate-limiting-algorithm
        http://www.iasptk.com/block-unwanted-ip-addresses-linux-ubuntu/
    """
    data, addr = sock.recvfrom(1024) # 1024-byte buffer size

    now = time.time()
    ip_addr = addr[0]

    if ip_addr not in ip_limit:
        ip_limit[ip_addr] = [MAX_PACKET_LIMIT, now]
    else:
        #calculate allowed packet send value
        time_diff = now - ip_limit[ip_addr][1] #now - last checked
        ip_limit[ip_addr][0] += MAX_PACKET_LIMIT / MAX_TIME_INTERVAL * time_diff
        if ip_limit[ip_addr][0] > MAX_PACKET_LIMIT:
            ip_limit[ip_addr][0] = MAX_PACKET_LIMIT

        #assign last checked time
        ip_limit[ip_addr][1] = now

    #deprecating packet sent
    ip_limit[ip_addr][0] -= 1
    time.sleep(0.1)
    #the sleep here is so that the logic below could be completed
    #if not then the api would spam iptables would 84 new rules
    if ip_limit[ip_addr][0] < 1.0:
        if ip_addr not in ip_blacklist:
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
            rule = iptc.Rule()
            rule.src = ip_addr
            rule.target = iptc.Target(rule, "DROP")
            chain.insert_rule(rule)

            ip_blacklist.add(ip_addr)
            print("Blacklisted: {}".format(ip_addr))


    #if (addr[0] == UDP_CLIENT):
    print("{0} received: {1}".format(ip_addr, data))

    # sending the same data back
    sock.sendto(data, addr)
