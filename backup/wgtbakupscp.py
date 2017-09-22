# -*- coding:utf8 -*-
# !/usr/bin/python
# fucong
# 2017-09-04

"""
数据同步脚本逻辑
1.jenkins 内网打包jar 包
2.上传到跳板机
3.不同的项目本地备份一份数据，并且删除上一次的备份文件
4.从跳板机上根据不同的项目分发到不同的服务器上

第一步时间会很快
第二步带宽问题，导致速度不快需要等待，使用shell脚本编写，直接作scp 动作到跳板机即可
第三步使用python 多线程的模式，同时去做备份，删除
第四步使用python 多线程的模式，同时去做远程拷贝

"""
import os
import time
import datetime
import sys

baktime = time.strftime("%Y-%m-%d", time.localtime())
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def getyesterday():
	today = datetime.date.today()
	noeday = datetime.timedelta(days=1)
	yesterday = today - noeday
	return yesterday


print getyesterday()
print nowtime

servers = ['config-server', 'discovery', 'server-demo', 'server-info', 'server-message', 'server-order','server-payment', 'server-product', 'server-user']


def help():
	print "Usage:  "
	print "       %s process_name" % sys.argv[0]
	print "Example: "
	print "       %s gateway " % sys.argv[0]


def web1(hostip1='ip'):
	bakdir = os.popen("ssh root@%s 'mkdir -p /data/backup/%s/%s'" % (hostip1, baktime, sys.argv[1])).read()
	bakup = os.popen("ssh root@%s 'mv /opt/%s/*.jar /data/backup/%s/%s/'" % (hostip1, sys.argv[1], baktime, sys.argv[1])).read()
	scp = os.popen("scp /opt/%s/*.jar root@%s:/opt/%s/" % (sys.argv[1], hostip1, sys.argv[1])).read()
	scdsh = os.popen("ssh root@%s 'cd /opt/%s/ && sh %s.sh restart' " % (hostip1, sys.argv[1], sys.argv[1])).read()
	print "%s%s 创建备份目录完成" % (nowtime,bakdir)
	print "%s%s 发布机本机备份完成" % (nowtime,bakup)
	print "%s%s 开始发布" % (nowtime,scp)
	print "%s%s 发布完成，正在重启服务，请等待" % (nowtime,scdsh)
	time.sleep(30)
	preocess = os.popen("ssh root@%s netstat -ntpl | grep java | grep 9000| wc -l" % hostip1).read().split("\n")[0]
	if int(preocess) < 1:
		print "%s %s %s is donw" % (hostip1,nowtime, sys.argv[1])
		return
	else:
		print "%s %s %s is ok"  % (hostip1,nowtime, sys.argv[1])
		return


def web2(hostip2='ip'):
	bakdir = os.popen("ssh root@%s 'mkdir -p /data/backup/%s/%s'" % (hostip2, baktime, sys.argv[1])).read()
	bakup = os.popen("ssh root@%s 'mv /opt/%s/*.jar /data/backup/%s/%s/'" % (hostip2, sys.argv[1], baktime, sys.argv[1])).read()
	scp = os.popen("scp /opt/%s/*.jar root@%s:/opt/%s/" % (sys.argv[1], hostip2, sys.argv[1])).read()
	scdsh = os.popen("ssh root@%s 'cd /opt/%s/ && sh %s.sh restart' " % (hostip2, sys.argv[1], sys.argv[1])).read()
	print bakdir
	print bakup
	print scp
	print scdsh

	preocess = os.popen("ssh root@%s netstat -ntpl | grep java | grep 9000| wc -l" % hostip2).read().split("\n")[0]
	if int(preocess) < 1:
		print "%s %s %s is donw" % (hostip2,nowtime, sys.argv[1])
		return
	else:
		print "%s %s %s is ok" % (hostip2,nowtime, sys.argv[1])
		return


def backwebi(hostip3='ip'):
	bakdir = os.popen("ssh root@%s 'mkdir -p /data/backup/%s/%s'" % (hostip3, baktime, sys.argv[1])).read()
	bakup = os.popen("ssh root@%s 'mv /opt/%s/*.jar /data/backup/%s/%s/'" % (hostip3, sys.argv[1], baktime, sys.argv[1])).read()
	scp = os.popen("scp /opt/%s/*.jar root@%s:/opt/%s/" % (sys.argv[1], hostip3, sys.argv[1])).read()
	scdsh = os.popen("ssh root@%s 'cd /opt/%s/ && sh %s.sh restart' " % (hostip3, sys.argv[1], sys.argv[1])).read()
	print bakdir
	print bakup
	print scp
	print scdsh
	time.sleep(30)
	preocess = os.popen("ssh root@%s  'ps -ef  | grep java | grep %s | grep -v grep | wc -l'" % (hostip3, sys.argv[1])).read().split("\n")[0]
	if int(preocess) < 1:
		print "%s %s %s is donw" % (hostip3,nowtime, sys.argv[1])
		return
	else:
		print "%s %s %s is ok"  % (hostip3,nowtime,sys.argv[1])
		return

def backwebii(hostip4='1ip'):
	bakdir = os.popen("ssh root@%s 'mkdir -p /data/backup/%s/%s'" % (hostip4, baktime, sys.argv[1])).read()
	bakup = os.popen("ssh root@%s 'mv /opt/%s/*.jar /data/backup/%s/%s/'" % (hostip4, sys.argv[1], baktime, sys.argv[1])).read()
	scp = os.popen("scp /opt/%s/*.jar root@%s:/opt/%s/" % (sys.argv[1], hostip4, sys.argv[1])).read()
	scdsh = os.popen("ssh root@%s 'cd /opt/%s/ && sh %s.sh restart' " % (hostip4, sys.argv[1], sys.argv[1])).read()
	print bakdir
	print bakup
	print scp
	print scdsh
	time.sleep(30)
	preocess = os.popen("ssh root@%s 'ps -ef | grep java | grep %s | grep -v grep |wc -l'" % (hostip4, sys.argv[1])).read().split("\n")[0]
	if int(preocess) < 1:
		print "%s %s %s is down" % (hostip4,nowtime, sys.argv[1])
		return
	else:
		print "%s %s %s is ok" % (hostip4,nowtime, sys.argv[1])
		return


servers = ['config-server','discovery','server-demo','server-info','server-message','server-order','server-payment','server-product','server-user']
#start execute
if len(sys.argv) == 2:
    if sys.argv[1] == 'gateway':
        web1()
        web2()
        print "%s is ok over" % sys.argv[1]
        sys.exit()
if len(sys.argv) == 2:
    if sys.argv[1] in servers:
        backwebi()
        backwebii()
        print "%s %s is over " % (nowtime,sys.argv[1])
    sys.exit()
else:
    help()
    sys.exit()
