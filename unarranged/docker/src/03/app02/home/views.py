from django.shortcuts import render
from django.http import HttpResponse

import time
import redis

def index(request):
    _r = redis.Redis(host='redis', port=6379, db=0)

    _infos = []
    _infos.append(redis.__file__)
    _infos.append('Set')
    _infos.append('Before:%s' % _r.get('Hi'))
    _r.set('Hi', 'APP-02-%s' % time.time())
    _infos.append('After:%s' % _r.get('Hi'))
    _infos.append('Reids Infos:')
    _rinfo = _r.info()
    for _key in _rinfo:
        _infos.append('%s:%s' % (_key, _rinfo[_key]))
    return HttpResponse('<br>'.join(_infos))
