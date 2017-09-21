# -*- coding:utf8 -*-
# !/usr/bin/python
# fucong
# 2017-09-12
"""
rsync  ssh 方法远程拷贝线上的打包日志文件到本地目录

"""
import os
import time
import datetime
#备份时间
def getyesterday():
	today = datetime.date.today()
	noeday = datetime.timedelta(days=1)
	yesterday = today - noeday
	return yesterday
#脚本执行时间
backupday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#创建并获取备份目录
jump_bakup_path = os.popen('mkdir -p /data/backup/%s ; cd /data/backup/%s ;pwd -P ' % (getyesterday(),getyesterday())).read().split("\n")[0]
#远程执行每一个设备上的备份脚本
def web(host1='172.17.135.32',host2='172.17.135.33'):
	web1 = os.popen()
	web2 = os.popen()

def backend(host1='',host2=''):
	backend1 = os.popen()
	backend2 = os.popen()

def db(host='',host2=''):
	db1 = os.popen()
	db2 = os.popen()


#远程拷贝每一个设备上的备份目录到跳板机上



