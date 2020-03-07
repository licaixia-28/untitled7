# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/7

E-mail:530103946@qq.com

=================================


"""
import os

from common.execute_mysql import ExecuteMysql
from common.random_phone import RandomPhone
from common.read_excel import ReadExcel
from common.dir_config import DATE_DIR
from common.config import conf
from library.ddt import ddt, data

file_name = conf.get("excel", "file_name")


class SqlAssertion(object):
	wb = ReadExcel(os.path.join(DATE_DIR, file_name), "register")
	cases = wb.read_line_date()

	def phone(self):
		for case in self.cases:
			request_data = eval(case.request_data)
			row = case.case_id
			print(row)
		# 将参数值里的手机号码提取出来给phone
		phone = request_data.get("mobilephone")
		print(phone)
		return phone, row

	def sqlassertion(self):
		# 实例话执行用例的类
		self.executemysql = ExecuteMysql()
		# 取excle里的手机号码
		sqlresult = self.executemysql.find_one("select * from member where MobilePhone = %s;" % self.phone()[0])
		print(sqlresult)
		if sqlresult:
			self.wb.write_date(int(self.phone()[1]+1), 11, "数据库插入数据成功")
		else:
			self.wb.write_date(int(self.phone()[1]+1), 11, "数据库插入数据失败")


if __name__ == '__main__':
    a = SqlAssertion()
    b = a.sqlassertion()
    print(b)

