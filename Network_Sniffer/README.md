# Basic Network Sniffer Using Python

## Project Overview
This project is a **Basic Network Sniffer** built using Python and the Scapy library. The application captures live network traffic and analyzes packets to extract important details such as source and destination IP addresses, protocol types, port numbers, and payload data.

The project is intended for educational purposes and provides hands-on experience with network packet analysis.

---

## Objectives
- Capture live network packets
- Analyze packet headers and protocol information
- Identify TCP, UDP, and ICMP packets
- Extract source and destination IP addresses
- Display port numbers for TCP and UDP traffic
- Inspect packet payload when available

---

## Tools & Technologies
- Operating System: Linux (Kali Linux / Ubuntu)
- Programming Language: Python 3
- Library: Scapy

---

## Installation & Setup

### Check Python Installation
```bash
python3 --version
```

### Install Scapy
```bash
sudo apt update
sudo apt install python3-scapy -y
```

Verify installation:
```bash
python3 -c "from scapy.all import *; print('Scapy Installed Successfully')"
```

---

## How to Run the Program
 Root privileges are required to capture network packets.

```bash
sudo python3 sniffer.py
```

Generate network traffic by browsing websites or running:
```bash
ping google.com
```

---

## Working of the Sniffer
- The sniffer uses Scapy’s `sniff()` function to capture live packets.
- Each packet is processed by the `packet_analyzer()` function.
- The program checks for the IP layer and extracts:
  - Source IP address
  - Destination IP address
  - Protocol type (TCP, UDP, ICMP)
  - Source and destination port numbers
  - Packet payload (if available)

---

## Sample Output
```
==============================
Source IP       : 192.168.1.10
Destination IP  : 142.250.183.14
Protocol        : TCP
Source Port     : 50322
Destination Port: 443
Payload         : b'...'
```

---

## Screenshots
This project includes screenshots showing:
- Successful Scapy installation
- Execution of the sniffer
- Live packet capture
- Payload analysis

---

## Ethical Considerations
This tool is developed **strictly for educational purposes**.  
Packet sniffing should only be performed on networks where you have explicit permission.

---

## Learning Outcomes
- Understanding of network packet structure
- Practical knowledge of TCP, UDP, and ICMP protocols
- Hands-on experience with live traffic capture
- Improved Python scripting skills
- Awareness of ethical network monitoring

---

## Future Enhancements
- Save captured packets to `.pcap` files
- Implement protocol-based filtering
- Add packet statistics and counters
- Integrate packet visualization tools

---

## Author
Name: Pratham Patil
Role: Cybersecurity Intern  
