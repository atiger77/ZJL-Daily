# -*- coding: utf-8 -*-
import itchat
import datetime,time
'''
Time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
Time_set_ymd = time.strftime("%Y-%m-%d")
Time_set_hour = Time_set_ymd + " 22:24:00"
date1 = datetime.datetime.strptime('%s'%Time_now,'%Y-%m-%d %H:%M:%S')
date2 = datetime.datetime.strptime('%s'%Time_set_hour, '%Y-%m-%d %H:%M:%S')
'''
Time_set = datetime.datetime(2017,3,26,22,18,0)
itchat.auto_login(hotReload=True)

while datetime.datetime.now() == Time_set:   
    #send_msg(msg='离订加班餐还有%s分钟'%date3, toUserName=atiger77)
    send_msg(msg='提醒测试1', toUserName=atiger77)
    send_msg(msg='提醒测试2', toUserName=atiger77)
    send_msg(msg='提醒测试3', toUserName=atiger77)



