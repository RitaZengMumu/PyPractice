#!/bin/python
#coding=utf-8
def users(username,group='Nokia'):
    list={}
    list[username]=group
    
    return list
print users('Alex')
print users('Rachel',"ChinaMobile")
