def display(self):
	# beginning portion of BGP packet, consistent with every message type
	# one tab deep
	print '\nRECEIVED:\n\traw: {0}'\
		'\n\tmarker: {1}'\
		'\n\tlength: {2} bytes'\
		'\n\ttype: {3}'\
		.format(
		self.raw,
		self.marker,
		int(self.length,16),
		self.type_human.upper()
		)
	# optional parameters define data relating to the message type
	if self.optional: print '\toptional params: {0}'.format(self.optional)
	# -- BEGIN : OPEN type
	if self.type_human == 'open':
		# two tabs deep
		output = '\t\tversion: {0}'\
			'\n\t\tAS: {1}'\
			'\n\t\thold: {2} seconds'\
			'\n\t\tid: {3}'\
			'\n\t\tlen(optional): {4} bytes'\
			'\n\t\toptional: {5}'\
			.format(
			int(self.open_version,16),
			int(self.open_as,16),
			int(self.open_hold_time,16),
			self.hex_to_ip(self.open_id),
			int(self.open_len_optional,16),
			self.open_optional
			)
		print output
		if len(self.open_optional) > 0: self.parse_open_optional()
	# -- END : OPEN type
	# -- BEGIN : UPDATE type
	elif self.type_human == 'update':
		output = '\t\tlen(withdrawn): {0}'\
			'\n\t\twithdrawn: {1}'\
			.format(
			self.u_withdrawn_length,
			self.u_withdrawn
			)
		#	'\n\t\tlen(path attributes): {2}'\
		#	'\n\t\tpath attributes: {3}'\
		#	'\n\t\tnlris: {4}'\
		#	.format(
		#	self.u_withdrawn_length,
		#	self.u_withdrawn,
		#	self.u_path_attribute_length,
		#	self.u_path_attributes,
		#	self.u_nlris
		#	)
		print output
		if len(self.u_withdrawn) > 0: self.parse_u_withdrawn()
		output = '\t\tlen(path attributes): {0}'\
			'\n\t\tpath attributes: {1}'\
			.format(
			self.u_path_attribute_length,
			self.u_path_attributes
			)
		print output
		if len(self.u_path_attributes) > 0:
			self.parse_u_pa()
			for x in self.p: print x
		output = '\t\tnlris: {0}'.format(self.u_nlris)
		print output
		if len(self.u_nlris) > 0: self.parse_u_nlri()
	# -- END : UPDATE type
	# -- BEGIN : NOTIFICATION type
	elif self.type_human == 'notification':
		error = {
			'01':'Message Header Error',
			'02':'OPEN Message Error',
			'03':'UPDATE Message Error',
			'04':'Hold Timer Expired',
			'05':'Finite State Machine Error',
			'06':'Cease'
		}
		if self.error_code in error:
			output = '\t\tError: {0}'\
				'\n\t\tSubcode: {1}'\
				.format(
				error[self.error_code],
				self.error_subcode
				)
			print output
		else:
			print '\t\tError: unknown'
	# -- END : NOTIFICATION type
	return