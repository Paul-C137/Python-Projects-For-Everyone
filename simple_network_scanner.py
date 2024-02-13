import networkx as nx
import matplotlib.pyplot as plt
import nmap

def scan_network(ip_range):
    """
    Scan the network using nmap and return a list of devices and their IP addresses.
    """
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')  # Use nmap to scan the network
    
    devices = []
    for host in nm.all_hosts():
        device = {
            'ip': host,
            'hostname': nm[host].hostname(),
            'mac_address': nm[host]['addresses']['mac'],  # Optional: Retrieve MAC address
            # Add more information as needed
        }
        devices.append(device)
    return devices

def create_network_graph(devices):
    """
    Create a NetworkX graph representing the network topology.
    """
    G = nx.Graph()
    for device in devices:
        G.add_node(device['hostname'], ip=device['ip'], mac=device['mac_address'])
        # Add more attributes as needed
        
    # Optionally, you can add edges between devices based on network connections
    
    return G

def main():
    # Scan your network
    ip_range = '192.168.1.0/24'  # Example IP range, adjust to your network
    devices = scan_network(ip_range)
    
    # Create a network graph
    G = create_network_graph(devices)
    
    # Specify layout for the graph
    pos = nx.spring_layout(G)
    
    # Visualize the network graph
    nx.draw(G, pos, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()
