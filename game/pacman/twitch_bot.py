import sys, socket, string, random
from threading import Thread

HOST="irc.twitch.tv"
PORT=6667
NICK="adfadfadfadfadf"
IDENT="pacman"    
REALNAME="Twitch plays pacman"
CHANNEL_ONE="#twitchispacman"
CHANNEL_TWO="#twitchisblinky"
PRIV_MSG="PRIVMSG"

# FIXME: Share this properly
def enum(**enums):
    return type('Enum', (), enums)

# Movement Directions
Directions = enum(RIGHT=1, LEFT=2, UP=3, DOWN=4)

class twitch_bot(Thread):

   def __init__(self, players, level):
      Thread.__init__(self)
      self.running = True
      self.players = players
      self.level = level

   def connect(self):

      readbuffer = ""
      irc=socket.socket()
      # Set a timeout of two seconds
      irc.settimeout(2)
      irc.connect((HOST, PORT))
      irc.send("PASS oauth:a7k5b9vzxor9d6tzarlia9rjw2c24kn\r\n")
      irc.send("NICK %s\r\n" % NICK)
      irc.send("USER %s %s :%s\r\n" % (IDENT, IDENT, REALNAME))
      irc.send("JOIN %s\r\n" % (CHANNEL_ONE))
      irc.send("JOIN %s\r\n" % (CHANNEL_TWO))

      while self.running:
        try:
           data = irc.recv(1024)
           if data.find('PING') != -1:
              irc.send('PONG '+data.split()[ 1 ]+'\r\n')

           list = data.split()
           if(len(list) >= 4):
              # TODO: Add the nickname of the caller, and write it to file
              # Example - :tonyzipper!tonyzipper@tonyzipper.tmi.twitch.tv PRIVMSG #twitchisblinky :down
              print "[DATA]", data, "[/DATA]"
              data = data.split()
              user = data[0][1:data[0].index('!')].strip()
              message_type = data[1].upper().strip()
              channel = data[2].lower().strip()
              command = data[3].lower().strip()
              print "[MSG_TYPE]", message_type, "[/MSG_TYPE]"

              if(message_type == PRIV_MSG):
                print "[CHANNEL]", channel, "[/CHANNEL]"
                if(channel == CHANNEL_ONE):
                  print user, "Pac-Man", command
                  if (command == ':right'):
                     self.players[0].QueueMove(Directions.RIGHT, self.level)
                  elif (command == ':left'):
                     self.players[0].QueueMove(Directions.LEFT, self.level)
                  elif (command == ':up'):
                     self.players[0].QueueMove(Directions.UP, self.level)
                  elif (command == ':down'):
                     self.players[0].QueueMove(Directions.DOWN, self.level)

                elif(channel == CHANNEL_TWO):
                  print user, "Blinky", command
                  if (command == ':right'):
                     self.players[1].QueueMove(Directions.RIGHT, self.level)
                  elif (command == ':left'):
                     self.players[1].QueueMove(Directions.LEFT, self.level)
                  elif (command == ':up'):
                     self.players[1].QueueMove(Directions.UP, self.level)
                  elif (command == ':down'):
                     self.players[1].QueueMove(Directions.DOWN, self.level)

        except socket.timeout:
          #print 'Socket Timeout - consider lengthing the socket timing'
          pass
        except ValueError:
          print 'Value error - this is not a Pac-Man command. Passing.'

   def run(self):
      self.connect()

   def stop_running(self):
      self.running = False
      print "Twitch Bot set to shutdown"

