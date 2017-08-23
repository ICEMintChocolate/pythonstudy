#!/usr/bin/python
#coding = utf-8
'''
java process Memory usage
'''
import os
import time
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
pidlist = os.popen("netstat -ntpl  | grep java | awk '{print $NF}' | awk -F "'/'" '{print $1}' ").read().split()
for i in pidlist:
	memtotal = os.popen("jmap -histo %s | grep Total | awk '{print $3/1024/1024}'" %i ).read()
	print "%s pid:%s memtotal:%sMb" % (nowtime,i,memtotal[0])