# -*- coding:utf8 -*-
# !/usr/bin/python
# fucong
# 2017-09-20
"""
html5 王思放的测试环境部署
"""
import os
import urllib2
#目录
jenkins_dev_work_wsf_path = '/data/jenkins/workspace/eflower-html-w-test/source_code/w'
jenkins_dev_cp_wsf_path = '/data/jenkins/workspace/eflower-html-w-test/source_code/w/w'
dev_html_8_233 = '/usr/local/nginx/html'
npm_command = '/usr/bin/npm'
tar_command = '/usr/bin/tar'
ssh_command = '/usr/bin/ssh'
scp_command = '/usr/bin/scp'
#构建
npm_install = os.popen('cd %s ;%s install'%(jenkins_dev_work_wsf_path,npm_command)).read()
npm_build = os.popen('cd %s ;%s run build'%(jenkins_dev_work_wsf_path,npm_command)).read()
print npm_build
#压缩
tar_wangsifang = os.popen('cd %s ;%s -zcf w.tar.gz w' % (jenkins_dev_work_wsf_path,tar_command)).read()
#远程拷贝
scp_wangsifang = os.popen('cd %s ;%s wangsifang.tar.gz root@ip:%s' %(jenkins_dev_work_wsf_path,scp_command,dev_html_8_233)).read()
#远程解压
ssh_tar_wangsifang = os.popen("%s root@ip 'cd %s/;%s -zxf w.tar.gz'"%(ssh_command,dev_html_8_233,tar_command)).read()
curl_test = 'http://xxx.xxx.com/w/#/booked'
req = urllib2.Request(curl_test)
response = urllib2.urlopen(req)
the_page = response.read()
url_code = response.getcode()
print url_code
print the_page