#!/usr/bin/python
#coding=utf-8
'''
safsfd
'''
import pexpect
passwd = '2Lzs!7m4a'
cmd = 'mysql -h localhost -uroot -p'
child = pexpect.spawn(cmd)
child.expect('Enter password:')
child.sendline(passwd)
child.expect('>')
child.sendline('show full processlist;')
child.expect('>')
print child.before
print child.after
print child.buffer