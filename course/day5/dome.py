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
	wp = WritePhone()
	phone = wp.dic()
	print(phone)