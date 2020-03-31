#!/usr/bin/python3
"""
	main.py - Python script to send health info of CATLab instance to a remote server 
	Author: Zak Ziiaidin (zalkar@bennington.edu)
	Date: 3/14/2020
"""

import psutil
import time

while True:

	# getting cpu_usage_percent
	cpu_usage_percent = psutil.cpu_percent(interval = 1)
	print(cpu_usage_percent)
	
	time.sleep(5)
