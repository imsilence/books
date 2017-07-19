#encoding: utf-8
import math

from scapy.all import *
import IPy

TTL_ABS = 5

ICMP_TTL_CACHED = {}

def ttl(pkt):
    _ip = pkt.getlayer(IP)
    if _ip and IPy.IP(_ip.src).iptype() == 'PUBLIC':
        _ttl = ICMP_TTL_CACHED.get(_ip.src)
        if _ttl is None:
            _icmp_pkt = sr1(IP(dst=_ip.src) / ICMP(), timeout=1, verbose=0, retry=0)
            _ttl = _icmp_pkt.ttl if _icmp_pkt else None
            ICMP_TTL_CACHED[_ip.src] = _ttl

        if _ttl is None or math.fabs(_ttl - pkt.ttl) > TTL_ABS:
            print '[-] ip:%s, ttl:%s, icmp ttl:%s' % (_ip.src, pkt.ttl, _ttl)


if __name__ == '__main__':
    sniff(prn=ttl, store=False)
