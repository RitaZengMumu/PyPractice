# _*_ coding:utf-8 _*_
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',1011))
server.listen(20)
print "I am waiting"
while True:
    conn,addr = server.accept()

    while True:
        print ("new conn:",addr)
        data = conn.recv(1024)
        if not data:
            break
        print data
        conn.send(data)