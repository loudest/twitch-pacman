#! /usr/bin/python 

import time
import datetime

deadline = datetime.datetime(2014, 2, 28, 20, 00, 00, 00000)

while(deadline>datetime.datetime.now()):
	currentremaining = deadline - datetime.datetime.now()
	days_remaining = currentremaining.days
	seconds_remaining = currentremaining.seconds
	hours_remaining = seconds_remaining//3600
	seconds_remaining = seconds_remaining - hours_remaining*3600
	minutes_remaining = seconds_remaining//60
	seconds_remaining = seconds_remaining - minutes_remaining*60
	
	f = open('time_countdown.txt','w')
	f.write('%02dd %02dh %02dm %02ds' % (days_remaining,hours_remaining,minutes_remaining,seconds_remaining))
	f.close()
	time.sleep(.1)