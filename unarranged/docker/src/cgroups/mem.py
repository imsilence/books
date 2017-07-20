#encoding: utf-8
import os
import time

if __name__ == '__main__':
    print os.getpid()
    time.sleep(10)
    x = []
    start = 0
    length = 100000
    for ii in range(10):
        print ii
        for i in range(25) :
            x += range(start, start + length)
            start += length
            time.sleep(2)
       
    time.sleep(120)
        
