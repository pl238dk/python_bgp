#### Additions : Jason Smith - Cisco#### Add support for single connections to multiple BGP peer host adapters##import threading

class ThreadedBGP(object):
	def __init__(self, ip):
		self.ip = ip
		thread = threading.Thread(target=self.prepare_socket, args=())
		thread.daemon = True
		thread.start()
	
	def prepare_socket(self):
		import socket
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.bind((self.ip,179))
		while True: establish_peer(s)
		s.close()
		print self.ip, "Closing"
		return

	def establish_peer(self,s):
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
	peers = ['1.1.1.1', '2.2.2.2']
	threads = []
	for p in peers:
		threads.append(ThreadedBGP(p))