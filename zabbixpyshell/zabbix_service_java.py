#!/usr/bin/python
#coding=utf-8
import os
import sys
'''
Determine whether ports and processes exist, and that ports are open states

'''
def help():
	print "Usage:  "
	print "       %s process_name [process_port]" % sys.argv[0]
	print "Example: "
	print "       %s mysql         ;If the process_nameexists, output 1, otherwise 0" % sys.argv[0]
	print "       %s nginx  80     ;If the process_port exists, output 1,otherwise 0" % sys.argv[0]
	print "       %s mysql  3306 " % sys.argv[0]

def service_name():
    services = os.popen(" ps -ef | grep %s | grep -v grep | grep -v python| wc -l " % sys.argv[1]).read().split("\n")[0]
    if not services:
	    print "0"
	    return
    if int(services) >= 1:
	    print "1"
    else:
	    print "0"


def service_port():
    ports = os.popen("netstat -lnt|grep -v grep|grep ':%s'| wc -l" % sys.argv[2]).read().split("\n")[0]
    if int(ports) >= 1:
	    print "1"
    else:
	    print "0"

###start execute
if len(sys.argv) == 2:
	service_name()
	sys.exit()
elif len(sys.argv) == 2:
	service_port()
	sys.exit()
else:
	help()
	sys.exit()