import logging
logging.getLogger("scapy").setLevel(logging.CRITICAL)
from scapy.all import *
import ipaddress
import warnings
import time
import crayons

ports = [25,80,53,443,445,8080,8443]

def is_device_present(ip):
    arp_request = ARP(pdst=ip)
    response = sr1(arp_request, timeout=5, verbose=0)
    return response is not None

def syn_scan_list(host):
	open_ports = []  # Initialize a list to store open ports
	ans, unans = sr(
		IP(dst=host) /
		TCP(sport=33333, dport=ports, flags='S'),
		timeout=2,
		verbose=0
	)
	for (s, r) in ans:
		if s[TCP].dport == r[TCP].sport and r[TCP].flags == 'SA':
			open_ports.append(s[TCP].dport)  # Append open port to the list
	return open_ports  # Return the list of open ports

def main():
	device = 1
	while device <= 255:
		host = f'192.168.222.{device}'
		try:
			# raise ValueError if the argument passed is not a valid ip address
			ipaddress.ip_address(host)
		except:
			print('Invalid address')
			exit(-1)
		# Check if the device is present
		if is_device_present(host):
			source = syn_scan_list(host)
			if source:  # Ensure that 'source' is valid before trying to print
				try:
					print(crayons.green(f'\nOpen ports at {host}:  '), end='')
					print(crayons.green(source), end='')
				except TypeError:
					continue
			else:
				print(crayons.yellow(f'\nNo response from {host}, skipping scan'), end='')
		else:
			print(crayons.red(f'\nNo host found at {host}'), end='')
		device += 1
		#time.sleep(1)
	
main()