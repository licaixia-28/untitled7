# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/1

E-mail:530103946@qq.com

=================================


"""
import os


BASE_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

DATE_DIR = os.path.join(BASE_DIR, "data")

CONF_DIR = os.path.join(BASE_DIR, "conf")

REPORT_DIR = os.path.join(BASE_DIR, "report")

LOGS_DIR = os.path.join(BASE_DIR, "logs")

CASE_DIR = os.path.join(BASE_DIR, "test_cases")



if __name__ == '__main__':
	print(LOGS_DIR)
