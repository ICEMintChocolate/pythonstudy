# -*- coding:utf8 -*-
# !/usr/bin/python
# fucong
# 2017-09-21
"""
重构server order 项目 测试环境发布脚本
"""
import os
#jenkins 项目目录
server_home = '/data/jenkins/workspace/eflower-server-order-test/target'
server_tmep_home = '/data/eflower-server-order'
#server order 工作目录
server_bak_home = '/data/bak/eflower-server-order'
server_work_home = '/opt/server-order'
#拷贝jar 文件到 临时目录
mv_server = os.popen('\mv %s/*.jar %s' %(server_home,server_tmep_home)).read()
#备份测试环境的程序包
mv_ssh_server = os.popen('ssh root@47.94.8.233 "\mv %s/*.jar %s/"' %(server_work_home,server_bak_home)).read()
#拷贝临时目录下的文件到测试环境
scp_server = os.popen('scp %s/*.jar root@47.94.8.233:%s'%(server_tmep_home,server_work_home)).read()
#远程启动order项目
sh_server = os.popen('ssh root@47.94.8.233 "source .bash_profile;cd %s ;sh server-order.sh restart"'%server_work_home).read()
print sh_server