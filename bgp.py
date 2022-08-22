class bgp(object):
	def __init__(self,connection,address):
		self.conn = connection
		self.peer = address
		import sqlite3 as sql
		with sql.connect('db.db') as con:
			con.execute('UPDATE next_hop SET state = 0 WHERE state = 1')
			con.commit()
		return
	def inspect_packet(self,packet):
		from bgp_packet import bgp_packet
		#import display
		p = bgp_packet(packet)
		#p.get_type()
		p.parse()
		# check for OPEN
		if p.packet['header']['type'] == '01':
			p.send_open_confirm(self.conn)
			#print p.__dict__
		# check for KEEPALIVE
		elif p.packet['header']['type'] == '04':
			p.send_keepalive_confirm(self.conn)
		# check for UPDATE
		elif p.packet['header']['type'] == '02':
			p.send_keepalive_confirm(self.conn)
			self.db_work(p)
			#print p.__dict__
		return
	def inspect_recv(self,data):
		# queue packets received by socket buffers
		packets = []
		# buffers can contain more than one packet, check offset for length
		if len(data)/2 > int(data[32:36],16):
			while len(data) > 0:
				ptemp = data[0:int(data[32:36],16)*2]
				packets.append(ptemp)
				data = data.replace(ptemp,'')
		else:
			packets.append(data)
		for x in packets: self.inspect_packet(x)
		# keep memory clean
		del packets
		return
	def db_work(self,packet):
		import sqlite3 as sql
		with sql.connect('db.db') as con:
			# if exist within 'insert'
			if len(packet.packet['type_field']['insert']['nlri']) > 0:
				for net in packet.packet['type_field']['insert']['nlri']:
					ex = con.execute('SELECT count(net) FROM nlri WHERE net = "' + net + '"')
					result = ex.fetchall()
					# create row if NLRI does not exist
					if result[0][0] == 0:
						con.execute('INSERT INTO nlri (net) VALUES ("' + net + '")')
						con.commit()
					ex = con.execute('SELECT rowid FROM nlri WHERE net = "' + net + '"')
					nlri_id = ex.fetchall()
					# check next_hop table for existing entries
					ex = con.execute('SELECT count(address) FROM next_hop WHERE nlri_id = ' + str(nlri_id[0][0]) + ' AND address = "' + packet.packet['type_field']['attribute']['next_hop'] + '"')
					result = ex.fetchall()
					if result[0][0] == 0:
						con.execute('INSERT INTO next_hop (nlri_id,address,state) VALUES (' + str(nlri_id[0][0]) + ',"' + packet.packet['type_field']['attribute']['next_hop'] + '",1)')
					else:
						con.execute('UPDATE next_hop SET state = 1 WHERE nlri_id = (SELECT rowid FROM nlri WHERE net = "' + net + '")')
			# if exist within 'withdraw'
			if len(packet.packet['type_field']['withdraw']['nlri']) > 0:
				for net in packet.packet['type_field']['withdraw']['nlri']:
					con.execute('UPDATE next_hop SET state = 0 WHERE nlri_id = (SELECT rowid FROM nlri WHERE net = "' + net + '")')
			con.commit()
		return