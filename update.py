# -- BEGIN : parsing portions of UPDATE
def parse_withdrawn(u):
	wd = []
	copy = u['withdraw']['raw']
	while len(copy) > 0:
		cidr = int(copy[0:2],16)
		offset = 2 + (cidr/8) * 2
		prefix_hex = copy[2:offset]
		prefix_ddn = []
		for x in range(0,len(prefix_hex),2):
			prefix_ddn.append(
				str(int(prefix_hex[x:x+2],16))
				)
		copy = copy[offset:]
		full = '.'.join(prefix_ddn) + '/' + str(cidr)
		wd.append(full)
	# u['withdraw']['nlri'] = wd
	return wd
def parse_pa(u):
	import pa
	p = {
		'raw':None,
		'origin':None,
		'as_path':[],
		'next_hop':None,
		'med':None,
		'local_pref':None,
		'agg':None,
		'atomic_agg':None
	}
	p['raw'] = u['attribute']['raw']
	original = u['attribute']['raw']
	while len(p['raw']) > 0:
		#flags_raw = bin(int(p['raw'][0:1]))[2:]
		#while len(flags_raw) < 4: flags_raw = '0' + flags_raw
		#flags = 'optional,' if flags_raw[0] is '1' else 'well-known,'
		#flags += 'transitive,' if flags_raw[1] is '1' else 'non-transitive,'
		#flags += 'partial,' if flags_raw[2] is '1' else 'complete,'
		#flags += 'extended length,' if flags_raw[3] is '1' else 'regular length,'
		#
		t = {
			'01':pa.parse_pa_origin,
			'02':pa.parse_pa_as_path,
			'03':pa.parse_pa_next_hop,
			'04':pa.parse_pa_med,
			'05':pa.parse_pa_local_pref,
			'06':pa.parse_pa_atomic_agg,
			'07':pa.parse_pa_agg
		}
		if p['raw'][2:4] in t: p = t[p['raw'][2:4]](p)
	p['raw'] = original
	return p
def parse_nlri(u):
	# to test :
	# nlri = '18033b002001010101'
	n = []
	copy = u['insert']['raw']
	while len(copy) > 0:
		cidr = int(copy[0:2],16)
		offset = 2 + (cidr/8) * 2
		prefix_hex = copy[2:offset]
		prefix_ddn = []
		for x in range(0,len(prefix_hex),2):
			prefix_ddn.append(
				str(int(prefix_hex[x:x+2],16))
				)
		copy = copy[offset:]
		full = '.'.join(prefix_ddn) + '/' + str(cidr)
		n.append(full)
	return n
# -- END : parsing portions of UPDATE