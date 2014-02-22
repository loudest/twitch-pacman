network = 'irc'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK botty\r\n' )
irc.send ( 'USER botty botty botty :Python IRC\r\n' )
irc.send ( 'JOIN #paul\r\n' )
irc.send ( 'PRIVMSG #Paul :Hello World.\r\n' )
while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( '!botty quit' ) != -1:
      irc.send ( 'PRIVMSG #paul :Fine, if you don't want me\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'hi botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
   if data.find ( 'hello botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #paul\r\n' )
   if data.find ( 'cheese' ) != -1:
      irc.send ( 'PRIVMSG #paul :WHERE!!!!!!\r\n' )
   if data.find ( 'slaps botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
   print data
rk = 'irc.snm.co.nz'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK botty\r\n' )
irc.send ( 'USER botty botty botty :Python IRC\r\n' )
irc.send ( 'JOIN #paul\r\n' )
irc.send ( 'PRIVMSG #Paul :Hello World.\r\n' )
while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( '!botty quit' ) != -1:
      irc.send ( 'PRIVMSG #paul :Fine, if you don't want me\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'hi botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
   if data.find ( 'hello botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #paul\r\n' )
   if data.find ( 'cheese' ) != -1:
      irc.send ( 'PRIVMSG #paul :WHERE!!!!!!\r\n' )
   if data.find ( 'slaps botty' ) != -1:
      irc.send ( 'PRIVMSG #paul :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
   print data
