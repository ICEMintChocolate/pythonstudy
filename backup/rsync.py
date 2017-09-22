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
def getyesterday():
    today = datetime.date.today()
    noeday = datetime.timedelta(days=1)
    yesterday = today - noeday
    return yesterday

backupday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#本地目录
online_backup_path = '/volume2/online221_211backup/'
test_java_backup_path = '/volume2/test_java_log_backup/'
#每天的备份目录创建，不管是否有备份文件都要生成一个
test_erverday_java_bak_path = os.popen('echo b12345y |sudo -S mkdir -p %s%s ;cd %s%s ;pwd -P '% (test_java_backup_path,getyesterday(),test_java_backup_path,getyesterday())).read().split("\n")[0]
online_erverday_bak_path = os.popen('echo b12345y |sudo -S mkdir -p %s%s ;cd %s%s ;pwd -P '% (online_backup_path,getyesterday(),online_backup_path,getyesterday())).read().split("\n")[0]
print test_erverday_java_bak_path
print online_erverday_bak_path
#远程拷贝数据到本地
rsync_logs = os.popen('echo b12345y | sudo -S rsync root@47.94.8.233:/data/backup/%s/* %s '%(getyesterday(),test_erverday_java_bak_path))
rsync_online_logs = os.popen("echo b12345y | sudo -S rsync --exclude-from '/volume2/script/exclude.txt' root@47.94.221.211:/data/backup/* %s "%online_erverday_bak_path)