# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/7

E-mail:530103946@qq.com

=================================


"""
import random


class RandomPhone(object):
	# 获取随机手机号
	def randomphone(self, phone_head):
		self.phone = str(phone_head)
		for i in range(8):
			self.phone_end = random.randint(0, 9)
			self.phone += str(self.phone_end)
		# phone += random.randint(0, 9)
		return self.phone

	# 将随机手机号写入字典
	def writerandphone(self):
		rp = self.randomphone(139)
		dic = {"mobilephone": "15209847653", "pwd": "1234567", "regname": "user1"}
		dic["mobilephone"] = rp
		return dic