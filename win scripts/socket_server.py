# _*_ coding:utf-8 _*_
import socket

server = socket.socket()
server.bind(('localhost',6969))

server.listen(50)

print ("I am waiting")
conn,addr = server.accept()
print (conn,addr)

data = conn.recv(1024)


print ("recv:",data)
conn.send(data.upper())
