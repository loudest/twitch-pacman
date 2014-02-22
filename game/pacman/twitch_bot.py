import sys, socket, string

def connect():

   HOST="irc.twitch.tv"
   PORT=6667
   NICK="not_lying"
   IDENT="pacman"    
   REALNAME="Twitch plays pacman"
   CHANNEL="#pacman"

   readbuffer = ""
   irc=socket.socket( )
   irc.connect((HOST, PORT))
   irc.send("PASS oauth:4vbd0oj5s68rfexwvkywzhicp6zyaal")
   irc.send("NICK %s\r\n" % NICK)
   irc.send("USER %s %s :%s\r\n" % (IDENT, IDENT, REALNAME))
   irc.send("JOIN %s\r\n" % (CHANNEL))
   irc.send ('PRIVMSG #pacman: hello\r\n')

   while True: 
      data = irc.recv(4096)
      if data.find('PING') != -1:
         irc.send('PONG '+data.split()[ 1 ]+'\r\n')      
      if data.find ('hello') != -1:
         irc.send ('PRIVMSG #pacman: hello\r\n')
      print data

connect()