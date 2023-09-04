'''This program sends an ARP broadcast and returns the IP and MAC address
   for all the devices that respond.'''
# Import the necessary Scapy module
import scapy.all as scapy

# Create an ARP packet
request = scapy.ARP()

# Set the target IP range to scan (CIDR notation)
# Change to match your network, if necessary.
request.pdst = '192.168.0.1/24'

# Create an Ethernet frame (broadcast)
broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff'  # MAC address for broadcast

# Combine the Ethernet frame and ARP packet
request_broadcast = broadcast / request

# Send ARP requests and receive responses
# srp() returns a list of (sent_packet, received_packet) pairs
# Timeout set to 10 seconds, and verbose mode enabled (verbose = 1)
clients = scapy.srp(request_broadcast, timeout=10, verbose=1)[0]

# Loop through the received packets and extract IP and MAC addresses
for element in clients:
    ip_address = element[1].psrc  # Source IP address (target's IP)
    mac_address = element[1].hwsrc  # Source MAC address (target's MAC)
    print(f"IP Address: {ip_address}\tMAC Address: {mac_address}")
