import sys, socket, string, random
from threading import Thread

class twitch_bot(Thread):

   def __init__(self, game):
      Thread.__init__(self)
      self.running = True
      self.game = game

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
         if data.find ('hello') != -1:
            irc.send ('PRIVMSG #pacman: hello\r\n')
         print data

   def run(self):
      self.connect()