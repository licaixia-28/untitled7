# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/6

E-mail:530103946@qq.com

=================================


"""
import random
from common.read_excel import ReadExcel
import os
from common.dir_config import DATE_DIR
from common.dir_config import REPORT_DIR

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







if __name__ == '__main__':
	import re
	lists = os.listdir(REPORT_DIR)
	# lists.sort(key=lambda fn: os.path.getmtime(REPORT_DIR + '\\' + fn))
	# for path in lists:
	# 	full_path = os.path.join(REPORT_DIR, path)
	# 	# print(full_path)
	# file = os.path.join(REPORT_DIR, list[-1])

	# s = ['a.dat', 'c.dat', 'b.dat']
	new = sorted(lists, key=lambda i:int(re.match(r'(\d+)', i).group()))
	print(new)