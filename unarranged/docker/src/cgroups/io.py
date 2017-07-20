#encoding: utf-8
import os
import time

if __name__== '__main__':
    print os.getpid()
    h = open('test.log', 'wb')
    for i in xrange(10000000000000):
        h.write(str(time.time()))
    f.close()
