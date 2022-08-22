# -- BEGIN : parsing portions of OPEN
def parse_optional(o):
	# to test :
	# optional = '02060104000100010202800002020200'
	option_list = []
	copy = o['raw']
	while len(copy) > 0:
		capability_code = copy[:2]
		capability_length = int(copy[2:4],16)
		capability_length_index = 4 + (capability_length * 2)
		capability = copy[:capability_length_index]
		option_list.append(capability)
		copy = copy[capability_length_index:]
	results = []
	for x in option_list: results.append(parse_capability(x))
	o['capability'] = results
	return o
# -- END : parsing portions of OPEN
def parse_capability(capability):
	# three tab deep
	cap_code = capability[:2]
	cap_length = int(capability[2:4],16)
	cap_index = 4 + (cap_length * 2)
	cap_subcode = capability[4:6]
	cap = capability[6:cap_index]
	if cap_subcode == '01':
		#cap_mp_afi = cap[:4]
		#decode_afi(cap_mp_afi)
		afi = decode_afi(cap[2:6])
		cap_mp_reserved = cap[6:8]
		#cap_mp_safi = cap[6:8]
		#decode_safi(cap_mp_safi)
		safi = decode_safi(cap[8:10])
		c = 'Multi-Protocol Extensions - {0},{1}'.format(afi,safi)
	elif cap_subcode == '02': c = 'Route-Refresh'
	elif cap_subcode == '80': c = 'Route-Refresh - Cisco'
	else: c = 'unknown'
	return c
def decode_afi(code):
	afi = {
		'0000':'Reserved',
		'0001':'IPv4',
		'0002':'IPv6'
		# other uncommon AFI codes omitted
	}
	if code in afi:
		return afi[code]
	else:
		return 'unknown'
def decode_safi(code):
	safi = {
		'00':'Reserved',
		'01':'Unicast',
		'02':'Multicast',
		'03':'Reserved',
		'04':'NLRI w/ MPLS Labels'
		# other uncommon SAFI codes omitted
	}
	if code in safi:
		return safi[code]
	else:
		return 'unknown'

#if __name__ == '__main__':
	# optional = '02060104000100010202800002020200'
	# parse_open_optional(optional)	