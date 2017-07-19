#encoding: utf-8

import pxssh

class Client(object):

    def __init__(self, host, port, user, password):
        self._session = self._connect(host, port, user, password)
        self._host = host
        self._port = port

    def _connect(self, host, port, user, password):
        try:
            _client = pxssh.pxssh()
            _client.login(host, user, port=port, password=password)
            return _client
        except BaseException as e:
            print '[-] Error connect:%s' % str(e)
            return None

    def command(self, cmd):
        _output = None
        if self._session:
            self._session.sendline(cmd)
            self._session.prompt()
            _output = self._session.before
        return _output

    def close(self):
        if self._session:
            self._session.logout()

    def __str__(self):
        return '%s:%s' % (self._host, self._port)

class Botnet(object):
    def __init__(self):
        self._clients = []

    def add_client(self, host, port, user, password):
        self._clients.append(Client(host, port, user, password))

    def exec_cmd(self, cmd):
        for _client in self._clients:
            _output = _client.command(cmd)
            print '%s, output:%s' % (_client, _output)

    def close(self):
        for _client in self._clients:
            _client.close()

if __name__ == '__main__':
    _bnt = Botnet()
    _bnt.add_client('x.x.x.x', 22, 'xxxx', 'xxxx')
    _bnt.exec_cmd('id')
    _bnt.close()
