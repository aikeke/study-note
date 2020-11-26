#/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import urllib2 
from urllib2 import URLError 
class ZabbixApi(object):
    def __init__(self):
        self.__url = 'http://xxx/zabbix/api_jsonrpc.php'
        self.__user = 'xxxx'
        self.__password = 'xxxx'
        self.__header = {"Content-Type": "application/json"}
        self.__token_id = self.UserLogin()

    def UserLogin(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.__user,
                "password": self.__password
            },
            "id": 0,
        }
        return self.PostRequest(data)

    def PostRequest(self, data):
        request = urllib2.Request(self.__url,json.dumps(data).encode('utf-8'))        
#result = requests.post(self.__url,self.__header,data=json.dumps(data))
        for key in self.__header: 
                request.add_header(key, self.__header[key]) 
        result = urllib2.urlopen(request)
        print result.read()
            #return response['result']

test=ZabbixApi()

