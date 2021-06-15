#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import os,time

# 获取当前执行脚本的绝对路径
curPath = os.path.realpath(__file__)
# 返回一个目录的目录名
parPath = os.path.dirname(curPath)
projectPath = os.path.dirname(parPath)

# 截图保存路径
screenPath = os.path.join(projectPath, "screenshots")
if not os.path.exists(screenPath):
    os.mkdir(screenPath)
nowtime = time.strftime("%Y%m%d_%H_%M_%S", time.localtime())
screenName = os.path.join(screenPath, "%s.png" % nowtime)


# borwser.ini文件路径
bsConfing = os.path.join(projectPath, "Config", "browser.ini")

# 礼物素材参数
name = "ssm"
img1 = "/Users/lyg/Desktop/material/{0}/{0}1.png".format(name)
img2 = "/Users/lyg/Desktop/material/{0}/{0}2.png".format(name)
img3 = "/Users/lyg/Desktop/material/{0}/{0}3.png".format(name)
img = "/Users/lyg/Desktop/material/{0}/{0}.png".format(name)
app_id = "捞月狗"
gift_id = 100007
gift_name = "上传图片测试7"
gift_describe = "新礼物配置"
gift_explain = "测试"
value_type = "狗粮"  #狗粮 无价值 碎片
value_gl = 999
gift_time = 90
gift_grade = "普通礼物" #普通礼物 全屏礼物
gift_sort = 1
gift_type = "面板礼物" #面板礼物 背包 全部



# email参数
sender = 'ggboytgg@163.com'
# 授权码不是邮箱登录密码，网易邮箱可以通过 "设置"->客户端授权密码，
auth_code = "CJTKWQUKTDXNLOSP"
host = "smtp.163.com"
# port = 465
receiver = ['ggboytgg1@163.com', 'ggboytgg2@163.com']
title = "邮件主题"
content = "UI自动化测试报告邮件已发送，详情请查看附件。"
# reportPath = os.path.join(projectPath, "report", "result.html")
# off = 1  # 发送开关


# logger参数
logPath = os.path.join(projectPath, "report","log")
logName = os.path.join(logPath,"out.log")

# excek文件路径
login_testdata = os.path.join(projectPath, "data")
if not os.path.exists(login_testdata):
    os.mkdir(login_testdata)
login_testdata =os.path.join(login_testdata, "login_testdata.xls")
login_sheet = "Sheet1"



if __name__ == '__main__':
    # print(logName)
    # print(login_testdata)
    import time

    nowtime = time.strftime("%Y%m%d_%H_%M_%S", time.localtime())
    print(screenName)
    print(img1,img,img2,img3)