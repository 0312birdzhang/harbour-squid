#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import subprocess
import urllib
import pyotherside

#stop squid
def kill():
    p = subprocess.Popen('sh -c "echo asd10086 | devel-su -c /usr/local/squid/sbin/squid -k kill"',shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #0则安装成功
    retval = p.wait()
    code = p.returncode
    if code and code == 0:
        return True
    else:
        return False

#start squid
def start():
    p = subprocess.Popen('sh -c "echo asd10086 | devel-su -c /usr/local/squid/sbin/squid -s -f /usr/local/squid/etc/squid.conf"',shell=True)
    retval = p.wait()

#is running
def isrun():
    p = subprocess.Popen('sh -c "echo asd10086 | devel-su -c  ps -ef|grep squid.conf|grep -v grep|wc -l"',shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #0则安装成功
    wc = p.stdout.readlines()
    wc = wc[0].decode('utf-8').strip('\n')
    if "0" in wc:
        return False
    else:
        return True
