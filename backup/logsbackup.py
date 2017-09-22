# -*- coding:utf8 -*-
# !/usr/bin/python
# user: fucong
# date: 2017-09-21
# mail: fucong@bianhk.com
"""
后端日志备份
"""
import os
import time
import datetime
server_log_path = '/opt/logs/'
backup_path = '/data/backup/log/'
baktime = time.strftime("%Y-%m-%d", time.localtime())
def getyesterday():
	today = datetime.date.today()
	noeday = datetime.timedelta(days=1)
	yesterday = today - noeday
	return yesterday
tar_server_logs = os.popen('cd /opt/;tar -zcf serverslogs.%s.tar.gz logs' %baktime).read()
mv_server_logs = os.popen('mv /opt/*.tar.gz %s' %backup_path).read()
