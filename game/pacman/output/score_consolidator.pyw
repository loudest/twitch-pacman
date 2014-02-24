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
	
	rounds = pacman_wins + blinky_wins
	f = open('round_counter.txt','w')
	f.write(str(rounds))
	f.close()
	
	f = open('blinky_current_contributions.txt','r')
	blinky_donation = int(f.readline().strip())
	f.close()
	
	f = open('pacman_current_contributions.txt','r')
	pacman_donation = int(f.readline().strip())
	f.close()
	
	pacman_score = pacman_wins + (pacman_donation//100)*2
	
	blinky_score = blinky_wins + (blinky_donation//100)*2
	
	f = open('pacman_total_score.txt','w')
	f.write(str(pacman_score))
	f.close()
	
	f = open('blinky_total_score.txt','w')
	f.write(str(blinky_score))
	f.close()
	
	time.sleep(.5)