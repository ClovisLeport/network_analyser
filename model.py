from scapy.all import sniff
import socket
import subprocess
import ipaddress
from device import Device
from network import Network

import scapy.all as scapy

class Model:

    def get_devices():
        ca = sniff(iface = 'Wi-Fi',count= 5)
        request = scapy.ARP()
        network=Network()
        request.pdst = str(network.ip)+"/"+str(network.mask)
        broadcast = scapy.Ether()
        broadcast.dst = 'ff:ff:ff:ff:ff:ff'
        hostname = socket.gethostname() 
        IPAddr = socket.gethostbyname(hostname)
        request_broadcast = broadcast / request
        clients = scapy.srp(request_broadcast, timeout = 1)[0]
        devices = []

        for device in clients:
            ip=str(device[1].psrc)
            mac_address = str(device[1].hwsrc)
            device_name = str(socket.getfqdn(ip))
            device_name = device_name if device_name.count(".") == 0 else "NaN"
            if ip[-1]=="1" and ip[-2] == ".": device_name = "Router"
            device = Device(ip, mac_address, device_name)
            devices.append(device)
            print(ip,mac_address, device_name)

        return devices

