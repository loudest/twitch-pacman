import twitter, json, redis, time
from threading import Thread

# FIXME: Share this properly
def enum(**enums):
    return type('Enum', (), enums)

# Movement Directions
Directions = enum(RIGHT=1, LEFT=2, UP=3, DOWN=4)

class twitter_bot(Thread):

	def __init__(self, players, level):
		Thread.__init__(self)
		self.r = redis.StrictRedis(host='redis.snorting.co.ke', port=6379, db=0)
		self.running = True
		self.players = players
		self.level = level
		self.consumer_key = 'ugD4ZKV6GxeLJuiHyosw'
		self.consumer_secret = 'D89yuzda0mlpYCnOMPG1NK9koWnw0ksOWI6UL4zM'
		self.access_token = '2356976360-D8LrSAJ46ZsrCtvS34jFFDbm8GfqdUB4EvhUy4o'
		self.access_token_secret = 'fpuWA5O53hNHtYF4jgIvJ4uEugwOOcWEAVSEaIuwkztLb'


	def searchTweets(self):

		api = twitter.Api(	self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)

      	while self.running:
        	try:
				pacman = api.GetSearch('#twitchispacman')
				for status in pacman:
					id = str(status.GetId())
					user = status.GetUser()
					text = status.GetText()
					value = self.r.get(id);
					data = text.lower()
					if(value is None): 
						#print "Storing @%s: %s" % (user.GetScreenName(), text)
						self.r.set(id,'a')
						if(data.find ('right') != -1):
						 self.players[0].QueueMove(Directions.RIGHT, self.level)
						elif(data.find('left') != -1):
						 self.players[0].QueueMove(Directions.LEFT, self.level)
						elif(data.find('up') != -1):
						 self.players[0].QueueMove(Directions.UP, self.level)
						elif(data.find('down') != -1):
						 self.players[0].QueueMove(Directions.DOWN, self.level)

				blinky = api.GetSearch('#twitchisblinky')
				for status in pacman:
					id = str(status.GetId())
					user = status.GetUser()
					text = status.GetText()
					value = self.r.get(id);
					data = text.lower()
					if(value is None): 
						#print "Storing @%s: %s" % (user.GetScreenName(), text)
						self.r.set(id,'a')
						if(data.find ('right') != -1):
						 self.players[1].QueueMove(Directions.RIGHT, self.level)
						elif(data.find('left') != -1):
						 self.players[1].QueueMove(Directions.LEFT, self.level)
						elif(data.find('up') != -1):
						 self.players[1].QueueMove(Directions.UP, self.level)
						elif(data.find('down') != -1):
						 self.players[1].QueueMove(Directions.DOWN, self.level)

				time.sleep(15)

			except Exception, e:

				self.running = False
				break;

	def run(self):
	  self.searchTweets()

	def stop_running(self):
	  self.running = False
	  print "Twitch Bot set to shutdown"


t = twitter_bot()
t.searchTweets('#twitchispacman')
t.searchTweets('#twitchisblinky') 	