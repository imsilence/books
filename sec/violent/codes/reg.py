#encoding: utf-8

import _winreg

def get_wireless():
    _sub_key = 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged'
    _key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, _sub_key)
    i = 0
    while True:
        try:
            _guid = _winreg.EnumKey(_key, i)
            _child_key = _winreg.OpenKey(_key, str(_guid))
            _, _network, _ = _winreg.EnumValue(_child_key, 4)
            _, _mac, _ = _winreg.EnumValue(_child_key, 5)
            _mac = ':'.join(['%02X' % ord(_c) for _c in _mac])
            _winreg.CloseKey(_child_key)
            print '[+] %s:%s' % (_network, _mac)
            i += 1
        except BaseException as e:
            break
    _winreg.CloseKey(_key)

if __name__ == '__main__':
    get_wireless()
    pass
