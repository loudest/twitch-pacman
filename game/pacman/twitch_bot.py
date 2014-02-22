import sys, socket, string, random
from threading import Thread

class twitch_bot(Thread):

   def __init__(self, game, player, level):
      Thread.__init__(self)
      self.running = True
      self.game = game
      self.player = player
      self.level = level

   def connect(self):

      HOST="irc.twitch.tv"
      PORT=6667
      NICK="lxndkcfi"
      IDENT="pacman"    
      REALNAME="Twitch plays pacman"
      CHANNEL="#pacman"

      readbuffer = ""
      irc=socket.socket()
      irc.connect((HOST, PORT))
      irc.send("PASS oauth:7xd9z7gljnxy3kr42uuberuumnaqaoh\r\n")
      irc.send("NICK %s\r\n" % NICK)
      irc.send("USER %s %s :%s\r\n" % (IDENT, IDENT, REALNAME))
      irc.send("JOIN %s\r\n" % (CHANNEL))

      while True: 
         data = irc.recv(1024)
         if data.find('PING') != -1:
            irc.send('PONG '+data.split()[ 1 ]+'\r\n')

         list = data.split()
         if(len(list) >= 4):
            #pac-man commands
            command = data.split()[3].lower()
            print "COMMAND: %s\n" % (command) 
            if data.find ('right') != -1:
               self.game.input(self.player, self.level, 'd')
               print "PAC-MAN RIGHT\n"
            if data.find ('left') != -1:
               self.game.input(self.player, self.level, 'a')
               print "PAC-MAN LEFT\n"
            if data.find ('up') != -1:
               self.game.input(self.player, self.level, 'w')
               print "PAC-MAN UP\n"
            if data.find ('down') != -1:
               self.game.input(self.player, self.level, 's')
               print "PAC-MAN DOWN\n"            
         print data

   def run(self):
      self.connect()