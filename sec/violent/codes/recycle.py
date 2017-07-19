#encoding: utf-8
import os
import _winreg

def get_root_dirs():
    _root_dirs = []
    _key = None
    try:
        _sub_key = 'SYSTEM\MountedDevices'
        _key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, _sub_key)
        i = 0
        while True:
            _value, _, _ = _winreg.EnumValue(_key, i)
            if _value.startswith('\\DosDevices\\'):
                _root_dirs.append(_value[-2:])
            i += 1
    except BaseException as e:
        pass
    finally:
        if _key:
            _winreg.CloseKey(_key)

    return _root_dirs

def get_recycler_dirs(root_dirs):
    _recycler_names = ['Recycler', 'Recycled', '$Recycle.Bin']
    _recycler_paths = []
    for _root_dir in _root_dirs:
        for _recycler_name in _recycler_names:

            _path = os.path.join(_root_dir, '\\', _recycler_name)
            if os.path.exists(_path) and os.path.isdir(_path):
                _recycler_paths.append(_path)
    return _recycler_paths

def sid2user(sid):
    _user = sid
    _key = None
    try:
        _sub_key = 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\%s' % sid
        _key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, _sub_key)
        _dir, _ = _winreg.QueryValueEx(_key, 'ProfileImagePath')
        _user = os.path.basename(_dir)
        _winreg.CloseKey(_key)
    except BaseException as e:
        pass
    finally:
        if _key:
            _winreg.CloseKey(_key)

    return _user

if __name__ == '__main__':
    _root_dirs = get_root_dirs()
    _recycler_dirs = get_recycler_dirs(_root_dirs)
    for _recycler_dir in _recycler_dirs:
        for _dirname in os.listdir(_recycler_dir):
            print '[+] User[%s] Recycler (%s) Delete Files:' % (sid2user(_dirname), _recycler_dir)
            for _filename in os.listdir(os.path.join(_recycler_dir, _dirname)):
                print os.path.basename(os.path.join(_recycler_dir, _filename))
