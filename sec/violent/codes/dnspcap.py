#encoding: utf-8

from scapy.all import *

def analysis(pkt):
    # _layer = pkt.getlayer(DNSQR)
    # if _layer:
    #     print 'DNSQR: qname:%s, qtype:%s, qclass:%s' % (_layer.qname, _layer.qtype, _layer.qclass)
    _layer = pkt.getlayer(DNSRR)
    if _layer:
        print 'DNSRR: rrname:%s, type:%s, rclass:%s, ttl:%s, rdlen:%s, rdlen:%s' % (_layer.rrname, _layer.type, _layer.rclass, _layer.ttl, _layer.rdlen, len(_layer.rdata))

if __name__ == '__main__':
    for pkt in rdpcap("e:/temp/test.pcap"):
        analysis(pkt)
    #sniff(prn=analysis, store=False)
