#/usr/bin/env python
#-*- coding:utf-8 -*-
#上班摸鱼
import requests
import time
import hmac
import hashlib
import base64
import urllib
import json
timestamp = long(round(time.time() * 1000))
secret = 'XXXXXX'
secret_enc = bytes(secret).encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = bytes(string_to_sign).encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.quote_plus(base64.b64encode(hmac_code))

def get_res(code):
    url='http://hq.sinajs.cn/list=s_{}'.format(code)
    res=requests.get(url)
    res=res.text.split(',')[3]
    return res

result='今日大盘指数:\n'
sour_dict={'上证指数':'sh000001','深圳指数':'sz399001','创业板指数':'sz399006','医疗指数':'sz399441','新能源车':'sz399976'}
for key,value in sour_dict.items():
    res=get_res(value)
    result=result+str(key)+':'+str(res)+'%'+'\n'

url='https://oapi.dingtalk.com/robot/send?access_token=796be9814261a23e271b10894cfdf6aa51e9e2b0f049b6b305db1441bf3ca2d1&timestamp={}&sign={}'.format(timestamp,sign)
headers={"Content-Type": "application/json"}
data={"msgtype": "text","text": {"content": result }}
data_json=json.dumps(data)
res=requests.post(url,data_json,headers=headers)
