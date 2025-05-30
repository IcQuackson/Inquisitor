import sys
import re
import ipaddress
from ipaddress import AddressValueError

def print_usage(error_msg):
	if error_msg:
		print(error_msg)
	print("Usage: 	inquisitor <IP-src> <MAC-src> <IP-target> <MAC-target>")
	print()
	print("Arguments:")
	print("  <IP-src>      The IP address you are pretending to be (spoofed IP, usually the target's IP).")
	print("  <MAC-src>     The MAC address you want to associate with <IP-src> (usually the attacker's MAC).")
	print("  <IP-target>   The IP address of the victim (the device whose ARP cache you're poisoning).")
	print("  <MAC-target>  The MAC address of the victim (to properly address the Ethernet frame).")
	print()
	print("Example:")
	print("  python3 poison.py 172.16.238.30 02:aa:bb:cc:dd:10 172.16.238.20 02:42:ac:00:00:bb")
	

def arg_count_valid(args):
	return len(args) == 4

def mac_is_valid(mac):
	return re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower())

def ip_is_valid(ip):
	try:
		ipaddress.IPv4Address(ip)
		return True
	except AddressValueError as e:
		print("IPv4 address not valid! " + str(e))
	return False


def parse_arguments(args):

	if not arg_count_valid(args):
		print_usage("Wrong argument count!")
		sys.exit()

	arg_labels = ["ip_src", "mac_src", "ip_target", "mac_target"]
	args = dict(zip(arg_labels, args))

	if not (mac_is_valid(args["mac_src"]) and mac_is_valid(args["mac_target"])):
		print("MAC address not valid!")
		sys.exit()
	
	if not (ip_is_valid(args["ip_src"]) and ip_is_valid(args["ip_target"])):
		sys.exit()

	return args