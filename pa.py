def parse_pa_origin(p):
	# 'ORIGIN'
	origin_length = int(p['raw'][4:6],16)
	origin = p['raw'][6:6+(origin_length*2)]
	o = {
		'00':'IGP',
		'01':'EGP',
		'02':'INCOMPLETE'
	}
	p['raw'] = p['raw'][6+(origin_length*2):]
	if origin in o: p['origin'] = o[origin]
	else: p['origin'] = 'unknown'
	return p
def parse_pa_as_path(p):
	# 'AS_PATH'
	as_path_length = int(p['raw'][4:6],16)
	as_path_index = 6+(as_path_length * 2)
	as_path = p['raw'][6:as_path_index]
	# check for blank AS_PATH
	if as_path_length == 0:
		p['raw'] = p['raw'][6+(as_path_length*2):]
		p['as_path'] = []
		return p
	# non-blank contains AS_SET or AS_SEQ
	seg_type = as_path[:2]
	seg_length = int(as_path[2:4],16)
	seg_index = 6 + (seg_length * 4)
	path = [str(int(as_path[4+x:8+x],16)) for x in range(0,len(as_path[4:seg_index]),4)]
	p['raw'] = p['raw'][6+(as_path_length*2):]
	p['as_path'] = path
	#if seg_type == '01': return '\tAS_PATH: AS_SET {' + ','.join(path) + '}'
	#elif seg_type == '02': return '\tAS_PATH: AS_SEQUENCE {' + ','.join(path) + '}'
	return p
def parse_pa_next_hop(p):
	# 'NEXT_HOP'
	next_hop_length = int(p['raw'][4:6],16)
	next_hop_index = 6+(next_hop_length*2)
	next_hop = p['raw'][6:next_hop_index]
	p['raw'] = p['raw'][6+(next_hop_length*2):]
	p['next_hop'] = hex_to_ip(next_hop)
	return p
def parse_pa_med(p):
	# 'MULTI_EXIT_DISC'
	med_length = int(p['raw'][4:6],16)
	med_index = 6+(med_length*2)
	med = int(p['raw'][6:med_index],16)
	p['raw'] = p['raw'][6+(med_length*2):]
	p['med'] = med
	return p
def parse_pa_local_pref(p):
	# 'LOCAL_PREF'
	local_pref_length = int(p['raw'][4:6],16)
	local_pref_index = 6+(local_pref_length*2)
	local_pref = int(p['raw'][6:local_pref_index],16)
	p['raw'] = p['raw'][6+(local_pref_length*2):]
	p['local_pref'] = local_pref
	return p
def parse_pa_atomic_agg(p):
	# 'ATOMIC_AGGREGATE'
	atomic_agg_length = int(p['raw'][4:6],16)
	atomic_agg_index = 6+(atomic_agg_length*2)
	atomic_agg = p['raw'][6:atomic_agg_index]
	p['raw'] = p['raw'][6+(atomic_agg_length*2):]
	p['atomic_agg'] = atomic_agg
	return p
def parse_pa_agg(p):
	# 'AGGREGATOR'
	a = {
		'speaker':None,
		'as':None
	}
	agg_length = int(p['raw'][4:6],16)
	agg_index = 6+(agg_length*2)
	agg = p['raw'][6:agg_index]
	a['as'] = p['raw'][agg_index:agg_index+4]
	a['speaker'] = hex_to_ip(p['raw'][agg_index+4:agg_index+8])
	p['raw'] = p['raw'][6+(agg_length*2):]
	p['agg'] = a
	return p
def hex_to_ip(h):
	o1,o2,o3,o4 = h[0:2],h[2:4],h[4:6],h[6:8]
	ip_address = '{0}.{1}.{2}.{3}'.format(
		int(o1,16),
		int(o2,16),
		int(o3,16),
		int(o4,16)
		)
	return ip_address