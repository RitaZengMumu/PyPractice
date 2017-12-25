#!/bin/python
#coding=utf-8
import re
#import sys
f=open(r'/root/scripts/contacts.txt','r')
text=f.read()
f.close()
find=raw_input('please input what you want to find:').strip()
#find=re.escape(find)
result=re.findall(".*"+find+".*",text)
for line in result:
  print line



