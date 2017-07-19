#encoding: utf-8

from scapy.all import *

def call_tsn(target_ip, target_port=139):
    _prev_seq = 0
    _seq = 0
    _offset = 0
    for _ in xrange(5):
        _ans = sr1(IP(dst=target_ip) / TCP(dport=target_port), verbose=0, retry=0, timeout=1)
        if _ans:
            _seq = _ans.getlayer(TCP).seq
            _offset = _seq - _prev_seq
            _prev_seq = _seq
            print '[+] tcp seq offset:%s' % _offset

    return _seq + _offset

if __name__ == '__main__':
    target = '10.18.213.17'
    _seq = call_tsn(target)
    print '[+] next sequence number to ack is:%s' % (_seq)
