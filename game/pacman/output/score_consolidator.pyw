#! /usr/bin/python

import time

while(True):
	blinky_score = 0
	pacman_score = 0
	
	f = open('ghost_score.txt','r')
	blinky_wins = int(f.readline().strip())
	f.close()
	
	f = open('pacman_score.txt','r')
	pacman_wins = int(f.readline().strip())
	f.close()
	
	rounds = pacman_wins + blinky_wins + 1
	f = open('round_counter.txt','w')
	f.write(str(rounds))
	f.close()
	
	f = open('blinky_current_contributions.txt','r')
	blink = f.readline().strip()
	blink = blink[1:]
	print blink# = float(blink)
	blinker = float(blink)
	blinky_donation = 0
	while(blinker>100):
		blinky_donation = blinky_donation + 1
		blinker = blinker - 100
	#print blinky_donation
	f.close()
	
	f = open('pacman_current_contributions.txt','r')
	pac = f.readline().strip()
	pac = pac[1:]
	print pac
	pacer = float(pac)
	pacman_donation = 0
	while(pacer>100):
		pacman_donation = pacman_donation + 1
		pacer = pacer - 100
	#pacman_donation = float(pac)
	
	#print pac_donation
	f.close()
	
	pacman_score = pacman_wins + (pacman_donation)*2
	
	blinky_score = blinky_wins + (blinky_donation)*2
	
	f = open('pacman_total_score.txt','w')
	f.write(str(pacman_score))
	f.close()
	
	f = open('blinky_total_score.txt','w')
	f.write(str(blinky_score))
	f.close()
	
	time.sleep(.5)