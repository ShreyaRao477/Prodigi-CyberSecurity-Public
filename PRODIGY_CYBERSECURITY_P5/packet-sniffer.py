import os
import sys
from scapy.all import *
import matplotlib.pyplot as plt
from collections import Counter
import time

print("------------------------ Packet Sniffer Tool Disclaimer ---------------------------")
print("This packet sniffer tool is intended for educational and ethical purposes only.")
print("Unauthorized use, distribution, or modification of this tool is strictly prohibited.")
print("By using this tool, you agree to the following terms and conditions:")
print("\n1. You will only use this tool on networks and systems for which you have explicit permission.")
print("2. You will not use this tool to violate any laws, regulations, or terms of service.")
print("3. You will not use this tool to harm, disrupt, or exploit any networks or systems.")
print("4. You will not use this tool to intercept, collect, or store any sensitive or confidential information.")
print("5. You will not redistribute or sell this tool without the express permission of the author.")
print("6. The author is not responsible for any damages or losses incurred as a result of using this tool.")
print("7. You will respect the privacy and security of all networks and systems you interact with using this tool.")

accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")

if accept_terms.lower() != 'y':
    print("You must accept the terms and conditions before using this tool.")
    sys.exit()

print("\n--------------- Packet Sniffing Tool ---------------")

packet_data = {"src_ip": [], "src_port": [], "protocol": []}

def packet_type(packet):
    if packet.haslayer(TCP):
        return 'TCP'
    elif packet.haslayer(UDP):
        return 'UDP'
    else:
        return 'Other'

def packet_sniff(packet, filter_protocol):
    protocol = packet_type(packet)
    
    if (filter_protocol == 'TCP' and protocol == 'TCP') or (filter_protocol == 'UDP' and protocol == 'UDP') or filter_protocol == 'Both':
        src_ip = packet[IP].src
        src_port = packet.sport if protocol == 'TCP' else packet[UDP].sport

        packet_data["src_ip"].append(src_ip)
        packet_data["src_port"].append(src_port)
        packet_data["protocol"].append(protocol)

        output_string = f"Protocol: {protocol}\n"
        output_string += f"Source IP: {src_ip}\n"
        output_string += f"Source Port: {src_port}\n"
        output_string += f"Payload: {str(packet.payload)[:50]}...\n"

        print(output_string, end='')

        with open('packet_sniffer_results.txt', 'a') as f:
            f.write(output_string)

output_file = "packet_sniffer_results.txt"

def choose_protocol():
    print("\nSelect packet protocol to sniff:")
    print("1. TCP")
    print("2. UDP")
    print("3. Both TCP and UDP")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        return 'TCP'
    elif choice == '2':
        return 'UDP'
    elif choice == '3':
        return 'Both'
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return choose_protocol()

def get_sniffing_duration():
    try:
        duration = int(input("\nEnter duration for sniffing in seconds (default is 100): ").strip())
        return duration if duration > 0 else 100
    except ValueError:
        return 100

def start_sniffing(protocol_choice, duration):
    if protocol_choice == 'TCP':
        sniff(filter="tcp", prn=lambda packet: packet_sniff(packet, protocol_choice), store=0, count=0, timeout=duration)
    elif protocol_choice == 'UDP':
        sniff(filter="udp", prn=lambda packet: packet_sniff(packet, protocol_choice), store=0, count=0, timeout=duration)
    else:
        sniff(filter="ip", prn=lambda packet: packet_sniff(packet, protocol_choice), store=0, count=0, timeout=duration)

def plot_packet_data():
    ip_counter = Counter(packet_data["src_ip"])
    port_counter = Counter(packet_data["src_port"])
    protocol_counter = Counter(packet_data["protocol"])

    plt.figure(figsize=(10, 6))
    plt.bar(ip_counter.keys(), ip_counter.values(), color='b')
    plt.xlabel('Source IP')
    plt.ylabel('Packet Count')
    plt.title('Packet Count by Source IP')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(port_counter.keys(), port_counter.values(), color='g')
    plt.xlabel('Source Port')
    plt.ylabel('Packet Count')
    plt.title('Packet Count by Source Port')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(protocol_counter.keys(), protocol_counter.values(), color='r')
    plt.xlabel('Protocol')
    plt.ylabel('Packet Count')
    plt.title('Packet Count by Protocol (TCP/UDP)')
    plt.tight_layout()
    plt.show()

def user_menu():
    print("\nChoose an option:")
    print("1. View graphical data")
    print("2. View text file data")
    print("3. Start new sniffing")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == '1':
        plot_packet_data()
    elif choice == '2':
        with open(output_file, "r") as file:
            print("\n--- Packet Sniffer Results ---")
            print(file.read())
    elif choice == '3':
        print("Starting new sniffing session...\n")
        main()
    elif choice == '4':
        print("Exiting the tool. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        user_menu()

def main():
    protocol_choice = choose_protocol()
    duration = get_sniffing_duration()
    
    print(f"\nSniffing started for {duration} seconds, capturing {protocol_choice} packets...\n")
    
    start_sniffing(protocol_choice, duration)

    print(f"\nResults saved to: {output_file}")
    
    user_menu()

if __name__ == "__main__":
    main()
