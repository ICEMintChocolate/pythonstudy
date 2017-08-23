#!/usr/bin/python
#coding = utf-8
'''
#java jvm gc,gct,fgc,
#YGC 从应用程序启动到采样时年轻代中gc次数
#FGC 从应用程序启动到采样时old代(全gc)gc次数
#FGCT 从应用程序启动到采样时old代(全gc)gc所用时间(s)
#GCT 从应用程序启动到采样时gc用的总时间(s)
#LGCC 最后一次GC的原因
#GCC 当前GC的原因
'''
import os
import time
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
pidlist = os.popen("netstat -ntpl  | grep java | awk '{print $NF}' | awk -F "'/'" '{print $1}' ").read().split()
for i in pidlist:
    jvmcompiler = os.popen("jstat -gccause 11191 1000 1 | awk '{print $7,$8,$9,$10,$11,$12,$13}'" %i).read().split("")
    jvmcompilerkey = jvmcompiler[0].split()
    jvmcompilervalue = jvmcompiler[1].split()
    jvmcompilerdict = dict(zip(jvmcompilerkey,jvmcompilervalue))
    print "%s pid:%s %s" % (nowtime, i, jvmcompilerdict)