# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/2/28

E-mail:530103946@qq.com

=================================


"""
# a = input("请输入文本：")
# print("你输入的文本是:",a)
# print(type(a))
# b = int(a)
# print(type(b))

# 数据类型字典
dic1 = {"username": "lcx", "age": 18}
dic2 = {"username1": "LCX", "password": 123456}
# 数据字典的另外一种方式
ase_dict = dict(key1="lcx", key2=2, key3="value3")
# 获取字典键值
username = dic1["username"]
username1 = dic1.get("username1")
# 修改字典键值，有则修改无则新增
dic1["age"] = 20
# 删除字典值
# dic1.pop("age")
# 删除键值从末尾开始删
# dic1.popitem()

# 提取dic1的键给dic3
dic3 = dic1.keys()
# 提取dic1的值给dic4
dic4 = dic1.values()
print(dic4)
# 将字典a的键值添加到dic
dic1.update(dic2)

# 格式化键值
# print("姓名:{},年龄：{}".format(dic1.get("username"), dic1.get("age")))
# print("姓名：%s,年龄：%s" % (dic1.get("username"), dic1.get("age")))


# 定义空字典，插入键值对
# dic1 = dict()
dic1 = {}
dic1["username"] = "lcx"
dic1["password"] = 123456


# 格式化输出

# print("目标人物的名字:{} ,目标人物的年龄：{}".format(username, age))
# print("目标人物的名字:%s ,目标人物的年龄：%s" % (username, age))
# print(dic1)
