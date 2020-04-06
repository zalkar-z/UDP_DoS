#!/usr/bin/python3
"""
	get_cpu.py - prints local CPU usage every five seconds
	Author: Zak Ziiaidin (zalkar@bennington.edu)
	Date: 3/30/2020
"""

import psutil
import time

while True:

	# getting cpu_usage_percent
	cpu_usage_percent = psutil.cpu_percent(interval = 1)
	print(cpu_usage_percent)
	
	time.sleep(5)
