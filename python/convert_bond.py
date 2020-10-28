#/usr/bin/env python3
#author: aikeke
# -*- coding: utf-8 -*-
#当前可买的可转债
import json
import requests
import prettytable as pt

def get_dat():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    newUrl ="https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=1584777951900"
    response = requests.get(newUrl)
    data = response.content.decode("utf-8")
    data = json.loads(data)
    data=data['rows'] #list
    key_info={}
    data_list=[]
    new_data=[item['cell'] for item in data]
    for item in new_data:
        key_info['代码']=item.get("bond_id")
        key_info['名称']=item.get("bond_nm")
        key_info['价格']=item.get("price")
        key_info['涨跌幅']=item.get("increase_rt")
        key_info['正股']=item.get('stock_nm')
        key_info['正股涨跌幅']=item.get("sincrease_rt")
        key_info['溢价率']=item.get("premium_rt")
        key_info['换手率']=item.get("turnover_rt")
        key_info['交易量(万)']=item.get("volume")
        key_info['剩余规模(亿)']=item.get("curr_iss_amt")
        data_list.append(key_info)
        key_info={}
    return data_list

def comb_filter(data):
    new_list=[]
    for item in data:
        if float(item['价格'])<=115 and item['换手率'] is not None and float(item['剩余规模(亿)']) < 5 and float(item['溢价率'].split('%')[0])<30:
            new_list.append(item)
    return new_list            

if __name__=='__main__':
    data=get_dat()
    data=comb_filter(data)
    tb=pt.PrettyTable()
    tb.field_names = ["代码", "名称", "价格", "涨跌幅",'正股','正股涨跌幅','溢价率','换手率','交易量(万)','剩余规模(亿)']
    for item in data:
        tb.add_row(item.values())
    print(tb)
