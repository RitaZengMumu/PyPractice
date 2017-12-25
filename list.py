#!/bin/python
#encoding=utf-8
names = ['IBM','Alex','JACK','DELL']
names.extend(range(1000))
names.insert(100,'IBM')
names.insert(200,'IBM')
names.insert(500,'IBM')

for i in range(names.count('IBM')):
  ibm_index = names.index('IBM')
  print 'INDEX:',ibm_index
  names[ibm_index] = 'HP'
print names.count('HP')
