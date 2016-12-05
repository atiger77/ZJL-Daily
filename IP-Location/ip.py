#!/usr/bin/env python
#coding=utf-8
import sys
import requests

def ip_location(ip):
    #ak = 'your own key'
    ak = 'jIxP1eOG5e6a48shWbEFOd5UxVvZ18Fn'
    url = "http://api.map.baidu.com/highacciploc/v1?qcip="+ip+"&qterm=pc&ak="+ak+"&coord=bd09ll&extensions=1"
    r = requests.get(url)
    a =  r.json()
    if a.has_key('content'):
        print a['content']['formatted_address']
    else:
        print "输入IP未能找到位置。"


if __name__ == '__main__':
    try:
        ip = list(sys.argv)[1]
        ip_location(ip)
    except IndexError:
        print "eg: python ip.py 1.2.3.4"

