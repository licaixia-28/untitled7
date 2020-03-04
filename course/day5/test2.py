# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/2

E-mail:530103946@qq.com

=================================


"""


class Book(object):
	# 定义类属性
	username = 'mt'
	# 这是初始化方法，类只要被调用就会执行此方法

	def __init__(self):
		print("这是初始化方法")
		# 将类属性username当成实例属性来调用
		print(self.username)

	# 使用装饰器@staticmethod,将该方法定义成一个静态方法，静态方式是不使用类属性和类方法的方法
	@staticmethod
	def add():
		print("这是加法")

	@classmethod
	def add1(cls):
		print("这是类方法")
		# 调用类属性
		print(cls.username)

	def add2(self):
		print("这是实例方法")
		print(self.username)

	def add3(self):
		print("这是实例方法3")
		self.add2()
		self.add1()


if __name__ == '__main__':
	# 实例化Book类给生成对象book
	book = Book()
	# 实例对象调用静态方法
	# book.add()
	# 直接调用类方法不会执行实例方法，之后执行类方法
	Book.add1()
	# 实例方法可调用类方法
	# book.add1()
	# book.add2()
	# book.add3()