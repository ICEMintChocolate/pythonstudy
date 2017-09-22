# -*- coding:utf8 -*-
# !/usr/bin/python
# user: fucong
# date: 2017-09-22
# mail: fucong@bianhk.com
"""
web 前端日志备份
"""
import os
import time
import datetime
baktime = time.strftime("%Y-%m-%d", time.localtime())
def getyesterday():
	today = datetime.date.today()
	noeday = datetime.timedelta(days=1)
	yesterday = today - noeday
	return yesterday
#print getyesterday()
gatewaylog_path = '/opt/logs/'
h5logs_path = '/usr/local/nginx/logs/'
backup_path = '/data/backup/log'
tar_gateway = os.popen('cd %s ;tar -zcf gateway.%s.tar.gz gateway.log'%(gatewaylog_path,baktime)).read()
tar_h5 = os.popen('cd %s ;tar -zcf h5.%s.tar.gz access-%s.log'%(h5logs_path,baktime,getyesterday())).read()
mv_gateway = os.popen('mv %s/*.tar.gz %s' %(gatewaylog_path,backup_path)).read()
mv_h5 = os.popen('mv %s/*.tar.gz %s'%(h5logs_path,backup_path)).read()