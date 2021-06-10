#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from BeautifulReport import BeautifulReport
import Config.config as cf
from Common.send_email import SendMail
import unittest, os ,time

class RunALL(object):
    def __new__(cls, *args, **kwargs):
        '''单例模式'''
        if not (hasattr(cls, "_instance")):
            orign = super(RunALL, cls)
            cls._instance = orign.__new__(cls, *args, **kwargs)
        return cls._instance



    def all_tests(self,casename="Case", rule="test*.py"):
        curPath = os.path.realpath(__file__)
        parPath = os.path.dirname(curPath)
        rePath = os.path.join(parPath, casename)
        print(rePath)
        discover = unittest.defaultTestLoader.discover(rePath, pattern=rule)
        return discover

    def run(self,discover):
        reportPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"report/lyg_report")
        if not os.path.exists(reportPath):
            os.mkdir(reportPath)
        # reportPath = os.path.join(reportPath, "lyg_测试报告.html")
        # fp = open(reportPath, "wb")
        now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        filename = "lyg_自动化测试报告"+now
        runner = BeautifulReport(discover).report(filename=filename, description='web自动化测试报告', report_dir=reportPath)
        reportPath = os.path.join(reportPath,"{0}.html".format(filename))
        return reportPath



if __name__ == '__main__':
    r = RunALL()
    discover = r.all_tests()
    run = r.run(discover)
    s = SendMail(cf.host)
    # 运行后直接发送邮件
    s.send(cf.title,cf.content,cf.sender,cf.auth_code,cf.receiver,run)


