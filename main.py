# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/5

E-mail:530103946@qq.com

=================================


"""
import unittest
import os
import time

from library.HTMLTestRunnerNew import HTMLTestRunner
from common.config import conf
from common.dir_config import CASE_DIR, REPORT_DIR, DATE_DIR
from common.send_email import SendEmail
from common.dir_config import LOGS_DIR
from common.read_excel import ReadExcel


_title = "api_report"
_description = "这是第一份测试报告"
_tester = "tester"
report_name = 'report.html'
report_name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + "_" + report_name
# mail_title = conf.get('mail', 'mail_title')
# mail_message = conf.get('mail', 'mail_message')
file_path = os.path.join(REPORT_DIR, report_name)

suite = unittest.TestSuite()  # 创建测试集合
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))


with open(file_path, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title=_title,
        description=_description,
        tester=_tester
    )
    runner.run(suite)


file_name = conf.get("excel", "file_name")
wb = ReadExcel(os.path.join(DATE_DIR, file_name), "register")
cases = wb.read_line_date()
for case in cases:
     pass

# 发送邮件
sendemail = SendEmail()
file_path = os.path.join(REPORT_DIR, report_name)
sendemail.send_qq_file_email(cases.interface, cases.title, file_path=file_path)

