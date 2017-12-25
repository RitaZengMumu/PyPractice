# _*_ coding:utf-8 _*_

import socket
import os,sys
import hashlib

class Myclient():
    """ftp client"""
    def __init__(self,ip_port):
        self.ip_port = ip_port

    def connect(self):
        """connect server"""
        self.client = socket.socket()
        self.client.connect(self.ip_port)
    def start(self):
        """starting"""
        self.connect()
        while True:
            username = input("please input username:").strip()
            password = input("input password:").strip()
            login_info = ("%s:%s" %(username,password))
            self.client.sendall(login_info.decode())
