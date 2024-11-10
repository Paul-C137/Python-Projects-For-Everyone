from scapy.all import *
import ipaddress
import warnings

# Suppress ARP warning related to missing MAC address
#warnings.filterwarnings("ignore")

ports = [25,80,53,443,445,8080,8443]

def is_device_present(ip):
    arp_request = ARP(pdst=ip)
    response = sr1(arp_request, timeout=1, verbose=0)
    return response is not None

def syn_scan(host):
	ans, unans = sr(
		IP(dst=host)/
		TCP(sport=33333, dport=ports, flags='S'), 
		timeout=2, 
		verbose=0)
	print(f'Open ports at {host}:')
	for (s,r) in ans:
		if s[TCP].dport == r[TCP].sport and r[TCP].flags == 'SA':
			return s

def main():
	device = 0
	while device <= 255:
		device += 1
		host = f'192.168.222.{device}'
		try:
			# raise ValueError if the argument passed is not a valid ip address
			ipaddress.ip_address(host)
		except:
			print('Invalid address.')
			exit(-1)
		# Check if the device is present
		with warnings.catch_warnings():
		    if is_device_present(host):
			    source = syn_scan(host)
			    if source:  # Ensure that 'source' is valid before trying to print
				    try:
					    print(source[TCP].dport)
				    except TypeError:
					    continue
		    else:
			    print(f"No response from {host}, skipping scan.")


main()