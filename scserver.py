#!/bin/python
#_*_coding:utf-8_*_

import SocketServer
import commands

class MySockServer(SocketServer.BaseRequestHandler):
    def handle(self,newconnsock,client_address):
        listensock.listen(50)
        self.newconnsock,self.client_address=listensock.accept()
        #print 'Got a new conn from',self.client_address
               
        while True:
            print 'Got a new conn from',self.client_address
            newconnsock.send('hello i am server,welcome to connect me')
            cmd = self.request.recv(1024)
            if not cmd:
                print 'Lost connection with',self.client_address
                break
            cmd_result = commands.getstatusoutput(cmd)

            self.request.send(cmd_result[1])

if __name__ == '__main__':

    h = '0.0.0.0'
    p = 9001
    s = SocketServer.ThreadingTCPServer((h,p),MySockServer)
    

    s.serve_forever()

