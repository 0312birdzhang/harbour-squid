#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import subprocess
import urllib
import pyotherside

#stop squid
def kill():
    p = subprocess.Popen("ps -ef|grep squid|grep -v grep|awk '{print $2}'|xargs kill -9",shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #0则安装成功
    retval = p.wait()
    code = p.returncode
    if code and code == 0:
        return True
    else:
        return False

#start squid
def start():
    p = subprocess.Popen(" /usr/local/squid/sbin/squid -s -f /usr/local/squid/etc/squid.conf",shell=True)
    retval = p.wait()

#is running
def isrun():
    p = subprocess.Popen("ps -ef|grep squid|grep -v grep|wc -l",shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #0则安装成功
    wc = p.stdout.readlines()
    wc = wc[0].decode('utf-8').strip('\n')
    if "0" in wc:
        return False
    else:
        return True
