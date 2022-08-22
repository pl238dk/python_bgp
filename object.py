'''
RECEIVED:
        raw: ffffffffffffffffffffffffffffffff002d01040001000f070707071002060104000100010202800002020200
        marker: ffffffffffffffffffffffffffffffff
        length: 45 bytes
        type: OPEN
        optional params: 040001000f070707071002060104000100010202800002020200
                version: 4
                AS: 1
                hold: 15 seconds
                id: 7.7.7.7
                len(optional): 16 bytes
                optional: 02060104000100010202800002020200
                        capability: multiprotocol extensions - IPv4,Unicast
                        capability: Route-refresh - Cisco
                        capability: Route-refresh
'''
open_pkt = {'packet': {'raw': 'ffffffffffffffffffffffffffffffff002d01040001000f070707071002060104000100010202800002020200', 'type_field': {'as': '0001', 'version': '04', 'optional': {'capability': [], 'raw': '02060104000100010202800002020200', 'length': '10', 'auth': None}, 'hold': '000f', 'id': '07070707'}, 'header': {'marker': 'ffffffffffffffffffffffffffffffff', 'data': '040001000f070707071002060104000100010202800002020200', 'length': '002d', 'type': '01'}}}
open_packet = {
	'raw':'ffffffffffffffffffffffffffffffff002d01040001000f070707071002060104000100010202800002020200',
	'header':{
		'marker':'ffffffffffffffffffffffffffffffff',
		'length':45,
		'type':'OPEN',
		'data':'040001000f070707071002060104000100010202800002020200'
	},
	'type_field':{
		'version':4,
		'as':1,
		'hold':15,
		'id':'7.7.7.7',
		'optional':{
			'raw':'02060104000100010202800002020200',
			'length':16,
			'auth':None,
			'capability':[
				'multiprotocol extensions - IPv4, Unicast',
				'Route-refresh - Cisco',
				'Route-refresh'
			]
		}
	}
}

'''
RECEIVED:
        raw: ffffffffffffffffffffffffffffffff004e02000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a
        marker: ffffffffffffffffffffffffffffffff
        length: 78 bytes
        type: UPDATE
        optional params: 000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a
                len(withdrawn): 0
                withdrawn:
                len(path attributes): 40
                path attributes: 4001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064
                        well-known,transitive,complete,regular length,  ORIGIN: INCOMPLETE
                        well-known,transitive,complete,regular length,  AS_PATH: AS_SEQUENCE {2,222,223,224,225}
                        well-known,transitive,complete,regular length,  NEXT_HOP: 10.1.2.2
                        optional,non-transitive,complete,regular length,        MED: 0
                        well-known,transitive,complete,regular length,  LOCAL_PREF: 100
                nlris: 200a1e1e1e200a141414200a0a0a0a
                        NLRI: 10.30.30.30/32
                        NLRI: 10.20.20.20/32
                        NLRI: 10.10.10.10/32
'''

update_pkt = {'packet': {'raw': 'ffffffffffffffffffffffffffffffff004e02000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a', 'type_field': {'insert': {'raw': '200a1e1e1e200a141414200a0a0a0a', 'nlri': ['10.30.30.30/32', '10.20.20.20/32', '10.10.10.10/32']}, 'withdraw': {'raw': '', 'length': '0000', 'nlri': []}, 'attribute': []}, 'header': {'marker': 'ffffffffffffffffffffffffffffffff', 'data': '000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a', 'length': '004e', 'type': '02'}}}
update_packet = {
	'raw':'ffffffffffffffffffffffffffffffff004e02000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a',
	'header':{
		'marker':'ffffffffffffffffffffffffffffffff',
		'length':78,
		'type':'UPDATE',
		'data':'000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a'
	},
	'type_field':{
		'withdraw':{
			'length':0,
			'nlri':[]
		},
		'insert':{
			'nlri':[]
		},
		'attributes':{
			'origin':'INCOMPLETE',
			'as_path':[2,222,223,224,225],
			'next_hop':'10.1.2.2',
			'med':0,
			'local_pref':100,
			'agg':'',
			'atomic_agg':''
		}
	}
}

keepalive_packet = {
	'raw':'ffffffffffffffffffffffffffffffff001304',
	'header':{
		'marker':'ffffffffffffffffffffffffffffffff',
		'length':19,
		'type':'KEEPALIVE'
	}
}

notification_packet = {
	'raw':'',
	'header':{
		'marker':'ffffffffffffffffffffffffffffffff',
		'length':,
		'type':'NOTIFICATION',
		'data':''
	},
	'type_field':{
		'error':{
			'code':'',
			'subcode':'',
			'data':''
		}
	}
}


## so far
{'packet': {'raw': 'ffffffffffffffffffffffffffffffff002d01040001000f070707071002060104000100010202800002020200', 'type_field': {'as': '0001', 'version': '04', 'optional': {'capability': ['Multi-Protocol Extensions - IPv4,Unicast', 'Route-Refresh - Cisco', 'Route-Refresh'], 'raw': '02060104000100010202800002020200', 'length': '10', 'auth': None}, 'hold': '000f', 'id': '07070707'}, 'header': {'marker': 'ffffffffffffffffffffffffffffffff', 'data': '040001000f070707071002060104000100010202800002020200', 'length': '002d', 'type': '01'}}}
{'packet': {'raw': 'ffffffffffffffffffffffffffffffff005e020000001c40010102400200400304033b00818004040000000040050400000064180a0102200707070720060606062005050505200404040418033b00200303030320020202022001010101', 'type_field': {'insert': {'raw': '180a0102200707070720060606062005050505200404040418033b00200303030320020202022001010101', 'nlri': ['10.1.2/24', '7.7.7.7/32', '6.6.6.6/32', '5.5.5.5/32', '4.4.4.4/32', '3.59.0/24', '3.3.3.3/32', '2.2.2.2/32', '1.1.1.1/32']}, 'withdraw': {'raw': '', 'length': '0000', 'nlri': []}, 'attribute': {'origin': 'INCOMPLETE', 'raw': '40010102400200400304033b00818004040000000040050400000064', 'next_hop': '3.59.0.129', 'med': 0, 'agg': None, 'local_pref': 100, 'atomic_agg': None, 'as_path': []}}, 'header': {'marker': 'ffffffffffffffffffffffffffffffff', 'data': '0000001c40010102400200400304033b00818004040000000040050400000064180a0102200707070720060606062005050505200404040418033b00200303030320020202022001010101', 'length': '005e', 'type': '02'}}}
{'packet': {'raw': 'ffffffffffffffffffffffffffffffff003c020000002040010102400204020100024003040a0102028004040000000040050400000064200a282828', 'type_field': {'insert': {'raw': '200a282828', 'nlri': ['10.40.40.40/32']}, 'withdraw': {'raw': '', 'length': '0000', 'nlri': []}, 'attribute': {'origin': 'INCOMPLETE', 'raw': '40010102400204020100024003040a0102028004040000000040050400000064', 'next_hop': '10.1.2.2', 'med': 0, 'agg': None, 'local_pref': 100, 'atomic_agg': None, 'as_path': ['2']}}, 'header': {'marker': 'ffffffffffffffffffffffffffffffff', 'data': '0000002040010102400204020100024003040a0102028004040000000040050400000064200a282828', 'length': '003c', 'type': '02'}}}
{'packet': {'raw': 'ffffffffffffffffffffffffffffffff004e02000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a', 'type_field': {'insert': {'raw': '200a1e1e1e200a141414200a0a0a0a', 'nlri': ['10.30.30.30/32', '10.20.20.20/32', '10.10.10.10/32']}, 'withdraw': {'raw': '', 'length': '0000', 'nlri': []}, 'attribute': {'origin': 'INCOMPLETE', 'raw': '4001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064', 'next_hop': '10.1.2.2', 'med': 0, 'agg': None, 'local_pref': 100, 'atomic_agg': None, 'as_path': ['2', '222', '223', '224', '225']}}, 'header': {'marker': 'ffffffffffffffffffffffffffffffff', 'data': '000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a', 'length': '004e', 'type': '02'}}}