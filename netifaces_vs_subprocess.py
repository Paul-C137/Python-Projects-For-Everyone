import netifaces
import subprocess
import re

def get_interfaces_netifaces():
    """Retrieve network interface info using netifaces library."""
    interfaces_info = {}
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        interface_info = {
            'ipv4': addrs.get(netifaces.AF_INET, [{}])[0].get('addr', None),
            'ipv6': addrs.get(netifaces.AF_INET6, [{}])[0].get('addr', None),
            'mac': addrs.get(netifaces.AF_LINK, [{}])[0].get('addr', None)
        }
        interfaces_info[interface] = interface_info
    return interfaces_info

def get_interfaces_ip_a():
    """Retrieve network interface info using `ip a` shell command."""
    interfaces_info = {}
    try:
        output = subprocess.check_output(['ip', 'a']).decode('utf-8')
        interfaces = re.split(r'\d+:\s', output)[1:]
        for iface in interfaces:
            lines = iface.split('\n')
            interface_name = lines[0].split(':')[0]
            interface_info = {'ipv4': None, 'ipv6': None, 'mac': None}
            
            for line in lines:
                if 'inet ' in line and not 'inet6' in line:
                    interface_info['ipv4'] = line.split()[1].split('/')[0]
                elif 'inet6 ' in line:
                    interface_info['ipv6'] = line.split()[1].split('/')[0]
                elif 'link/ether ' in line:
                    interface_info['mac'] = line.split()[1]
            
            interfaces_info[interface_name] = interface_info
    except subprocess.CalledProcessError as e:
        print(f"Error executing ip command: {e}")
    return interfaces_info

# Test the functions
if __name__ == "__main__":
    print("Using netifaces:")
    print(get_interfaces_netifaces())
    
    print("\nUsing ip a command:")
    print(get_interfaces_ip_a())
