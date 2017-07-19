#encoding: utf-8
import socket

import dpkt
import geoip2.database

def ip2geo(ip):
    _reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    _geo = None
    try:
        _geo = _reader.city(ip)
    except BaseException as e:
        pass
    _reader.close()
    return _geo

def unpack_pcap(path):
    _fhandler = open(path, 'rb')
    _reader = dpkt.pcap.Reader(_fhandler)
    for _ts, _buffer in _reader:
        try:
            _eth = dpkt.ethernet.Ethernet(_buffer)
            _ip = _eth.data
            _src = socket.inet_ntoa(_ip.src)
            _dst = socket.inet_ntoa(_ip.dst)
            _src_geo = ip2geo(_src)
            _prints = []
            _prints.append('[+] %s' % _src)
            if _src_geo:
                _prints.append('(%s, %s)' % (_src_geo.city.name, _src_geo.country.name))
            _prints.append(' => %s' % _dst)
            _dst_geo = ip2geo(_dst)
            if _dst_geo:
                _prints.append('(%s, %s)' % (_dst_geo.city.name, _dst_geo.country.name))
            print ''.join(_prints)

        except BaseException as e:
            #print str(e)
            pass
    _fhandler.close()


if __name__ == '__main__':
    unpack_pcap('e:/temp/test.pcap')
