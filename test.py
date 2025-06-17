from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *


# store = {'client_key': '22258343646e5169fe976e6b4562ef9e'}
# client = WebOSClient.discover()[0]
# client.connect()

# for status in client.register(store):
#     if status == WebOSClient.PROMPTED:
#         print("Please accept")
#     elif status == WebOSClient.REGISTERED:
#         print("REg successful")
        
# print(store)



# import time
# from wakeonlan import send_magic_packet

# store = {'client_key': 'bd6b621e59cd9f6cde153e30190b1847'}


# MAC = "44-CB-8B-2B-7E-DC"
# IP = "192.168.1.35"

# send_magic_packet(MAC)
# client = WebOSClient(IP)
# client.connect()
# for status in client.register(store):
#     if status == WebOSClient.PROMPTED:
#         print("PLease accept")
#     elif status == WebOSClient.REGISTERED:
#         print("Registered successfully")

# time.sleep(15)

# system = SystemControl(client)
# system.notify("This is a notify msg", icon_ext="png")
from scapy.all import ARP, Ether, srp
import socket

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        hostname = get_hostname(ip)
        devices.append({'ip': ip, 'mac': mac, 'hostname': hostname})

    return devices

# Example: Scan 192.168.1.x range (change if needed)
devices = scan_network("192.168.1.0/24")
print("Connected Devices:\n")
for device in devices:
    print(f"IP: {device['ip']}\tMAC: {device['mac']}\tHostname: {device['hostname']}")
