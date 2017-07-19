#encoding: utf-8
import logging
import socket
import argparse
import colorama
import threading

TIMEOUT = 1
SEND_MSG = 'KK\r\n'
RECV_MSG_SIZE = 100

logger = logging.getLogger(__name__)
screen_lock = threading.Semaphore(value=1)

def _connect(ip, port):
    _client = None
    try:
        _client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _client.connect((ip, port))
        _client.send(SEND_MSG)
        _msg = _client.recv(RECV_MSG_SIZE)
        screen_lock.acquire()
        logger.info('%s[+] %s/tcp open', colorama.Fore.GREEN, port)
        logger.info('%s[+] banner:%s', colorama.Fore.GREEN, _msg )
        screen_lock.release()
        return True, _msg
    except BaseException as e:
        screen_lock.acquire()
        logger.info('%s[-] %s/tcp closed', colorama.Fore.RED, port)
        screen_lock.release()
        return False, ''
    finally:
        if _client:
            _client.close()

def banner_scan(host, ports):
    _ip = None
    _hostname = ''

    try:
        _ip = socket.gethostbyname(host)
    except BaseException as e:
        logger.error('%s[-] error get host ip addr:%s', colorama.Fore.RED,host)
        return
    try:
        _hostname = socket.gethostbyaddr(_ip)[0]
    except BaseException as e:
        logger.error('%s[-] error get hostname:%s', colorama.Fore.RED, _ip)

    socket.setdefaulttimeout(TIMEOUT)
    logger.info('%sscan host:%s[%s]', colorama.Fore.MAGENTA, _hostname, _ip)
    for _port in ports:
        _th = threading.Thread(target=_connect, args=(_ip, _port))
        _th.start()

if __name__ == '__main__':
    colorama.init(autoreset=True)
    logging.basicConfig(level=logging.DEBUG)
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-T', '--target', help='scan target', type=str, default='localhost')
    _parser.add_argument('-P', '--ports', help='scan ports', type=int, default=[80, 21, 22, 443, 8080], nargs='+')
    _args = _parser.parse_args()
    banner_scan(_args.target, _args.ports)
