import os
list = ['8716','9000']
for i in list:
    ports = os.popen("nmap 127.0.0.1 -p %s | grep tcp | awk '{print $2}' " %i).read()
    if ports == "open":
    	print "%s is ok" %(i)
    else:
    	print "%s is down" %(i)
