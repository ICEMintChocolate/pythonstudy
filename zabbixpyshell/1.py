#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lcj
import paramiko

privatekey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')#私钥路径

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.17.135.32', port=22, username='root',key_filename=privatekey)

stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()
print(result)

ssh.close()