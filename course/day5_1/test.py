# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/2

E-mail:530103946@qq.com

=================================


"""
from course.day5.test2 import Book
import logging


# 类的继承
class Test(Book):
	def demo(self):
		self.add()


if __name__ == '__main__':
	test = Test()
	test.demo()
	logging.info("理论")

