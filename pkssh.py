#!/usr/bin/env python
#_*_coding:utf-8_*_

import paramiko

host = '192.168.1.16'
user = 'root'
password = 'hehe7971335'

t = paramiko.Transport((host,22))

t.connect(username=user, password=password)

sftp = paramiko.SFTPClient.from_transport(t)

sftp.put('/data/MySQL-python-1.2.5.zip','/root/scripts/rita.zip')

t.close()


