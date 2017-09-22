# -*- coding:utf8 -*-
# !/usr/bin/python
# user: fucong
# date: 2017-09-22
# mail: fucong@bianhk.com
"""
收集所有设备的备份文件到指定的目录
"""
import os
#jump back path
backup_path = '/data/backup'
#server back path
backup_server_paht = '/data/backup/log'
#db back path
backup_db_path = '/data/backup'

#前端server备份文件回传
webip1='172.17.135.32'
webip2='172.17.135.33'
scpIP1 = os.popen('rsync root@%s:%s/* %s/%s/' %(webip1,backup_server_paht,backup_path,webip1) ).read()
scpIP2 = os.popen('rsync root@%s:%s/* %s/%s/' %(webip2,backup_server_paht,backup_path,webip2) ).read()

#后端备份文件回传
backendip1='172.17.135.30'
backendip2='172.17.135.31'
backendscpIP1 = os.popen('rsync root@%s:%s/* %s/%s/' %(backendip1,backup_server_paht,backup_path,backendip1) ).read()
backendscpIP2 = os.popen('rsync root@%s:%s/* %s/%s/' %(backendip2,backup_server_paht,backup_path,backendip2) ).read()
#数据库备份回传w
dbipm='172.17.135.28'
dbips='172.17.135.27'
dbscpIP1 = os.popen('rsync root@%s:%s/*.sql %s/%s/' %(dbipm,backup_db_path,backup_path,dbipm) ).read()
dbscpIP2 = os.popen('rsync root@%s:%s/*.sql %s/%s/' %(dbips,backup_db_path,backup_path,dbips) ).read()

