open='ffffffffffffffffffffffffffffffff002d01040001000f070707071002060104000100010202800002020200'
update='ffffffffffffffffffffffffffffffff004e02000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a'
keepalive='ffffffffffffffffffffffffffffffff001304'
notification=''

class bgp_packet(object):
	def __init__(self,data):
		self.packet = {
			'raw':data,
			'header':{
				# marker is always 16-octets, all FF
				'marker':data[0:32],
				'length':data[32:36],
				'type':data[36:38],
				'data':''
			},
			'type_field':{}
		}
		# keepalive packets consist of marker, 2-octet length, and type code 04
		if int(self.packet['header']['length'],16) > 19:
			self.packet['header']['data'] = data[38:]
		return
	def parse(self):
		t = {
			'01':self.msg_open,
			'02':self.msg_update,
			'03':self.msg_notification,
			'04':self.msg_keepalive
		}
		if self.packet['header']['type'] in t:
			return t[self.packet['header']['type']]()
		return
# -- BEGIN : message types
	def msg_open(self):
		# opop shortened from open_optional
		import open as opop
		o = {
			'version':None,
			'as':None,
			'hold':None,
			'id':None,
			'optional':{
				'length':None,
				'raw':None,
				'auth':None,
				'capability':[]
			}
		}
		o['version'] = self.packet['header']['data'][0:2]
		o['as'] = self.packet['header']['data'][2:6]
		o['hold'] = self.packet['header']['data'][6:10]
		o['id'] = self.packet['header']['data'][10:18]
		o['optional']['length'] = self.packet['header']['data'][18:20]
		o['optional']['raw'] = self.packet['header']['data'][20:]
		if len(o['optional']['raw']) > 0: o['optional'] = opop.parse_optional(o['optional'])
		# assign to full packet
		self.packet['type_field'] = o
		return
	def msg_update(self):
		import update
		u = {
			'withdraw':{
				'length':None,
				'raw':None,
				'nlri':[],
			},
			'insert':{
				'raw':None,
				'nlri':[]
			},
			'attribute':{
				'raw':None,
				'origin':None,
				'as_path':[],
				'next_hop':None,
				'med':None,
				'local_pref':None,
				'agg':None,
				'atomic_agg':None
			}
		}
		# withdrawn routes
		u['withdraw']['length'] = self.packet['header']['data'][0:4]
		wd_index = 4 + (int(u['withdraw']['length'],16) * 2)
		u['withdraw']['raw'] = self.packet['header']['data'][4:wd_index]
		if u['withdraw']['raw']: u['withdraw']['nlri'] = update.parse_withdrawn(u)
		# path attributes
		pa_length = int(self.packet['header']['data'][wd_index:wd_index + 4],16)
		pa_index = wd_index + 4 + (pa_length * 2)
		u['attribute']['raw'] = self.packet['header']['data'][wd_index + 4:pa_index]
		if u['attribute']['raw']: u['attribute'] = update.parse_pa(u)
		# NLRIs
		u['insert']['raw'] = self.packet['header']['data'][pa_index:]
		if len(u['insert']['raw']) > 0: u['insert']['nlri'] = update.parse_nlri(u)
		# assign to full packet
		self.packet['type_field'] = u
		return
	def msg_notification(self):
		n = {
			'error':{
				'code':'',
				'subcode':'',
				'data':''
			}
		}
		n['error']['code'] = self.packet['header']['data'][0:2]
		n['error']['subcode'] = int(self.packet['header']['data'][2:4],16)
		self.packet['type_field'] = n
		return
	def msg_keepalive(self):
		k = {
			'raw':'ffffffffffffffffffffffffffffffff001304',
			'header':{
				'marker':'ffffffffffffffffffffffffffffffff',
				'length':19,
				'type':'04'
			}
		}
		return
# -- END : message types
# -- BEGIN : responses
	def send_open_confirm(self,conn):
		# server ip address is statically typed, fix to add dynamically-assigned
		prep = self.packet['header']['marker'] + self.packet['header']['length'] + self.packet['header']['type'] + \
			self.packet['type_field']['version'] + self.packet['type_field']['as'] + self.packet['type_field']['hold'] + \
			self.ip_to_hex('3.59.0.1') + self.packet['type_field']['optional']['length'] + self.packet['type_field']['optional']['raw']
		reply = self.hex_to_bytestr(prep)
		conn.sendall(reply)
		return
	def send_keepalive_confirm(self,conn):
		# blank marker, length of 19 bytes, message type 4
		raw = 'ffffffffffffffffffffffffffffffff001304'
		reply = self.hex_to_bytestr(raw)
		conn.sendall(reply)
		return
# -- END : responses
# -- BEGIN : tool functions
	def hex_to_ip(self,h):
		o1,o2,o3,o4 = h[0:2],h[2:4],h[4:6],h[6:8]
		ip_address = '{0}.{1}.{2}.{3}'.format(
			int(o1,16),
			int(o2,16),
			int(o3,16),
			int(o4,16)
			)
		return ip_address
	def ip_to_hex(self,ip_address):
		h = ''.join('%02x' % int(x) for x in ip_address.split('.'))
		return h
	def hex_to_bytestr(self,h):
		b = []
		for i in range(0,len(h),2):
			b.append( chr( int( h[i:i+2], 16 ) ) )
		bytestr = ''.join(b)
		return bytestr
# -- END : tool functions

if __name__ == '__main__':
	p = test_packet(open)
	p.parse()
	print p.__dict__