#encoding: utf-8

from scapy.all import *

def analysis(pkt):
    _layer = pkt.getlayer(DNSRR)
    if _layer:
        return _layer.rrname, _layer.rdata
    return None, None

if __name__ == '__main__':
    _pkts = rdpcap("e:/temp/dns.pcap")
    _cached = {}
    for _pkt in _pkts:
        _rrname, _rdata = analysis(_pkt)
        if _rrname:
            _values = _cached.get(_rrname, [])
            if _rdata not in _values:
                _values.append(_rdata)
            _cached[_rrname] = _values

    for _rrname, _values in _cached.items():
        print '[+] %s has %s unique IPs' % (_rrname, len(_values))
    #sniff(prn=analysis, store=False)
