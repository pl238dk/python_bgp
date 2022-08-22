def prepare_socket():
	import socket
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('3.59.0.1',179))
	while True: establish_peer(s)
	s.close()
	return

def establish_peer(s):
	from bgp import bgp
	print 'Listening for BGP peer ...'.format()
	s.listen(1)
	conn, addr = s.accept()
	print 'connection to {0}'.format(addr)
	b = bgp(conn,addr)
	while True:
		data = conn.recv(1024)
		if not data: break
		b.inspect_recv(data.encode('hex'))
	conn.close()
	print 'Peer session closed. Re-establishing ...'
	return

if __name__ == '__main__':
	prepare_socket()