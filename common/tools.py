# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/1

E-mail:530103946@qq.com

=================================


"""
import time
import datetime
import datedelta
import random
import os

from common.read_excel import ReadExcel
from common.dir_config import DATE_DIR
from common.config import conf
from common.execute_mysql import ExecuteMysql

# 从配置文件获取数据
def time_custom(before_year=None, before_month=None, before_days=None, before_hours=None, before_minute=None, now=None):
	time_style = "%Y-%m-%d %H:%M"
	now = datetime.datetime.now()
	# if before_year:
	delta = datedelta.datedelta(years=before_year, months=before_month)
	before = now - delta
	return before.strftime(time_style)


def random_phone(phone_head):
	phone = str(phone_head)
	for i in range(8):
		phone_end = random.randint(0, 9)
		phone += str(phone_end)
	# phone += random.randint(0, 9)
	return phone


# 将随机手机号写入字典
def writer_and_phone(self):
	rp = self.randomphone(139)
	dic = {"mobilephone": "15209847653", "pwd": "1234567", "regname": "user1"}
	dic["mobilephone"] = rp
	return dic


# 自动替换手机号方法
def replace_data(tittle, request_data):
	mobilephone = eval(request_data)["mobilephone"]
	if str(tittle) == "正常注册":
		phone = random_phone(mobilephone[-3:])
	elif str(tittle) == "手机号码已存在":
		db = ExecuteMysql()
		# 查询一条结果，查询结果有多条时只取第一条，没有时返回None
		res = db.find_one(sql="select * from member;")
		# 取查询结果里面的手机号
		phone = res[3]
	# 用取的手机号替换用例里面的号段
	request_data = request_data.replace(mobilephone, phone)
	return request_data



if __name__ == '__main__':
	tittle ="正常注册"
	request_data ="{'mobilephone': 'phone183', 'pwd': '1234567', 'regname': 'user1'}"
	replace_data = replace_data(tittle, request_data)
	print(replace_data)

