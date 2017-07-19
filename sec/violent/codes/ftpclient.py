#encoding: utf-8
import os
import sys
import argparse
import ftplib
import getpass
from pprint import pprint

NIL = lambda *args, **kwargs: None

def login(host, port, user, password, cwd=None, callback=NIL):
    try:
        _client = ftplib.FTP()
        _client.connect(host, port)
        _client.login(user, password)
        if cwd:
            _client.cwd(cwd)
        callback(_client)
        _client.close()
        return True
    except BaseException as e:
        print '[-] %s' % str(e)
        return False

def ftp_list_dir(client, *args):
    print '[+] list dir:'
    pprint(client.nlst())

def ftp_download_file(client, *args):
    _files = client.nlst()
    for _arg in args:
        if _arg not in _files:
            print '[-] file not found:%s' % _arg
        else:
            fhandler = open(_arg, 'wb+')
            client.retrbinary('RETR "%s"' % _arg, fhandler.write)
            fhandler.close()
            print '[+] download file %s ok' % _arg

def ftp_upload_file(client, *args):
    curr = os.path.dirname(os.path.abspath(__file__))
    for _arg in args:
        _path = os.path.join(curr, _arg)
        if not os.path.exists(_path) or not os.path.isfile(_path):
            print '[-] file not found:%s' % _path
        else:
            fhandler = open(_path, 'rb+')
            client.storbinary('STOR "%s"' % _arg, fhandler)
            fhandler.close()
            print '[+] upload file %s ok' % _arg



if __name__ == '__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-T', '--target', help='ftp host', \
                            default='localhost', type=str)
    _parser.add_argument('-P', '--port', help='ftp port', \
                            default=21, type=int)
    _parser.add_argument('-U', '--user', help='ftp user', \
                            default='anonymous', type=str)
    _parser.add_argument('-A', '--action', help='action',\
                            default='list_dir', type=str,
                            choices=['list_dir', 'download_file', 'upload_file'])
    _parser.add_argument('-C', '--cwd', help='dir cwd',\
                            type=str)
    _parser.add_argument('args', help='other args', type=str,\
                            default=[], nargs='*')

    _args = _parser.parse_args()

    _password = getpass.getpass('please input password:')

    _action = globals().get('ftp_%s' % _args.action)
    if _action is None:
        _parser.print_help()
        sys.exit(-1)

    login(_args.target, _args.port, _args.user, _password, _args.cwd, lambda x: _action(x, *_args.args))
