#/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import requests

def get_mem():
    res=commands.getoutput('''free -m|grep Mem|awk '{print $2}' ''')    
    return res


url='http://192.168.21.23:5000/api'
data=get_mem()
data={'mem':data,'wife':'爱丽丝'}
for i in data.values():
    print i
response=requests.post(url,data=data)
print type(response.text)
res=requests.get(url)
print res.text
