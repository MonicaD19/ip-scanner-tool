IP Scanner Tool

*Description*
This repository contains a simple Python-based IP scanner tool for scanning a range of ports on a given IP address. It includes three types of scanning techniques:

- Basic TCP Scanner: A simple scanner using sockets.
- Multithreaded TCP Scanner: A faster version of the TCP scanner using Python’s threading module.
- Advanced SYN Scanner: A more advanced scanner using Scapy to perform SYN scans.
Each script is designed to be easy to understand, use, and modify. This tool is particularly useful for penetration testing and network auditing.

*Features*
Basic TCP Scanner: Performs port scans on a given IP address for a specified range of ports.
Multithreaded TCP Scanner: Performs concurrent scans to speed up the scanning process.
Advanced SYN Scanner: Uses Scapy to perform SYN scans for a more accurate and stealthy port scan.
Scripts Overview

*basic_ip_scanner.py*
This script performs a basic TCP port scan using the socket library. It takes a target IP address and port range as input, then checks whether each port is open or closed.

Usage:
- The user is prompted to enter the target IP and port range.
For each port, the script attempts to establish a TCP connection and reports whether the port is open or closed.
# Example:
Enter target IP: 192.168.1.1
Enter port range (e.g., 20-80): 20-80
The script will check all ports from 20 to 80 on the target IP and display the results.

*threaded_ip_scanner.py*
This script enhances the basic scanner by using multithreading to run multiple port scans concurrently, making the process faster. Each port scan runs in a separate thread.

Usage:
- Similar to the basic scanner, the user inputs the target IP and port range.
The script spawns a thread for each port, improving the scan's speed.
# Example:
Enter target IP: 192.168.1.1
Enter port range (e.g., 20-80): 20-80
The results will be displayed faster compared to the basic scanner.

*scapy_ip_scanner.py*
This script performs an advanced SYN scan using Scapy. SYN scans are more stealthy and precise because they only send a SYN packet to initiate a connection without completing the handshake.

Usage:
The user is prompted to enter the target IP and port range.
The script sends a SYN packet to each port, analyzing the response to determine whether the port is open or closed.
# Example:
Enter target IP: 192.168.1.1
Enter port range (e.g., 20-80): 20-80
Results will show whether the port responded to the SYN packet, indicating it is open.

Note: This script requires root privileges to run since it uses raw packets.

Requirements
Python 3.x
Scapy (for the advanced SYN scanner)

## Install Scapy
To install Scapy, run:

pip3 install scapy

## Setup Guide
- Step 1: Clone the Repository
Clone this repository to your local machine using git:


git clone https://github.com/yourusername/ip_scanner_tool.git
cd ip_scanner_tool

- Step 2: Install Dependencies
For the advanced scanner, you need to install the Scapy library:

pip3 install scapy

- Step 3: Run the Scripts
3.1 Basic TCP Scanner

# Run the basic scanner:

python3 basic_ip_scanner.py
You will be prompted to enter the target IP and port range.

3.2 Multithreaded TCP Scanner
# Run the multithreaded scanner:

python3 threaded_ip_scanner.py
Again, you will be prompted to enter the target IP and port range.

3.3 Advanced SYN Scanner (Scapy-based)
# Run the Scapy-based SYN scanner (requires root privileges):

sudo python3 scapy_ip_scanner.py
This will also prompt you for the target IP and port range.

Usage Examples
Here’s an example of how to use each scanner:

## Basic TCP Scanner Example:
python3 basic_ip_scanner.py
Enter target IP: 192.168.1.1
Enter port range (e.g., 20-80): 20-80
You will see output like:

Port 20 on 192.168.1.1 is closed.
Port 21 on 192.168.1.1 is open.
Port 22 on 192.168.1.1 is open.
...

## Multithreaded TCP Scanner Example:
python3 threaded_ip_scanner.py
Enter target IP: 192.168.1.1
Enter port range (e.g., 20-80): 20-80
Output will be similar to the basic scanner, but results will appear faster due to multithreading.

## Advanced SYN Scanner Example:
sudo python3 scapy_ip_scanner.py
Enter target IP: 192.168.1.1
Enter port range (e.g., 20-80): 20-80
Output:

Port 22 on 192.168.1.1 is open.
Port 80 on 192.168.1.1 is open.
...

# Contributing
If you would like to contribute to this project, feel free to fork the repository, create a feature branch, and submit a pull request.
