#coding=utf-8
import sys
"""infor = {
    'zhangli':['zhangli@163.com','360','IT','15513856114'],
    'wangping':['wp@126.com','easynet','IT','13501445733'],
    'lili':['lili@sina.com','xiaomi','developer','175019844333'],
    'liuli':['liuli@126.com','360','support','1871456667'],
    'liusan':['liusan@qq.com','qq','SA','171014456444']
}
list = infor.keys()
"""
while True:
  name=raw_input("please input the search info:").strip()
  if len(name) == 0:
    print "you must input the name!"
    continue
  elif name == 'exit':
      sys.exit()
  else:
      for m in list:
          print





