# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/1

E-mail:530103946@qq.com

=================================


"""
from course.day4 import LoginPage as Lp

# 获取类属性
username = Lp.username
print(username)

# 调用类的类方法，该方法必须加上@classmethod
res = Lp.login(num=1)
print(res)

# 调用类的一般方法必须先实例化类获取对象
lp = Lp()
res = lp.demo(1)
print(res)

username = lp.username
print(username)

