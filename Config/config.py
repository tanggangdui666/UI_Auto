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