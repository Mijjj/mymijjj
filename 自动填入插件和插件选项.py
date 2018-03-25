import os
import sys
import time
path = os.getcwd()
filesname= os.listdir(path)
a=0
raw_input(unicode('Do you read the readme.txt?','utf-8').encode('gbk'))
for ii in filesname:
    if ii == "gui-config.json":
        a=1
if a!=1:
    print "no file named 'gui-config.json'"
    time.sleep(5)
c=0
lines=open("gui-config.json",'r').readlines()
for i in range(len(lines)-1):
    if lines[i].find('"plugin"')!=-1:
        lines[i]='      "plugin": "obfs-local",\n'
    elif lines[i].find('plugin_opts')!=-1:
#change obfs and obfs-host
        lines[i]='      "plugin_opts": "obfs=tls;obfs-host=www.mircosoft.com",\n'
        c=c+1
open("gui-config.json",'w').writelines(lines)
print "number of times:",c
time.sleep(5)
