#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys
import struct
from socket import *

try:
    import simplejson as json
except:
    import json

reload(sys)
sys.setdefaultencoding("utf-8")

class zabbix_sender(object):
    def __init__(self, host, port=10051, timeout=10):
        self.__host__ = host
        self.__port__ = port
        self.__timeout__ = timeout

    def __del__(self):
        if self.tcpCliSock:
            try:
                self.tcpCliSock.close()
            except:
                self.tcpCliSock = None
        self.tcpCliSock = None

    def __protocol_pack__(self, data):
        protocol_package = {"request":"sender data"}
        protocol_package["data"] = data
        datajson = json.dumps(protocol_package)

        datalength = len(datajson)
        byte1 = (datalength & 0xFF)
        byte2 = (datalength & 0xFF00) / 0x100
        byte3 = (datalength & 0xFF0000) / 0x10000
        byte4 = (datalength & 0xFF000000) / 0x1000000
        return struct.pack("!4ssBBBB4s%ds" % datalength,
                               "ZBXD",
                               "\x01",
                               byte1,byte2,byte3,byte4,
                               "\x00\x00\x00\x00",
                               datajson)

    def __protocol_unpack__(self, datarecv):
        datalength = len(datarecv) - 13
        datajson, = struct.unpack("13x%ds" % datalength, datarecv)
        return json.loads(datajson)

    def __datarecv_print__(self, datarecv):
        for key in datarecv.keys():
            print "%s: %s" % (key, datarecv[key])

    def send(self, data, callback=None):
        '''
        data format like this:
        [
        {"host":hostname, "key":key, "value":value},
        {"host":hostname, "key":key, "value":value}
        ]
        '''

        datasend = self.__protocol_pack__(data)
        datarecv = ""

        buffersize = 65535
        self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
        self.tcpCliSock.settimeout(self.__timeout__)
        self.tcpCliSock.connect((self.__host__, self.__port__))

        self.tcpCliSock.send(datasend)
        while True:
            tempdata = self.tcpCliSock.recv(buffersize)
            if not tempdata:
                break
            datarecv += tempdata

        dataunpack = self.__protocol_unpack__(datarecv)
        if callback:
            callback(dataunpack)
        else:
            print self.__datarecv_print__(dataunpack)

        if self.tcpCliSock:
            try:
                self.tcpCliSock.close()
            except:
                self.tcpCliSock = None
        self.tcpCliSock = None
