#!/usr/bin/python
#coding=utf-8
'''
监控每一个java 进程的 ygc，fgc，fgct，gct时间
'''
import os
import time
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
pidlist = os.popen("netstat -ntpl  | grep java | awk '{print $NF}' | awk -F "'/'" '{print $1}' ").read().split()
#javaname = os.popen()
#print pidlist
for i in pidlist:
        jstat = os.popen("jstat -gcutil %s 1000 1 |awk '{print $7,$8,$9,$10,$11}'" %i ).read().split("\n")
        test1 = jstat[0].split()
        test2 = jstat[1].split()
        jstatdict = dict(zip(test1,test2))
        #print jstatdict
        #print jstat
        print "%s pid:%s %s" % (nowtime,i,jstatdict)
