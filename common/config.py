# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/3

E-mail:530103946@qq.com

=================================


"""
import configparser
import os
from common.dir_config import CONF_DIR


# 配置执行环境
class ReadConfig(configparser.ConfigParser):
	def __init__(self):
		# 调用父类的init方法
		super().__init__()
		# 读取配置文件，读取后就可以使用conf.get()获取数据
		self.read(os.path.join(CONF_DIR, "env.ini"), encoding="utf8")
		version = self.get("env", "version")
		if version == "test":
			self.read(os.path.join(CONF_DIR, "config_test.ini"), encoding="utf8")
		elif version == "produce":
			self.read(os.path.join(CONF_DIR, "config_produce.ini"), encoding="utf8")


conf = ReadConfig()

if __name__ == '__main__':
	host = conf.get("mysql", "host")
	print(host)

