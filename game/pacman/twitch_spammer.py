import twitter, json, redis, time, sys, socket, string, random, math, fileinput
from threading import Thread

IDENT = 'pacman'
REAL_NAME = 'Twitch plays pacman'
CHANNEL_ONE = '#twitchispacman'
CHANNEL_TWO = 'twitchisblinky'
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

				num = random.sample([1, 2, 3, 4],  1)[0]
				command = 'down'
				if(num == 1):
					command = 'right'
				elif(num == 2):
					command = 'left'
				elif(num == 3):
					command = 'up'

				irc.send('PRIVMSG %s :%s\r\n' % (CHANNEL_ONE, command))

				num = random.sample([1, 2, 3, 4],  1)[0]
				command = 'down'
				if(num == 1):
					command = 'right'
				elif(num == 2):
					command = 'left'
				elif(num == 3):
					command = 'up'

				irc.send('PRIVMSG %s :%s\r\n' % (CHANNEL_TWO, command))

			except Exception, e:
				continue
			
			time.sleep(10)

	def run(self):
		self.connect()

	def stop_running(self):
		self.running = False
		print "Twitch Bot set to shutdown"


def loader():

	threads = []
	t1 = twitch_bot('blinky1005', '4pbfhq3ltswg8psjeq9i53xfd7a9tjl')
	threads.append(t1)
	t1.start()
	t2 = twitch_bot('blinky1004', 'a7mr3xi912jmf72zhct3afe5ra3d797')
	threads.append(t2)
	t2.start()
	t3 = twitch_bot('blinky1006', 'phkboj8njrdz3x7mthb3krm6bz3rpus')
	threads.append(t3)
	t3.start()

loader()


