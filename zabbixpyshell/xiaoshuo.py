#coding = utf-8
# -*- coding: ascii -*-
import urllib.request
import re
import time
import sys

if len(sys.argv) > 1:
	module = sys.argv[1]
else:
	module = '0_168'

start_page = ''

filepath = 'D:/'
url = "http://www.biquge.com/" + module + "/"
rule = r'/' + module + '/[\d]{7,9}.html'


def array_unique(list):
	new_array = []
	for item in list:
		if item not in new_array:
			new_array.append(item)
	return new_array


def getSubStr(str, start_str, end_str, start_len, end_len):
	pos_start = str.find(start_str)
	if pos_start == -1:
		return ''
	pos_end = str.find(end_str, pos_start)
	if pos_end == -1:
		return ''
	return str[pos_start + start_len:pos_end - end_len]


def getContent(host, param):
	newurl = host + '/' + param.split('/')[2]
	html = urllib.request.urlopen(newurl).read().decode('UTF-8')
	title = getSubStr(html, '<div class="bookname">', '</h1>', 34, 0)
	content = getSubStr(html, '<div id="content">', '<div class="bottem2">', 43, 70)
	content = content.replace('&nbsp;', ' ').replace('<br/>', '\r\n')
	result = title + '\r\n' * 2 + content + '\r\n' * 4
	return result if title != '' and content != '' else ''


indexContent = urllib.request.urlopen(url).read().decode('UTF-8')
bookname = getSubStr(indexContent, '<div id="maininfo">', '</h1>', 51, 0)
filename = filepath + bookname + '小说-全本.txt'
data = array_unique(re.findall(rule, indexContent))
data.sort()

for page in data:
	if page >= start_page:
		print('请求页面：%s' % page, end='')
		content = getContent(url, page)
		curtime = time.strftime('%H:%M:%S', time.localtime(time.time()))
		if content != '':
			file = open(filename, 'a+', encoding='utf-8')
			file.write(content)
			file.close()
			print(' 执行结果：成功 %s' % curtime)
		else:
			print(' 执行结果：失败 %s' % curtime)