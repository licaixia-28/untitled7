import os
import random


def random_ip():
	# a = 3
	# b = 3 ** 2
	# print("hello world")
	# print(a, b)
	ip = "{}.{}.{}.{}".format(random.randint(0, 255), random.randint(0, 255),
	                          random.randint(0, 255), random.randint(0, 255))
	# 字符串的格式化输出
	return ip




# 传入指定号段获取随机手机号
def random_phone(phone_head):
	phone = str(phone_head)
	for i in range(8):
		phone_end = random.randint(0, 9)
		phone += str(phone_end)
	return phone


# 冒泡排序1
def order_by():
	a = [1, 3, 4, 0, 9, 0, 2]
	for f in range(7):
		for i in range(7-f-1):
				if a[i] >= a[i+1]:
					t = a[i]
					a[i] = a[i+1]
					a[i+1] = t
	return a

def order_by1():
	a = [1, 3, 4, 0, 9]
	for i in range(4):
		j = i+1
		for  j in range(4):
				if a[i] >= a[j]:
					t = a[i]
					a[i] = a[j]
					a[j] = t
				print(a)

if __name__ == '__main__':
	# ip = random_ip()
	# print(ip)
	# phone = random_phone(139)
	# print(phone)
	# a=10
	# for i in range(10):
	# 	a -= 1
	# print(a)

	a = order_by()
	print(a)