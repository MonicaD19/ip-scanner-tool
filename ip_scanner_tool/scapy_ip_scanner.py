from scapy.all import sr1, IP, TCP

def syn_scan(ip, port):
    packet = IP(dst=ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)
    
    if response and response.haslayer(TCP):
        if response[TCP].flags == "SA":
            print(f"Port {port} on {ip} is open.")
        elif response[TCP].flags == "RA":
            print(f"Port {port} on {ip} is closed.")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    port_range = input("Enter port range (e.g., 20-80): ")
    
    start_port, end_port = map(int, port_range.split('-'))
    
    for port in range(start_port, end_port + 1):
        syn_scan(target_ip, port)
