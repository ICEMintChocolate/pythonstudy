#!/usr/bin/python
#coding = utf-8
'''
java process Memory usage
'''
import os
import sys
servicename = os.popen("mysql -e 'show global status like 'Questions';' | awk NR==2").read().split("\n")
servicemem = os.popen("jmap -histo %s | grep Total | awk '{print $3/1024/1024}'" %(servicename)).read().split("\n")[0]
