import twitter, json, redis, time, sys, socket, string, random, math, fileinput
from threading import Thread

class twitch_bot():

	def __init__(self, user, password):

		self.running = True
		self.user = user
		self.password = password
		self.ident = "pacman"
		self.real_name = "Twitch plays pacman"
		self.CHANNEL_ONE = '#twitchispacman'
		self.CHANNEL_TWO = 'twitchisblinky'
		self.HOST = "irc.twitch.tv"
		self.PORT = 6667

	def connect(self):

		readbuffer = ""
		irc=socket.socket()
		# Set a timeout of two seconds
		irc.settimeout(2)
		irc.connect((self.HOST, self.PORT))
		irc.send("PASS oauth:%s\r\n" % (self.password))
		irc.send("NICK %s\r\n" % (self.nick))
		irc.send("USER %s %s :%s\r\n" % (self.ident, self.indent, self.real_name))
		irc.send("JOIN %s\r\n" % (self.CHANNEL_ONE))
		irc.send("JOIN %s\r\n" % (self.CHANNEL_TWO))

      	while self.running:
    		try:
           		data = irc.recv(1024)

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

        		irc.send('PRIVMSG %s :%s\r\n' % (self.CHANNEL_ONE, command))

        		num = random.sample([1, 2, 3, 4],  1)[0]
        		command = 'down'
        		if(num == 1):
        			command = 'right'
        		elif(num == 2):
        			command = 'left'
        		elif(num == 3):
        			command = 'up'

    			irc.send('PRIVMSG %s :%s\r\n' % (self.CHANNEL_TWO, command))

    		except Exception, e:
				continue
			
		time.sleep(10)

	def run(self):
		self.connect()

	def stop_running(self):
		self.running = False
		print "Twitch Bot set to shutdown"


def loader():

	threads = array()
	('blinky1005', '4pbfhq3ltswg8psjeq9i53xfd7a9tjl')
	('blinky1004', 'a7mr3xi912jmf72zhct3afe5ra3d797')
	('blinky1006', 'phkboj8njrdz3x7mthb3krm6bz3rpus')


