import sys, socket, string, random, os, time, traceback, logging, twitter, json, calendar
from datetime import datetime
from threading import Thread

# 180 requests, 900 seconds = 5 Seconds between requests
SEARCH_DELAY = 5
UNITS_OF_WORK = 200
REQUESTS_PER_WINDOW = 180
WINDOW_DURATION = 15 *60
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'output')

# FIXME: Share this properly
def enum(**enums):
    return type('Enum', (), enums)

# Movement Directions
Directions = enum(RIGHT=1, LEFT=2, UP=3, DOWN=4)

class twitter_bot(Thread):

	def __init__(self, players, level, textFileBuffer):
          Thread.__init__(self)
          self.running = True
          self.players = players
          self.level = level
          self.textFileBuffer = textFileBuffer
          self.uow = UNITS_OF_WORK
          self.logger = logging.getLogger('pacman')

          self.consumer_key = 'ugD4ZKV6GxeLJuiHyosw'
          self.consumer_secret = 'D89yuzda0mlpYCnOMPG1NK9koWnw0ksOWI6UL4zM'
          self.access_token = '2356976360-D8LrSAJ46ZsrCtvS34jFFDbm8GfqdUB4EvhUy4o'
          self.access_token_secret = 'fpuWA5O53hNHtYF4jgIvJ4uEugwOOcWEAVSEaIuwkztLb'
          self.api = twitter.Api(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)

        def flush(self):
          return

        def read_integer(self, filename, default = 0):
          file_path = os.path.join(OUTPUT_DIRECTORY, filename)
          if os.path.isfile(file_path):
            f = open(file_path, 'r')
            number = int(f.readline().strip())
            f.close()
            return number
          else:
            return default

        def write_integer(self, number, filename):
          file_path = os.path.join(OUTPUT_DIRECTORY, filename)
          f = open(file_path, 'w')
          f.write(str(number))
          f.close()

	def searchPacmanTweets(self):
          # Pacman
          try:
            since_id = self.read_integer("twitchispacman_since_id.txt")
            truncated = True

            while truncated and (self.api_requests_remaining > 0):
              self.api_requests_remaining -= 1
              statuses = self.api.GetSearch('#twitchispacman', geocode=None, since_id=since_id, count=100)
              if len(statuses) is 0:
                truncated = False 

              for status in statuses:
                status_since_id = str(status.GetId())
                if (status_since_id > since_id): since_id = status_since_id 
                user = status.GetUser().GetScreenName()
                data = status.GetText().lower()
                truncated = status.GetTruncated()

                if(data.find ('right') != -1):
                  self.logger.info("@" + user + " Pac-Man :right")
                  self.players[0].QueueMove(Directions.RIGHT, self.level)
                  self.textFileBuffer.pacman_move_queue.append("RIGHT | @" + user)
                elif(data.find('left') != -1):
                  self.logger.info("@" + user + " Pac-Man :left")
                  self.players[0].QueueMove(Directions.LEFT, self.level)
                  self.textFileBuffer.pacman_move_queue.append(" LEFT | @" + user)
                elif(data.find('up') != -1):
                  self.logger.info("@" + user + " Pac-Man :up")
                  self.players[0].QueueMove(Directions.UP, self.level)
                  self.textFileBuffer.pacman_move_queue.append("   UP | @" + user)
                elif(data.find('down') != -1):
                  self.logger.info("@" + user + " Pac-Man :down")
                  self.players[0].QueueMove(Directions.DOWN, self.level)
                  self.textFileBuffer.pacman_move_queue.append(" DOWN | @" + user)

            self.write_integer(since_id, "twitchispacman_since_id.txt")
          except:
            self.logger.error("Unexpected error fetching Pacman tweets:" + traceback.format_exc())

          # Ghost
	def searchGhostTweets(self):
          try:
            since_id = self.read_integer("twitchisblinky_since_id.txt")
            truncated = True

            while truncated and (self.api_requests_remaining > 0):
              self.api_requests_remaining -= 1
              statuses = self.api.GetSearch('#twitchisblinky', geocode=None, since_id=since_id, count=100)
              if len(statuses) is 0:
                truncated = False 

              for status in statuses:
                status_since_id = str(status.GetId())
                if (status_since_id > since_id): since_id = status_since_id 
                user = status.GetUser().GetScreenName()
                data = status.GetText().lower()
                truncated = status.GetTruncated()

                if(data.find ('right') != -1):
                  self.logger.info("@" + user + " Blinky :right")
                  self.players[1].QueueMove(Directions.RIGHT, self.level)
                  self.textFileBuffer.ghost_move_queue.append("RIGHT | @" + user)
                elif(data.find('left') != -1):
                  self.logger.info("@" + user + " Blinky :left")
                  self.players[1].QueueMove(Directions.LEFT, self.level)
                  self.textFileBuffer.ghost_move_queue.append(" LEFT | @" + user)
                elif(data.find('up') != -1):
                  self.logger.info("@" + user + " Blinky :up")
                  self.players[1].QueueMove(Directions.UP, self.level)
                  self.textFileBuffer.ghost_move_queue.append("   UP | @" + user)
                elif(data.find('down') != -1):
                  self.logger.info("@" + user + " Blinky :down")
                  self.players[1].QueueMove(Directions.DOWN, self.level)
                  self.textFileBuffer.ghost_move_queue.append(" DOWN | @" + user)

            self.write_integer(since_id, "twitchisblinky_since_id.txt")
          except:
            self.logger.error("Unexpected error fetching ghost tweets:" + traceback.format_exc())

                  
	def run(self):
          self.logger.info("Twitter bot starting, UOW is " + str(self.uow))
          self.api_requests_remaining = self.read_integer("twitter_bot_api_requests_remaining.txt", REQUESTS_PER_WINDOW)
          start_time = datetime.utcfromtimestamp(self.read_integer("twitter_bot_start_time.txt", time.time()))

          while (self.running and self.uow > 0):
            self.uow -= 1

            self.searchPacmanTweets()
            time.sleep(SEARCH_DELAY)
            if not self.running: break

            self.searchGhostTweets()
            time.sleep(SEARCH_DELAY)

            if (datetime.utcnow() - start_time).seconds > WINDOW_DURATION:
              self.api_requests_remaining = REQUESTS_PER_WINDOW
              start_time = datetime.utcnow()

          self.write_integer(calendar.timegm(start_time.utctimetuple()), "twitter_bot_start_time.txt")
          self.write_integer(self.api_requests_remaining, "twitter_bot_api_requests_remaining.txt")
          self.logger.info("Twitter Bot stopping, UOW is " + str(self.uow))

	def stop_running(self):
          self.running = False
          self.logger.info("Twitter Bot set to shutdown")
