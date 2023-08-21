#!/usr/bin/env python3

import netifaces

def get_ipv6_addresses(interface):
    addresses = netifaces.ifaddresses(interface).get(netifaces.AF_INET6, [])
    ipv6_addresses = []
    
    for address_info in addresses:
        for addr in address_info.get('addr', []):
            ipv6_addresses.append(addr)
            
    return ipv6_addresses

def main():
    print("Available network interfaces:")
    interfaces = netifaces.interfaces()
    print(interfaces)
    
    for interface in interfaces:
        end_to_remove = len(interface) + 1
        print('\n********Details of Interface - ' + interface + ' ************')
        
        if netifaces.AF_LINK in netifaces.ifaddresses(interface):
            print("MAC address:", (netifaces.ifaddresses(interface)[netifaces.AF_LINK])[0]['addr'])
        
        if netifaces.AF_INET in netifaces.ifaddresses(interface):
            print("IPv4 address:", (netifaces.ifaddresses(interface)[netifaces.AF_INET])[0]['addr'])
        
        ipv6_addresses = get_ipv6_addresses(interface)
        if ipv6_addresses:
            print("IPv6 addresses:", ''.join(ipv6_addresses)[0:-end_to_remove])
        else:
            print("No IPv6 addresses found.")

if __name__ == "__main__":
    main()
