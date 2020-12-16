#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys,commands,re

from zabbix_sender import *


def datarecv_print(datarecv):
    for key in datarecv.keys():
        print "%s: %s" % (key, datarecv[key])


if __name__ == "__main__":
    zbx_host = "58.215.51.221"
    zbx_port = 10051
    zbx_target = "192.168.21.23"
    
    log_file="/tmp/access.log/access.log"
    localip = commands.getoutput("/sbin/ifconfig eth1|grep Bcast|awk -F'addr:' '{print $2}'|awk '{print $1}'")
    if not zbx_target:
        zbx_target = localip
    zbxdata = []
    cmd='''cat {}'''.format(log_file)+r'''|awk '{print $9}'|sort|uniq -c'''
    res=commands.getoutput(cmd)
    print res
    zbxdata.append({"host":zbx_target, "key":"nginx_log", "value":res})
    zbxsender = zabbix_sender(zbx_host, zbx_port)
    zbxsender.send(zbxdata, datarecv_print)
