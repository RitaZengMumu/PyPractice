# _*_ coding:utf-8 _*_
import select
import socket
import Queue

server = socket.socket()
server.bind(('localhost',9000))
server.listen(1000)

server.setblocking(False)

msg_dic = {}

inputs = [server,]

outputs = []

while True:
    readable ,writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable,writeable,exceptional)

    for r in readable:
        if r is server:
            conn,addr = server.accept()
            print(u"来了个新连接",addr)
            inputs.append(conn)
            msg_dic[conn] = Queue.Queue()
        else:
            data = r.recv(1024)
            print(u"收到数据",data)
            msg_dic[r].put(data)
            outputs.append(r)
    for w in writeable:
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)

        outputs.remove(w)

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)

            del msg_dic[e]

    for s in writeable:
        try:
            next_msg = msg_dic[s].get_nowait()

        except Queue.Empty:
            print("client [%s]" %s.getpeername()[0],"queue is empty")
            outputs.remove(s)

        else:
            print("sending msg to [%s]" %s.getpeername()[0],next_msg)



