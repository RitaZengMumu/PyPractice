#!/bin/bash
#_*_coding:utf-8_*_
import time

def sayhi():
    print 'hi your sister...'
    time.sleep(0.1)

def time_counter(func):
        def wrapper():
            start = time.time()
            func()
            end = time.time()
            print"this function costs:",end - start
        return wrapper
@time_counter
def tellyoursalary():
    print "Allen makes 25k per month"

sayhi = time_counter(sayhi)
sayhi()

