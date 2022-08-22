from thread import *
from bgp import bgp
from socket import *

# mandatory ASCII art
welcome_message = '''
############################################
#  _____ _____ _____    _____              #
# | __  |   __|  _  |  |  _  |___ ___ ___  #
# | __ -|  |  |   __|  |   __| -_| -_|  _| #
# |_____|_____|__|     |__|  |___|___|_|   #
#                                          #
############################################
#  Main executable: speak BGP with Python  #
############################################
'''

def establish_peer(conn, addr):
	print 'Starting new peer with', addr
	b = bgp(conn, addr)
	while True:
		data = conn.recv(1024)
		if not data: 
			break
		b.inspect_recv(data.encode('hex'))

if __name__ == '__main__':
	print welcome_message
	host = '3.59.0.1'
	port = 179
	sock = socket(AF_INET,SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(5)
	while True:
		conn, addr = sock.accept()
		start_new_thread(establish_peer, (conn, addr))
	conn.close()
	sock.close()

