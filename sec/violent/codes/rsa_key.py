#encoding: utf-8

import rsa
import time

if __name__ == '__main__':

    s = time.time()

    # 生成公、私钥
    _public, _private = rsa.newkeys(1024)

    print time.time() - s
    s = time.time()

    #存储公、私钥
    with open('public.pem', 'wb') as handler:
        handler.write(_public.save_pkcs1())

    print time.time() - s
    s = time.time()

    with open('private.pem', 'wb') as handler:
        handler.write(_private.save_pkcs1())

    print time.time() - s
    s = time.time()

    #读取公、私钥
    with open('public.pem', 'rb') as handler:
        _public_key = rsa.PublicKey.load_pkcs1(handler.read())

    print time.time() - s
    s = time.time()

    with open('private.pem', 'rb') as handler:
        _private_key = rsa.PrivateKey.load_pkcs1(handler.read())

    print time.time() - s
    s = time.time()

    #加密&解密
    _msg = 'Hello, KK'
    _crypto = rsa.encrypt(_msg, _public_key)

    print time.time() - s
    s = time.time()
    _msg = rsa.decrypt(_crypto, _private_key)

    print time.time() - s
    s = time.time()

    #签名&认证
    _signature = rsa.sign(_msg, _private_key, 'SHA-1')

    print time.time() - s
    s = time.time()

    rsa.verify(_msg, _signature, _public_key)

    print time.time() - s
    s = time.time()
