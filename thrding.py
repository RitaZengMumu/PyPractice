#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import threading
import time
def show(arg):
    time.sleep(1)
    print 'thread'+str(arg)

for i in range(10):
    t = threading.Thread(target=show,args=(i,))
    t.start()

print 'main thread stop'
