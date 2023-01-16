#!/usr/local/bin/python3.9/site-packages/
import nmap


nmap_path = []
scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<--------------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of the scan you want to run
             1)SYN ACK Scan
             2)UDP Scan
             3)Comprehensive Scan""")

print("You have selected option: ", resp)
if resp == '1':
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v-sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols)
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v-sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols)
    print("Open Ports: ", scanner[ip_addr]['ucp'].keys())
elif resp == '3':
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v-sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols)
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
else:
    please("Please enter a valid option")