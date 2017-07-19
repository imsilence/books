#encoding: utf-8
import logging
import socket
import argparse
import colorama

TIMEOUT = 1

logger = logging.getLogger(__name__)

def _connect(ip, port):
    _client = None
    try:
        _client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _client.connect((ip, port))
        return True
    except BaseException as e:
        return False
    finally:
        if _client:
            _client.close()

def port_scan(host, ports):
    _ip = None
    _hostname = ''

    try:
        _ip = socket.gethostbyname(host)
    except BaseException as e:
        logger.error('%s[-] error get host ip addr:%s', colorama.Fore.RED, host)
        return
    try:
        _hostname = socket.gethostbyaddr(_ip)[0]
    except BaseException as e:
        logger.error('%s[-] error get hostname:%s', colorama.Fore.RED, _ip)

    socket.setdefaulttimeout(TIMEOUT)
    logger.info('%sscan host:%s[%s]', colorama.Fore.MAGENTA, _hostname, _ip)
    for _port in ports:
        if _connect(_ip, _port):
            logger.info('%s[+] %s/tcp open', colorama.Fore.GREEN, _port)
        else:
            logger.info('%s[-] %s/tcp closed', colorama.Fore.RED, _port)

if __name__ == '__main__':
    colorama.init(autoreset=True)
    logging.basicConfig(level=logging.DEBUG)
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-T', '--target', help='scan target', type=str, default='localhost')
    _parser.add_argument('-P', '--ports', help='scan ports', type=int, default=[80, 21, 22, 443, 8080], nargs='+')
    _args = _parser.parse_args()
    port_scan(_args.target, _args.ports)
