#!/usr/bin/env python
#coding=utf-8
import sys
import requests
ip = list(sys.argv)[1]
ak = 'your own key'
url = "http://api.map.baidu.com/highacciploc/v1?qcip="+ip+"&qterm=pc&ak="+ak+"&coord=bd09ll&extensions=1"
r = requests.get(url)
a =  r.json()
if a.has_key('content'):
    print a['content']['formatted_address']
else:
    print "输入IP未能找到位置。"
