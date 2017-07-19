#encoding: utf-8
import logging
import argparse
import getpass

import colorama
import pxssh

logger = logging.getLogger(__name__)

def ssh_connect(host, port, user, password):
    try:
        _client = pxssh.pxssh()
        _client.login(host, user, password=password, port=port)
        return _client
    except BaseException as e:
        print '%s[-] error connect %s:%s' % (colorama.Fore.RED, host, port)
        return None

def run_cmd(client, cmd):
    _client.sendline(cmd)
    _client.prompt()
    _msg = '\n'.join(_client.before.split('\n')[1:])
    if _msg:
        print(_msg)

if __name__ == '__main__':
    colorama.init(autoreset=True)
    logging.basicConfig(level=logging.DEBUG)
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-T', '--target', help='ssh host', \
                            default='localhost', type=str)
    _parser.add_argument('-P', '--port', help='ssh port', \
                            default=22, type=int)
    _parser.add_argument('-U', '--user', help='ssh user', \
                                default='root', type=str)

    _password = ''

    while not _password:
        _password = getpass.getpass('请输入密码:')

    _args = _parser.parse_args()
    _client = ssh_connect(_args.target, _args.port, _args.user, _password)
    if _client:
        while True:
            _cmd = raw_input('>>>')
            if _cmd == 'quit':
                break
            run_cmd(_client, _cmd)
        _client.logout()
