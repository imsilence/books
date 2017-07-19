#encoding: utf-8

import requests
import socket

if __name__ == '__main__':
    _reponse = requests.get('https://rmccurdy.com/scripts/proxy/good.txt')
    socket.setdefaulttimeout(2)
    for _line in _reponse.text.splitlines():
        _ip, _port = _line.split(':')[:2]
        _client = None
        try:
            _client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _client.connect((_ip, int(_port)))
            print '[+] borker [%s:%s] is ok' % (_ip, _port)
        except BaseException as e:
            pass
            #print '[-] broker [%s:%s] is error' % (_ip, _port)
        finally:
            if _client:
                _client.close()
