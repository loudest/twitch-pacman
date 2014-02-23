import twitter, json

class twitter_bot():

	def searchTweets(self, query):
		consumer_key = 'ugD4ZKV6GxeLJuiHyosw'
		consumer_secret = 'D89yuzda0mlpYCnOMPG1NK9koWnw0ksOWI6UL4zM'
		access_token = '2356976360-D8LrSAJ46ZsrCtvS34jFFDbm8GfqdUB4EvhUy4o'
		access_token_secret = 'fpuWA5O53hNHtYF4jgIvJ4uEugwOOcWEAVSEaIuwkztLb'
		api = twitter.Api(	consumer_key, consumer_secret, access_token, access_token_secret)
		statuses = api.GetSearch(query)
		one = statuses[0]
		for status in statuses:
			user = status.GetUser()
			text = status.GetText()
			print "@%s: %s" % (user.GetScreenName(), text)

t = twitter_bot()
t.searchTweets('#twitchispacman')