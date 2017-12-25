#_*_coding:utf-8_*_
import time




def time_counter(func):
        def wrapper():
            start = time.time()
            func()
            end = time.time()
            print"this function costs:",(end - start)
        return wrapper
@time_counter
def tellyoursalary():
    print "Allen makes 25k per month"
tellyoursalary()

#sayhi = time_counter(sayhi)
@time_counter
def sayhi():
    print 'hi your sister...'
    time.sleep(0.1)
sayhi()



