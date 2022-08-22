# BGP Peer

Create and establish a peer session with a BGP router. Only participates enough to receive NLRI updates and withdrawals.

Schema (current):
- main.py and main-Thread.py both establish a TCP session with a BGP neighbor.
  - each TCP session instantiates a class from bgp.py to handle the underlying BGP protocol communication.
    - each packet received is queued and processed according to an instantiated class from bgp_packet.py.
    - when a BGP 'UPDATE' message is received, the reachability information (NLRI) is written to a database.
      - advertised NLRIs are marked as active
      - withdrawn NLRIs are marked as inactive
- database stores information about the NEXT_HOP, activity state, and NLRI.
- web frontend simply reads the database and pulls information statically from each page load.


Output :
```python
{
'packet':
	{
	'raw': 'ffffffffffffffffffffffffffffffff002d01040001000f070707071002060104000100010202800002020200',
	'type_field':
		{
		'as': '0001',
		'version': '04',
		'optional':
			{
			'capability':
				[
				'Multi-Protocol Extensions - IPv4,Unicast',
				'Route-Refresh - Cisco',
				'Route-Refresh'
				],
			'raw': '02060104000100010202800002020200',
			'length': '10',
			'auth': None
			},
		'hold': '000f',
		'id': '07070707'
		}, 
	'header':
		{
		'marker': 'ffffffffffffffffffffffffffffffff',
		'data': '040001000f070707071002060104000100010202800002020200',
		'length': '002d',
		'type': '01'
		}
	}
}
{
'packet':
	{
	'raw': 'ffffffffffffffffffffffffffffffff005e020000001c40010102400200400304033b00818004040000000040050400000064180a0102200707070720060606062005050505200404040418033b00200303030320020202022001010101',
	'type_field':
		{
		'insert':
			{
			'raw': '180a0102200707070720060606062005050505200404040418033b00200303030320020202022001010101',
			'nlri':
				[
				'10.1.2/24',
				'7.7.7.7/32',
				'6.6.6.6/32',
				'5.5.5.5/32',
				'4.4.4.4/32',
				'3.59.0/24',
				'3.3.3.3/32',
				'2.2.2.2/32',
				'1.1.1.1/32'
				]
			},
		'withdraw':
			{
			'raw': '',
			'length': '0000',
			'nlri':
				[
				]
			},
		'attribute':
			{
			'origin': 'INCOMPLETE',
			'raw': '40010102400200400304033b00818004040000000040050400000064',
			'next_hop': '3.59.0.129',
			'med': 0,
			'agg': None,
			'local_pref': 100,
			'atomic_agg': None,
			'as_path':
				[
				]
			}
		},
	'header':
		{
		'marker': 'ffffffffffffffffffffffffffffffff',
		'data': '0000001c40010102400200400304033b00818004040000000040050400000064180a0102200707070720060606062005050505200404040418033b00200303030320020202022001010101',
		'length': '005e',
		'type': '02'
		}
	}
}
{
'packet':
	{
	'raw': 'ffffffffffffffffffffffffffffffff003c020000002040010102400204020100024003040a0102028004040000000040050400000064200a282828',
	'type_field':
		{
		'insert':
			{
			'raw': '200a282828',
			'nlri':
				[
				'10.40.40.40/32'
				]
			},
		'withdraw':
			{
			'raw': '',
			'length': '0000',
			'nlri':
				[
				]
			},
		'attribute':
			{
			'origin': 'INCOMPLETE',
			'raw': '40010102400204020100024003040a0102028004040000000040050400000064',
			'next_hop': '10.1.2.2',
			'med': 0,
			'agg': None,
			'local_pref': 100,
			'atomic_agg': None,
			'as_path':
				[
				'2'
				]
			}
		},
	'header':
		{
		'marker': 'ffffffffffffffffffffffffffffffff',
		'data': '0000002040010102400204020100024003040a0102028004040000000040050400000064200a282828',
		'length': '003c',
		'type': '02'
		}
	}
}
{
'packet':
	{
	'raw': 'ffffffffffffffffffffffffffffffff004e02000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a',
	'type_field':
		{
		'insert':
			{
			'raw': '200a1e1e1e200a141414200a0a0a0a',
			'nlri':
				[
				'10.30.30.30/32',
				'10.20.20.20/32',
				'10.10.10.10/32'
				]
			},
		'withdraw':
			{
			'raw': '',
			'length': '0000',
			'nlri':
				[
				]
			},
		'attribute':
			{
			'origin': 'INCOMPLETE',
			'raw': '4001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064',
			'next_hop': '10.1.2.2',
			'med': 0,
			'agg': None,
			'local_pref': 100,
			'atomic_agg': None,
			'as_path':
				[
				'2',
				'222',
				'223',
				'224',
				'225'
				]
			}
		},
	'header':
		{
		'marker': 'ffffffffffffffffffffffffffffffff',
		'data': '000000284001010240020c0205000200de00df00e000e14003040a0102028004040000000040050400000064200a1e1e1e200a141414200a0a0a0a',
		'length': '004e',
		'type': '02'
		}
	}
}
```