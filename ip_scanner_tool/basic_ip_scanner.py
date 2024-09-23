import socket

def scan_ip(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port} on {ip} is open.")
        else:
            print(f"Port {port} on {ip} is closed.")
        sock.close()
    except socket.error as err:
        print(f"Error scanning {ip}: {err}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    port_range = input("Enter port range (e.g., 20-80): ")
    
    start_port, end_port = map(int, port_range.split('-'))
    
    for port in range(start_port, end_port + 1):
        scan_ip(target_ip, port)
