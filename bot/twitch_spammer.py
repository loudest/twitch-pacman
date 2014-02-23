import json, time, sys, socket, string, random, math, fileinput
from threading import Thread

IDENT = 'pacman'
REAL_NAME = 'Twitch plays pacman'
CHANNEL_ONE = '#twitchispacman'
CHANNEL_TWO = '#twitchisblinky'
HOST = 'irc.twitch.tv'
PORT = 6667

class twitch_bot(Thread):

	def __init__(self, user, password):
		Thread.__init__(self)
		self.running = True
		self.user = user
		self.password = password

	def connect(self):

		readbuffer = ""
		irc=socket.socket()
		# Set a timeout of two seconds
		irc.settimeout(2)
		irc.connect((HOST, PORT))
		irc.send("PASS oauth:%s\r\n" % (self.password))
		irc.send("NICK %s\r\n" % (self.user))
		irc.send("USER %s %s :%s\r\n" % (IDENT, IDENT, REAL_NAME))
		irc.send("JOIN %s\r\n" % (CHANNEL_ONE))
		irc.send("JOIN %s\r\n" % (CHANNEL_TWO))

		while self.running:
			try:
				data = irc.recv(1024)
				print data

				if(data.find('PING') != -1):
					irc.send('PONG '+data.split()[ 1 ]+'\r\n')

				#randomization
				who = random.sample([1,2],1)[0]

				#pac-man
				if(who == 1):
					num = random.sample([1, 2, 3, 4], 1)[0]
					command = 'down'
					if(num == 1):
						command = 'right'
					elif(num == 2):
						command = 'left'
					elif(num == 3):
						command = 'up'

					#print ("SENDING PACMAN %s\n" % command)
					irc.send('PRIVMSG %s :%s\r\n' % (CHANNEL_ONE, command))
					time.sleep(15)

				#blinky
				else:
					num = random.sample([1, 2, 3, 4], 1)[0]
					command = 'down'
					if(num == 1):
						command = 'right'
					elif(num == 2):
						command = 'left'
					elif(num == 3):
						command = 'up'

					#print ("SENDING BLINKY %s\n" % command)
					irc.send('PRIVMSG %s :%s\r\n' % (CHANNEL_TWO, command))
					time.sleep(15)

			except Exception, e:
				continue
			

	def run(self):
		self.connect()

	def stop_running(self):
		self.running = False
		print "Twitch Bot set to shutdown"


def loader():

	threads = []
	f = open('logins.txt', 'r')
	for line in f:
		temp = line.split(':')
		login = temp[0]
		password = temp[1]
		t = twitch_bot(login, password)
		threads.append(t)
		t.start()

loader()


