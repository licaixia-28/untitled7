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

REPORT_DIR = os.path.join(BASE_DIR, "output/report")

LOGS_DIR = os.path.join(BASE_DIR, "output/logs")

SCREEN_SHOT_DIR = os.path.join(BASE_DIR, "output/screen_shots")

CONF_DIR = os.path.join(BASE_DIR, "conf")


if __name__ == '__main__':
	print(BASE_DIR)
	print(DATE_DIR)
	print(LOGS_DIR)
	print(CONF_DIR)