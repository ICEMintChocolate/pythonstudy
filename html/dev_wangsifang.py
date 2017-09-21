# -*- coding:utf8 -*-
# !/usr/bin/python
# fucong
# 2017-09-20
"""
html5 王思放的开发环境部署
"""
import os
import urllib2
jenkins_dev_work_wsf_path = '/data/jenkins/workspace/eflower-html-w-dev/source_code/w'
jenkins_dev_cp_wsf_path = '/data/jenkins/workspace/eflower-html-w-dev/source_code/w/w'
dev_html_253 = '/data/devtest/apache2/htdocs/w'
npm_command = '/usr/bin/npm'
#构建
npm_install = os.popen('cd %s ;%s install'%(jenkins_dev_work_wsf_path,npm_command)).read()
npm_build = os.popen('cd %s ;%s run build'%(jenkins_dev_work_wsf_path,npm_command)).read()
print npm_build
#拷贝文件到dev环境
cp_i = os.popen('/usr/bin/unalias cp').read()
cp_wangsifang = os.popen('/usr/bin/cp -rfp %s/* %s/' %(jenkins_dev_cp_wsf_path,dev_html_253)).read()
curl_test = 'http://xxx.xxx.com/w/#/booked'
req = urllib2.Request(curl_test)
response = urllib2.urlopen(req)
the_page = response.read()
url_code = response.getcode()
print url_code
print the_page

