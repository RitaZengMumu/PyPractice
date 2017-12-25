#!/bin/python
#_*_coding:utf-8_*_

import socket

host,port = '192.168.1.16',9001

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((host,port))

while True:
    user_input = raw_input("msg to send::").strip()
    if len(user_input) == 0:continue
    c.send(user_input)
    recv_size = c.recv(1024)
    recv_data = c.recv(int(recv_size))
    print 'Receved:',recv_size

c.close()
