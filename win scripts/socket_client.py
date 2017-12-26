# _*_ coding:utf-8 _*_

import socket
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

client = socket.socket()
client.connect(('localhost',6969))
client.send("我要下电影".encode(encoding="utf-8"))
data = client.recv(1024)
print("recv:",unicode(data,'utf-8'))
client.close()
