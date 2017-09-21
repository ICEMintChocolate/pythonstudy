# -*- coding:utf8 -*-
# !/usr/bin/python
# fucong
# 2017-09-12
"""
rsync  ssh 方法远程拷贝线上的打包日志文件到本地目录
本地存储脚本
"""
import os
import time
import datetime
def getyesterday():
	today = datetime.date.today()
	noeday = datetime.timedelta(days=1)
	yesterday = today - noeday
	return yesterday
backupday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#backuptime = time.strftime("%Y-%m-%d", time.localtime())
java_backup_path = '/volume2/java_log_backup/'
web_backup_path = '/volume2/web_log_backup/'
elk_log_backup_path = '/volume2/elk_log_backup/'
mysql_log_backup_path = '/volume2/mysql_log_backup/'
test_java_backup_path = '/volume2/test_java_log_backup/'
#每天的备份目录创建，不管是否有备份文件都要生成一个
everday_java_bak_path = os.popen('echo b12345y | sudo -S mkdir -p %s%s' % (java_backup_path,getyesterday())).read()
everday_web_bak_path = os.popen('echo b12345y | sudo -S mkdir -p %s%s' % (web_backup_path,getyesterday())).read()
everday_elk_bak_path = os.popen('echo b12345y | sudo -S mkdir -p %s%s' % (elk_log_backup_path,getyesterday())).read()
everday_mysql_bak_path = os.popen('echo b12345y | sudo -S mkdir -p %s%s' % (mysql_log_backup_path,getyesterday())).read()
test_erverday_java_bak_path = os.popen('echo b12345y |sudo -S mkdir -p %s%s ;cd %s%s ;pwd -P '% (test_java_backup_path,getyesterday(),test_java_backup_path,getyesterday())).read().split("\n")[0]
print test_erverday_java_bak_path
#远程拷贝数据到本地
rsync_logs = os.popen('echo b12345y | sudo -S rsync root@47.94.8.233:/data/backup/%s/* %s '%(getyesterday(),test_erverday_java_bak_path))