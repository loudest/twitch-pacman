import twitter, json, memcache
from threading import Thread

class twitter_bot():

	def __init__(self):
		#Thread.__init__(self)
		self.r = memcache.Client(['twitch-plays-pacman.yjvmq8.cfg.usw2.cache.amazonaws.com:11211'], debug=0)

	def searchTweets(self, query):
		consumer_key = 'ugD4ZKV6GxeLJuiHyosw'
		consumer_secret = 'D89yuzda0mlpYCnOMPG1NK9koWnw0ksOWI6UL4zM'
		access_token = '2356976360-D8LrSAJ46ZsrCtvS34jFFDbm8GfqdUB4EvhUy4o'
		access_token_secret = 'fpuWA5O53hNHtYF4jgIvJ4uEugwOOcWEAVSEaIuwkztLb'
		api = twitter.Api(	consumer_key, consumer_secret, access_token, access_token_secret)
		statuses = api.GetSearch(query)

		for status in statuses:
			id = str(status.GetId())
			user = status.GetUser()
			text = status.GetText()
			value = self.r.get(id);
			print "id: ".value."\n"
			if(value is None): 
				print "Storing @%s: %s" % (user.GetScreenName(), text)
				self.r.set(id,'a')
			else:
				print "Stored: @%s: %s" % (user.GetScreenName(), text)

t = twitter_bot()
t.searchTweets('#twitchispacman')