from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_analyzer(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print("\n==============================")
        print(f"Source IP       : {src_ip}")
        print(f"Destination IP  : {dst_ip}")

        if TCP in packet:
            print("Protocol        : TCP")
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print("Protocol        : UDP")
            print(f"Source Port     : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif ICMP in packet:
            print("Protocol        : ICMP")

        # Payload analysis
        if packet.haslayer(Raw):
            print(f"Payload         : {packet[Raw].load}")

sniff(prn=packet_analyzer, store=False)
