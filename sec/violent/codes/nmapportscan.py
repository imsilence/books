#encoding: utf-8
import logging
import argparse
import colorama
import nmap
import socket

logger = logging.getLogger(__name__)

def port_scan(host, ports):
    try:
        _ip = socket.gethostbyname(host)
    except BaseException as e:
        logger.error('%s[-] error get host ip addr:%s', colorama.Fore.RED, host)
        return

    _nps = nmap.PortScanner()
    _result = _nps.scan(hosts=_ip, ports=','.join(map(str, ports)))
    _tcps = _result.get('scan', {}).get(_ip, {}).get('tcp', {})

    logger.info('[+]cmd: %s', _result.get('nmap', {}).get('command_line', ''))
    for _port in ports:
        _status = _tcps.get(_port, {})
        logger.info('%s[*] %s/tcp %s %s %s', \
                                colorama.Fore.GREEN, host, _port, \
                                _status.get('state', 'unknow'), \
                                _status.get('name', ''))


if __name__ == '__main__':
    colorama.init(autoreset=True)
    logging.basicConfig(level=logging.DEBUG)
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-T', '--target', help='scan target', type=str, default='localhost')
    _parser.add_argument('-P', '--ports', help='scan ports', type=int, default=[80,21,22,443,8080], nargs='+')
    _args = _parser.parse_args()
    port_scan(_args.target, _args.ports)
