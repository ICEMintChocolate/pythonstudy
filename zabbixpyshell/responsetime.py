#!/usr/bin/python
#coding = utf-8
'''
Detect the response time of 80 port, the response time is more than 1 second alarm
'''
import os
import json
responsetime = os.popen('curl -o /dev/null -s -w time_namelookup:%{time_namelookup},time_connect:%{time_connect},time_starttransfer:%{time_starttransfer},time_total:%{time_total},speed_download:%{speed_download}"\n" "http://www.taobao.com"').read().split()
test = responsetime[0].split(',')
print test
dict1 = json.loads(test)