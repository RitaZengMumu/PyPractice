# _*_ coding:utf-8 _*_

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host, port = 'localhost', 1011
client.connect((host,port))
while True:
    user_input = raw_input("please enter:")
    client.send(user_input)
    recv_data = client.recv()
    print recv_data