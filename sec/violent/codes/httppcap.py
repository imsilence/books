#encoding: utf-8
import socket

import dpkt

def unpack_pcap(path):
    _fhandler = open(path, 'rb')
    _reader = dpkt.pcap.Reader(_fhandler)
    for _ts, _buffer in _reader:
        try:
            _eth = dpkt.ethernet.Ethernet(_buffer)
            _ip = _eth.data
            _src = socket.inet_ntoa(_ip.src)
            _dst = socket.inet_ntoa(_ip.dst)
            _tcp = _ip.data
            _http = dpkt.http.Request(_tcp.data)
            if _http.method == 'GET':
                if '.zip' in _http.uri.lower():
                    print '%s(%s) => %s(%s)[%s]' % (_src, _tcp.sport, _dst, _tcp.dport, _http.uri)
                    print _tcp.data
        except BaseException as e:
            #print str(e)
            pass
    _fhandler.close()


if __name__ == '__main__':
    unpack_pcap('e:/temp/http.pcap')
