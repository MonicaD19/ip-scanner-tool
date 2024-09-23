import socket
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port} on {ip} is open.")
        sock.close()
    except socket.error:
        pass

def scan_ip(ip, start_port, end_port):
    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    port_range = input("Enter port range (e.g., 20-80): ")
    
    start_port, end_port = map(int, port_range.split('-'))
    scan_ip(target_ip, start_port, end_port)
