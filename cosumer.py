#!/usr/bin/env python
#coding:utf-8

import threading,time
import Queue

q = Queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("bone%s" % count)
        print("Produce bone",count)
        count +=1
        time.sleep(0.1)


def Consumer(name):

    while True:
        print("[%s]get[%s]and eat it..." %(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args=("Alex",))
c = threading.Thread(target=Consumer,args=("Rita",))
c1 = threading.Thread(target=Consumer,args=("Lily",))

p.start()
c.start()
c1.start()



