#!/usr/bin/env python
#coding:utf-8
import re,sys,datetime,requests,codecs

#Define
#LogFile_Location = "/data/soft/Anti_platform/Geo_Findout/logs"
DateTime =  datetime.datetime.now()
DateTime_Format = DateTime.strftime('%Y%m%d')
#免费手机号码归属地API查询接口
#http://www.tuicool.com/articles/mMjAf2
Phone_Geo = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel="
IP_Geo = "http://ip.taobao.com/service/getIpInfo.php?ip="


def Geo_PhoneNum_Findout(INPUT):
    now_format = DateTime.strftime('%Y-%m-%d %H:%M:%S')
    r = requests.get("%s%s" % (Phone_Geo,INPUT))
    print  r.text

def Geo_IP_Findout(INPUT):
    now_format = DateTime.strftime('%Y-%m-%d %H:%M:%S')
    r = requests.get("%s%s" % (IP_Geo,INPUT))
    response = r.json()
    print response["data"]["country"],response["data"]["area"],response["data"]["region"],response["data"]["city"]


if __name__ == '__main__':
    try:
        INPUT = sys.argv[1]
        if "." in INPUT:
            Geo_IP_Findout(INPUT)
        else:
            Geo_PhoneNum_Findout(INPUT)
    except Exception,e:
        print "eg: python Geo_Findout.py 1.2.3.4 OR python Geo_Findout.py 13888888888"
        #print e  
