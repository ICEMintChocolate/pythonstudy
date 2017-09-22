# -*- coding:utf8 -*-
# !/usr/bin/python
# fucong
# 2017-09-04

"""
1.在每一台server 上找到日志目录。并且打gz的压缩包。
2.将生产环境设备上的日志 远程拷贝到 跳板机上，然后删除前一天的日志备份
3.从跳板机上将日志回传到本地的 存储服务器上，存储服务器上需要作端口映射。确保外网可以访问或者联通阿里云跳板机
测试日志打包
"""
import os
import datetime,time
backupday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def getyesterday():
	today = datetime.date.today()
	noeday = datetime.timedelta(days=1)
	yesterday = today - noeday
	return yesterday
print getyesterday()
#生产环境本地日志文件打包

backpath = os.popen('mkdir -p /data/backup/%s ; cd /data/backup/%s ;pwd -P ' % (getyesterday(),getyesterday())).read().split("\n")[0]
print '备份目录创建时间:%s，目录为:%s' %(backupday,backpath)
logs_path = '/opt/logs'
logs = ['config-server.log','discovery.log','gateway.log','server-info.log','server-message.log','server-order.log','server-product.log','server-user.log']
#for 循环打包
for i in logs:
    tar_server_log = os.popen('cd %s && tar -zcf %s.%s.tar.gz %s' %(logs_path,i,getyesterday(),i)).read()
#显示打包的日志名称
logs_name = os.popen('cd %s ; ls | grep "tar.gz" ' % logs_path).read().split()
#日志移动到备份路径
for mv in logs_name:
	mv_logs = os.popen('mv %s/%s %s/' % (logs_path,mv,backpath))
#########以上是本地备份#######
######本地备份拷贝到跳板机#####




