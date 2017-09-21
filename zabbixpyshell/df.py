#!/usr/bin/python
#coding = utf-8
'''
disk full
'''
import os
import time
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
test = os.popen("df -h|egrep -v 'tmp|var|shm'").read().split("\n")
listdf1 = test[0].split()
listdf2 = test[1].split()
dfdict = dict(zip(listdf1,listdf2))
print "disk:%s mount:%s use:%s" % (dfdict['Filesystem'],dfdict['Mounted'],dfdict['Use%'])
if dfdict['Use%'] > '95%':
     print "%s disk:%s mount:%s use:%s Disk usage has reached 95%. Please clear the disk to avoid program startup failure" % (nowtime,dfdict['Filesystem'],dfdict['Mounted'],dfdict['Use%'])
elif dfdict['Use%'] > '85%':
     print "disk:%s mount:%s use:%s Disk usage has reached 85%, please check in and clean up in time "% (dfdict['Filesystem'],dfdict['Mounted'],dfdict['Use%'])
