#encoding: utf-8
import logging
import argparse
import getpass

import colorama
import pexpect

PROMPT = ['>>>', '#', '>', '\$']

logger = logging.getLogger(__name__)

def ssh_connect(host, port, user, password):
    _cmd = 'ssh -p {port} {user}@{host}'.format(port=port, user=user, host=host)
    _client = pexpect.spawn(_cmd)

    _rt = _client.expect([pexpect.TIMEOUT, 'Are you sure you want to continue connecting', '[P|p]assword:'])
    if _rt == 0:
        print '%s[-] error connect %s:%s' % (colorama.Fore.RED, host, port)
        return

    if _rt == 1:
        _client.sendline('yes')
        _rt = _client.expect([pexpect.TIMEOUT, '[P|p]assword:'])

    if _rt == 0:
        print '%s[-] error connect %s:%s' % (colorama.Fore.RED, host, port)
        return

    _client.sendline(password)
    _client.expect(PROMPT)
    print('%s$' % _client.before.split('\n')[-1]),
    return _client

def run_cmd(client, cmd):
    _client.sendline(cmd)
    _rt = _client.expect(PROMPT)
    print('%s%s' % ('\n'.join(_client.before.split('\n')[1:]), _client.after)),

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
    while True:
        _cmd = raw_input()
        if _cmd == 'quit':
            break
        run_cmd(_client, _cmd)
    _client.close()
