# _*_ coding:utf-8 _*_

import SocketServer
import account
import os,sys,commands

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.
    It is instantiated once per connection to the server,and must override the
    handle() method to implement communication to the client
    """

exit_flag = False

def handle(self):
    # self.request is the TCP socket connected to the client
    while not self.exit_flag:
        msg = self.request.recv(1024)
        if not msg:
            break
        msg_parse = msg.split("|")
        msg_type = msg_parse[0]