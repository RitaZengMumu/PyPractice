#!/bin/python
#coding=utf-8
def sayhi(name,salary,group='Nokia',title='SA'):
    age = 29
    """This is my first test function code"""
    print 'hello,%s,you are %s years old,you are working in %s' % (name,age,group)
    print title

sayhi('Alex',3000)
sayhi('Rita',15000,'CICC','Arch')
sayhi('Tina',10500,title='Testing')

