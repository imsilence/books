#encoding: utf-8
import os
import sys
import logging
import argparse
import getpass

import colorama
import pexpect

PROMPT = ['>>>', '#', '>', '\$']

logger = logging.getLogger(__name__)

def ssh_connect(host, port, user, keyfile):
    _cmd = 'ssh -p {port} {user}@{host} -i {keyfile} -o PasswordAuthentication=no'.format(port=port, user=user, host=host, keyfile=keyfile)
    _client = pexpect.spawn(_cmd)

    _rt = _client.expect([pexpect.TIMEOUT, 'Are you sure you want to continue connecting', 'Enter passphrase'])
    if _rt == 0:
        print '%s[-] error connect %s:%s' % (colorama.Fore.RED, host, port)
        return

    if _rt == 1:
        _client.sendline('yes')
        _rt = _client.expect([pexpect.TIMEOUT, 'Enter passphrase'])

    if _rt == 0:
        print '%s[-] error connect %s:%s' % (colorama.Fore.RED, host, port)
        return
    _password = getpass.getpass('Enter passphrase:')

    _client.sendline(_password)
    _client.expect(PROMPT)
    print('%s$' % _client.before.split('\n')[-1]),
    return _client

def run_cmd(client, cmd):
    _client.sendline(cmd)
    _rt = _client.expect(PROMPT)
    print('%s%s' % (_client.before, _client.after)),

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
    _parser.add_argument('-K', '--keyfile', help='ssh private key', \
                                type=str)
    _parser.add_argument('-C', '--cmds', help='ssh commands', \
                                default=['id'], type=str, nargs='+')


    _args = _parser.parse_args()
    if _args.keyfile is None or \
        not os.path.exists(_args.keyfile) or \
        not os.path.isfile(_args.keyfile):
        _parser.print_help()
        sys.exit(-1)

    _client = ssh_connect(_args.target, _args.port, _args.user, _args.keyfile)
    for _cmd in _args.cmds:
        run_cmd(_client, _cmd)
