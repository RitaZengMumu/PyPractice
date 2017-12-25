#!/usr/bin/env python

import settings
import paramiko
import threading
import os

class REMOTE_HOST(object):

    def __init__(self,host,port,username,password,cmd):

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd

    def run(self):
        cmd_str = self.cmd.split()[0]
        if hasattr(self, cmd_str):
            getattr(self, cmd_str)()

        else:


