# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/2/29

E-mail:530103946@qq.com

=================================


"""

# 列表
list1 = ['python', 'tudou', 'kkkk', 'python']
list2 = [1, 2, 3]
# 在位置0插入45
# list1.insert(0, 45)
# 将列表2的内容插入列表1
# list1.extend(list2)
# 往最后面的位置插入值
# list1.append("lcx")
# 指定下标删除，不传值默认删除最后一个
# list1.pop()
# 删除指定下标的值
# del list1[0]
# 清空所有元素
# list1.clear()
# list1.remove('python')
# 修改元素值
# list1[0] = "ppp"
# 统计元素值的个数
# a = list1.count("python")
print(list1)
# 查询长度
# b = len(list1)
# 最小值
# c = min(list2)
# 查找元素返回下标
# d = list1.index('tudou')
# 将列表倒叙处理
# list2.reverse()
# 复制列表
# list3 = list2.copy()
# list2.sort(reverse=True)

# for i in list1:
# 	if i == 'python':
# 		list1.remove(i)
# list1.insert(1, 'a')
# list1.extend(list2)
# list2.reverse()
# print(list1)

# list3 = [0, 8, 1, 3, 2]
# list3.sort(reverse=True)
# print(list3)



# score = int(input("请输入分数："))
# if score < 60:
# 	print("成绩不及格，当前成绩为：%s" % score)
# elif 60 <= score < 70:
# 	print("成绩合格，当前成绩为：%s" % score)
# elif 70 <= score < 80:
# 	print("成绩良好，当前成绩为：%s" % score)
# elif 80 <= score < 100:
# 	print("成绩优秀，当前成绩为：%s" % score)
# else:
# 	print("成绩特别优秀")

# while True:
# 	score = eval(input("请输入您的成绩："))
# 	# print(type(score))
# 	# if type(score) not in (int, float):
# 	# 	print("您的输入有误，请重新输入")
# 	# elif score >= 100:
# 	# 	print("您的成绩特别优秀")
# 	# elif score >= 80:
# 	# 	print("您的成绩为优秀")
# 	# elif score >= 70:
# 	# 	print("您的成绩为良好")
# 	# elif score >= 60:
# 	# 	print("您的成绩为及格")
# 	# else:
# 	# 	print("您的成绩不合格")


a = 0.5
print(type(a))
b = "1.0"
print(type(b))
print(type(eval(b)))
c = "[1,2,3,4,5]"
print(type(c))
print(type(eval(c)))








