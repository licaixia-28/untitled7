# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/1

E-mail:530103946@qq.com

=================================


"""
import os


# python执行命令行窗口下的命令
# os.system("ls")
# os.system("pwd")


# a = os.path.abspath(__file__)
# print(a)
# b = os.path.split(os.path.abspath(__file__))[0]
# c = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(c)
# i = 0
# while i < 10:
# 	print(i)
# 	i += 1

# 定义类
class LoginPage(object):
	# 定义属性
	username = 'tu'

	# 定义类方法
	@classmethod
	def login(self, num):
		res = num+10
		return res

	def demo(self, num):
		res = num+100
		return res

	def dem_table(self):
		for i in range(1, 10):
			for j in range(i, 10):
				print("{}*{}={}".format(i, j, i * j), end=" ")
			print("")


if __name__ == '__main__':
		for i in range(1, 10):
			for j in range(1, i+1):
				print("{}*{}={}".format(j, i, i * j), end="\t")
			print()





