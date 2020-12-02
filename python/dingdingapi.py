#/usr/bin/python
#-*- coding:utf-8 -*-
import time
import hmac
import hashlib
import base64
import urllib
import json
import requests

timestamp = long(round(time.time() * 1000))
secret = 'SECc891a8cd4254530f0861d03683c3ccac0cd40dfe9c2cf503db1fb92439441e0c'
secret_enc = bytes(secret).encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = bytes(string_to_sign).encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.quote_plus(base64.b64encode(hmac_code))

url='https://oapi.dingtalk.com/robot/send?access_token=796be9814261a23e271b10894cfdf6aa51e9e2b0f049b6b305db1441bf3ca2d1&timestamp={}&sign={}'.format(timestamp,sign) 
headers={"Content-Type": "application/json"}
data={"msgtype": "text","text": {"content": "可以上厕所摸鱼@130xxx"},"at": {"atMobiles": [ "130xxx","xx" ]}}
data_json=json.dumps(data)
res=requests.post(url,data_json,headers=headers)
print res.text
