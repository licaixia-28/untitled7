# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/5

E-mail:530103946@qq.com

=================================


"""
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.config import conf
from common.dir_config import CASE_DIR, REPORT_DIR
from common.send_email import SendEmail
import os
import time


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
