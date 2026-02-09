# Network Intrusion Detection System (NIDS) using Snort 3

## Project Overview

A Network Intrusion Detection System (NIDS) is designed to monitor network traffic and detect suspicious or malicious activities.
This project implements a network-based intrusion detection system using **Snort 3 (Snort++)** on Kali Linux.

The system captures live network traffic, applies custom detection rules, and generates alerts when potential attacks such as ICMP ping scans and TCP SYN port scans are detected in real time.

This project is developed as part of a **Cybersecurity Internship / Academic Project** and is suitable for GitHub publication.

---

## Objectives

* Understand the fundamentals of Network Intrusion Detection Systems
* Install and configure Snort 3 on a Linux system
* Write custom Snort rules for detecting network attacks
* Monitor live network traffic
* Detect and analyze intrusion attempts
* Gain hands-on experience in network security and ethical hacking

---

## Tools and Technologies Used

* Operating System: Kali Linux
* Intrusion Detection System: Snort 3 (Snort++)
* Attack Simulation Tools: Nmap, Ping
* Network Interface: eth0
* Configuration Language: Lua

---

## Installation and Setup

### Step 1: Install Snort

```
sudo apt update
sudo apt install snort -y
```

---

### Step 2: Verify Snort Installation

```
snort --version
```

Ensure that Snort 3 is installed successfully.

---

### Step 3: Check Network Interface

```
ip a
```

Ensure that the active network interface is `eth0` and it has an IP address (for example: `10.0.2.x`).

---

## Custom Detection Rules

Custom Snort rules are added in the following file:

```
/etc/snort/rules/local.rules
```

### Rules Implemented

```
alert icmp any any -> 10.0.2.0/24 any (msg:"ICMP Ping Detected"; sid:1000001; rev:1;)
alert tcp any any -> 10.0.2.0/24 any (flags:S; msg:"TCP SYN Scan Detected"; sid:1000002; rev:1;)
```

---

## Rule Explanation

* **ICMP Ping Detected**
  Detects ICMP echo request packets, commonly used for ping scans and host discovery.

* **TCP SYN Scan Detected**
  Detects TCP SYN packets, which are often used in port scanning and reconnaissance attacks.

---

## Configuration Testing

Before running Snort in live mode, the configuration is validated using the following command:

```
sudo snort -T -c /etc/snort/snort.lua
```

Expected output:

```
Snort successfully validated the configuration
```

This confirms that Snort is properly configured and ready to run.

---

## Running Snort (Live Monitoring)

Snort is executed in **console alert mode** to display alerts directly on the terminal:

```
sudo snort -c /etc/snort/snort.lua -i eth0 -A alert_fast
```

Snort will now monitor live network traffic on the `eth0` interface.

---

## Attack Simulation

In a separate terminal window, network attacks are simulated to test the IDS.

### ICMP Ping Test

```
ping 10.0.2.15
```

### TCP SYN Scan Test

```
nmap -sS 10.0.2.15
```

---

## Detection Results

When malicious or suspicious activity is detected, Snort generates real-time alerts on the terminal, such as:

```
[**] ICMP Ping Detected [**]
[**] TCP SYN Scan Detected [**]
```

These alerts confirm that the Network Intrusion Detection System is functioning correctly.

---

## Project Outcome

* Successfully installed and configured Snort 3
* Implemented custom intrusion detection rules
* Detected ICMP ping scans and TCP SYN scans in real time
* Gained practical experience with IDS concepts and tools
* Built a professional cybersecurity internship project

---

## Skills Gained

* Network security fundamentals
* Intrusion Detection Systems (IDS)
* Snort 3 configuration and rule writing
* Network traffic monitoring and analysis
* Ethical hacking basics
* Linux system administration

---

## Future Enhancements

* Automated response by blocking attacker IPs using iptables
* Alert logging and analysis
* Visualization of detected attacks using graphs or dashboards
* Integration with SIEM tools

---

## Resume Description

Developed a Network Intrusion Detection System using Snort 3 to monitor live network traffic and detect ICMP and TCP SYN scan attacks through custom rules. Successfully configured, tested, and deployed real-time intrusion detection in a Linux environment.

---

## Author

Name: Pratham Patil
Role: Cybersecurity Intern

