# _*_ coding:utf-8 _*_
import socket
HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    msg = bytes(input(">>:", encoding="utf-8"))
    s.sendall(msg)
    data = s.recv(1024)

    print('Received',data)
s.close()