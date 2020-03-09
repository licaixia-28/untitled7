# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/8

E-mail:530103946@qq.com

=================================


"""
from common.execute_mysql import ExecuteMysql

class DbExist(object):
	def dbexist(self, phone):
		# 实例话ExecuteMysql类
		emysql = ExecuteMysql()
		num = emysql.find_count("select * from member where MobilePhone=%s" % phone)
		if num:
			return 1
		else:
			return 0

if __name__ == '__main__':
	a = DbExist()
	b = a.dbexist(18317189352)
	print(type(b))