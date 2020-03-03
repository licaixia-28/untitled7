# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/2

E-mail:530103946@qq.com

=================================


"""
def demo(num1, num2, num3):
	print(num1)
	print(num2)
	print(num3)


def demo1(num, *args, **kwargs):
	print(num)
	print(args)
	print(kwargs)


if __name__ == '__main__':
	# dum = (1, 2, 3)
	# demo(*dum)
	demo1(1, *(2, 3, 4), **{"username": "土豆"})

