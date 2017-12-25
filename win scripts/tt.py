# _*_ encoding:utf-8 _*_
import threading

import time

def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,time.ctime())
        time.sleep(10)

def move(func):
    for i in range(2):
        print "I was at the  %s! %s" %(func,time.ctime())
        time.sleep(5)

threads = []

t1 = threading.Thread(target=music,args=('god is a gril',))
threads.append(t1)
t2 = threading.Thread(target=move,args=('avonda',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print "all over %s" %time.ctime()
