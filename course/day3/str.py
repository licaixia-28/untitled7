# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/2/29

E-mail:530103946@qq.com

=================================


"""


# 字符串 str
str1 = '2'
str2 = "hCx"
str3 = '("土豆")'
str4 = "('馒头.123')"
# 将字符串全部转换为大写
# str5 = str1.upper()
# 将字符串全部转换为小写
# str5 = str2.lower()
# 去除字符
# str5 = str4.rstrip()
# 查找元素
# str5 = str1.find('c')
# 替换字符,将str1中的c替换成12
# str5 = str1.replace('c', '12')
# str5 = str1.join("lcx,hj")
str5 ="88".join("licaixia")
print(str5)
# print("字符串2的内容是：{}, 类型是：{}, 长度是：{}".format(str2, type(str2), len(str2)))
# print("字符串3的内容是：{}, 类型是：{}, 长度是：{}".format(str3, type(str3), len(str3)))
# print("字符串4的内容是：{}, 类型是：{}, 长度是：{}".format(str4, type(str4), len(str4)))
# 字符串切片
str6 = '012345678910'
# 取值左闭右开
a = str6[0:15]
b = str6[0:13:2]
# print(a)