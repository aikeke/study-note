#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys,commands,re

from zabbix_sender import *

def usage():
    print __doc__

def datarecv_print(datarecv):
    for key in datarecv.keys():
        print "%s: %s" % (key, datarecv[key])

__doc__ = '''Usage: python process.status.py [OPTIONS]
        -z, --zbx_host=name
            Connect to host of Zabbix Server.
        --zbx_port[=#]
            Port number of Zabbix Server to use for connection, built-in default (10051).
        -?, --help
            Display this help and exit.
    '''

if __name__ == "__main__":
    zbx_host = "10.1.11.46"
    zbx_port = 10051
    zbx_target = ""

    localip = commands.getoutput("/sbin/ifconfig eth1|grep Bcast|awk -F'addr:' '{print $2}'|awk '{print $1}'")
    if not zbx_target:
        zbx_target = localip
    zbxdata = []
    res=commands.getoutput('''top -bn 1|grep game|awk '{print $9","$10}' ''')
    cpu=res.split(',')[0]
    zbxdata.append({"host":zbx_target, "key":"game_cpu", "value":int(cpu)})
    zbxsender = zabbix_sender(zbx_host, zbx_port)
    zbxsender.send(zbxdata, datarecv_print)
