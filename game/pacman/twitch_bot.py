import sys, socket, string, random
from threading import Thread

class twitch_bot(Thread):

   def __init__(self, game, player):
      Thread.__init__(self)
      self.running = True
      self.game = game
      self.player = player

   def connect(self):

      HOST="irc.twitch.tv"
      PORT=6667
      NICK="not_lying"
      IDENT="pacman"    
      REALNAME="Twitch plays pacman"
      CHANNEL="#pacman"

      readbuffer = ""
      irc=socket.socket()
      irc.connect((HOST, PORT))
      irc.send("PASS oauth:4vbd0oj5s68rfexwvkywzhicp6zyaal\r\n")
      irc.send("NICK %s\r\n" % NICK)
      irc.send("USER %s %s :%s\r\n" % (IDENT, IDENT, REALNAME))
      irc.send("JOIN %s\r\n" % (CHANNEL))

      while True: 
         data = irc.recv(4096)
         if data.find('PING') != -1:
            irc.send('PONG '+data.split()[ 1 ]+'\r\n')

         command = data.split()[:1].lower() 
         if command.find ('right') != -1:
            self.game.CheckInputs(self.player,'d')
            print "PAC-MAN RIGHT\n"
         if command.find ('left') != -1:
            self.game.CheckInputs(self.player,'a')
            print "PAC-MAN LEFT\n"
         if command.find ('up') != -1:
            self.game.CheckInputs(self.player,'s')
            print "PAC-MAN LEFT\n"
         if command.find ('left') != -1:
            self.game.CheckInputs(self.player,'w')
            print "PAC-MAN DOWN\n"            
         print data

   def run(self):
      self.connect()