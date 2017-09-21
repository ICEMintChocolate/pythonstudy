# -*- coding:utf8 -*-
#!/usr/bin/python

"""
java process Memory usage
java进程使用内存zabbix 监控
"""

import os
import sys
size = sys.argv[1]
duankou = sys.argv[2]
servicename = os.popen("netstat -ntpl | grep :%s | awk -F '/' '{print $1}' | awk '{print $NF}'" % duankou).read().split("\n")[0]
servicemem = os.popen("jmap -histo %s | grep Total | awk '{print int($3/1024/1024)}'" % servicename).read().split("\n")[0]
print servicemem