# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/6

E-mail:530103946@qq.com

=================================


"""
import random

from common.execute_mysql import ExecuteMysql
from common.config import conf

# 从配置文件获取数据
file_name = conf.get("excel", "file_name")

class WritePhone():

	def random_phone(self, phone_head):
		phone = str(phone_head)
		for i in range(8):
			phone_end = random.randint(0, 9)
			phone += str(phone_end)
		# phone += random.randint(0, 9)
		return phone

	def dic(self):
		rp = self.random_phone(139)
		dic = {"mobilephone": "15209847653", "pwd": "1234567", "regname": "user1"}
		dic["mobilephone"] = rp
		return dic

	# def test(self):
	# 	self.db = ExecuteMysql()
	# 	wb = ReadExcel(os.path.join(DATE_DIR, file_name), "recharge")
	# 	cases = wb.read_line_date()
	# 	for case in cases:
	# 		if case.title == '正常充值':
	# 			sql_amount = self.db.find_one("select LeaveAmount from member where LeaveAmount>0 and RegTime > '2020-02-10'")
	# 			# amount = int(eval(case.request_data)["amount"]) + int(sql_amount[0])
	# 			# leaveamount = eval(case.expected_data)["data"]["leaveamount"]
	# 			# a = eval(case.expected_data)["data"]["leaveamount"]
	# 			# case.expected_data = case.expected_data.replace(a, str(amount))
	# 			print(sql_amount)









if __name__ == '__main__':
	db = ExecuteMysql()
	sql_amount = db.find_one("select LeaveAmount from member where LeaveAmount>0 and RegTime > '2020-02-10'")
	print(sql_amount)
	# import re
	# lists = os.listdir(REPORT_DIR)
	# lists.sort(key=lambda fn: os.path.getmtime(REPORT_DIR + '\\' + fn))
	# for path in lists:
	# 	full_path = os.path.join(REPORT_DIR, path)
	# 	# print(full_path)
	# file = os.path.join(REPORT_DIR, list[-1])

	# s = ['a.dat', 'c.dat', 'b.dat']
	# new = sorted(lists, key=lambda i:int(re.match(r'(\d+)', i).group()))
	# print(new)