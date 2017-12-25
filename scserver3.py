#!/usr/bin/python
#_*_coding:utf-8_*_
import socket
listensock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listensock.bind(('192.168.1.16',6000))
listensock.listen(50)
while 1:
  newconnsock,address=listensock.accept()
  print 'got connected from ',address
  newconnsock.send('hello i am server,welcome to connect me')
  ra=newconnsock.recv(512)
  print ra
  socket
  #newconnsock.close()
  #print 'server closed the new connection'
