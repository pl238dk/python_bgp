## capability codes
#	0	Reserved	[RFC5492]
#	1	Multiprotocol Extensions for BGP-4	[RFC2858]
#	2	Route Refresh Capability for BGP-4	[RFC2918]
#	3	Outbound Route Filtering Capability	[RFC5291]
#	4	Multiple routes to a destination capability (deprecated)	[RFC8277]
#	5	Extended Next Hop Encoding	[RFC5549]
#	6	BGP-Extended Message (TEMPORARY - registered 2015-09-30, extension registered 2017-08-31, expires 2018-09-30)	[draft-ietf-idr-bgp-extended-messages]
#	7	BGPsec Capability	[RFC8205]
#	8	Multiple Labels Capability	[RFC8277]
#	9-63	Unassigned	
#	64	Graceful Restart Capability	[RFC4724]
#	65	Support for 4-octet AS number capability	[RFC6793]
#	66	Deprecated (2003-03-06)	
#	67	Support for Dynamic Capability (capability specific)	[draft-ietf-idr-dynamic-cap]
#	68	Multisession BGP Capability	[draft-ietf-idr-bgp-multisession]
#	69	ADD-PATH Capability	[RFC7911]
#	70	Enhanced Route Refresh Capability	[RFC7313]
#	71	Long-Lived Graceful Restart (LLGR) Capability	[draft-uttaro-idr-bgp-persistence]
#	72	Unassigned	
#	73	FQDN Capability	[draft-walton-bgp-hostname-capability]
#	74-127	Unassigned	
#	128-255	Reserved for Private Use	[RFC5492]

## AFI codes [RFC 1700]
#Number    Description                                          Reference
#------    ---------------------------------------------------- ---------
#     0    Reserved
#     1    IP (IP version 4)
#     2    IP6 (IP version 6)
#     3    NSAP
#     4    HDLC (8-bit multidrop)
#     5    BBN 1822
#     6    802 (includes all 802 media plus Ethernet "canonical format")
#     7    E.163
#     8    E.164 (SMDS, Frame Relay, ATM)
#     9    F.69 (Telex)
#    10    X.121 (X.25, Frame Relay)
#    11    IPX
#    12    Appletalk
#    13    Decnet IV
#    14    Banyan Vines
# 65535    Reserved

## SAFI codes
#	0	Reserved	[RFC4760]
#	1	Network Layer Reachability Information used for unicast forwarding	[RFC4760]
#	2	Network Layer Reachability Information used for multicast forwarding	[RFC4760]
#	3	Reserved	[RFC4760]
#	4	Network Layer Reachability Information (NLRI) with MPLS Labels	[RFC8277]
#	5	MCAST-VPN	[RFC6514]
#	6	Network Layer Reachability Information used for Dynamic Placement of Multi-Segment Pseudowires	[RFC7267]
#	7	Encapsulation SAFI	[RFC5512]
#	8	MCAST-VPLS	[RFC7117]
#	9-63	Unassigned	
#	64	Tunnel SAFI	[Gargi_Nalawade][draft-nalawade-kapoor-tunnel-safi-01]
#	65	Virtual Private LAN Service (VPLS)	[RFC4761][RFC6074]
#	66	BGP MDT SAFI	[RFC6037]
#	67	BGP 4over6 SAFI	[RFC5747]
#	68	BGP 6over4 SAFI	[Yong_Cui]
#	69	Layer-1 VPN auto-discovery information	[RFC5195]
#	70	BGP EVPNs	[RFC7432]
#	71	BGP-LS	[RFC7752]
#	72	BGP-LS-VPN	[RFC7752]
#	73	SR TE Policy SAFI	[draft-previdi-idr-segment-routing-te-policy]
#	74-127	Unassigned	
#	128	MPLS-labeled VPN address	[RFC4364][RFC8277]
#	129	Multicast for BGP/MPLS IP Virtual Private Networks (VPNs)	[RFC6513][RFC6514]
#	130-131	Reserved	[RFC4760]
#	132	Route Target constrains	[RFC4684]
#	133	IPv4 dissemination of flow specification rules	[RFC5575]
#	134	VPNv4 dissemination of flow specification rules	[RFC5575]
#	135-139	Reserved	[RFC4760]
#	140	VPN auto-discovery	[draft-ietf-l3vpn-bgpvpn-auto]
#	141-240	Reserved	[RFC4760]
#	241-254	Reserved for Private Use	[RFC4760]
#	255	Reserved	[RFC4760]