import sys

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

def validate_arguments():
	args = sys.argv[1:]

	if (not arg_count_valid(args)):
		print_usage("Wrong argument count!")
		sys.exit()

	args_dict = {}
	#args_dict["src_mac": arg]