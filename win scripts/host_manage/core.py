#_*_coding:utf-8_*_

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
        if hasattr(self,cmd_str):
            getattr(self,cmd_str)()
        else:
            setattr(self,cmd_str,self.command)
            getattr(self,cmd_str)()

    def command(self):
        """comand process"""

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname=self.host,port=self.port,username=self.username,password=self.password)
        stdin,stdout,stderr = ssh.exec_command(self.cmd)
        result = stdout.read()
        print("%s".center(50,"-") % self.host)
        print(result.decode())
        ssh.close()

    def put(self):

        filename = self.cmd.split()[1]
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(filename,filename)
        print("put sucess")
        transport.close()

def show_host_list():
    """choose the group"""
    for index,key in enumerate(settings.msg_dic):
         print (index + 1,key,len(settings.msg_dic[key]))

    while True:
        choose_host_list = input(">>>(eg:group1)").strip()
        host_dic = settings.msg_dic.get(choose_host_list)
        if host_dic:

            for key in host_dic:
                 print(key,host_dic[key]["IP"])
            return host_dic
        else:
            print("Does not exist this group!")

def interactive(choose_host_list):
    thread_list = []
    while True:
        cmd = input(">>>").strip()
        if cmd:
            for key in choose_host_list:
                host,port,username,password = choose_host_list[key]["IP"],choose_host_list[key]["port"],\
                                              choose_host_list[key]["username"],choose_host_list[key]["password"]

                func = REMOTE_HOST(host,port,username,password,cmd)
                t = threading.Thread(target=func.run)
                t.start()
                thread_list.append(t)
            for t in thread_list:
                t.join()
        else:
            continue

def run():
    choose_host_list = show_host_list()
    interactive(choose_host_list)









