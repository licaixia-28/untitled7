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
import json

from common.read_excel import ReadExcel
from common.dir_config import DATE_DIR
from common.config import conf
from common.execute_mysql import ExecuteMysql
from common.http_request import HTTPRequest

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
def replace_data(request_data):
	db = ExecuteMysql()
	mobilephone = eval(request_data)["mobilephone"]
	if "#phone" in request_data:
		phone = random_phone(mobilephone[-3:])
		request_data = request_data.replace(mobilephone, phone)
	elif "exist" in request_data:
		# 查询一条结果，查询结果有多条时只取第一条，没有时返回None
		res = db.find_one(sql="select * from member where LeaveAmount>0 and RegTime > '2020-02-10';")
		# 取查询结果里面的手机号
		phone = res[3]
		request_data = request_data.replace(mobilephone, phone)
	elif "#amount" in request_data:
		res = db.find_one(sql="select LeaveAmount from member where LeaveAmount>0 and RegTime > '2020-02-10';")
		amount = int(res[0])+1000
		excel_amount = eval(request_data)["amount"]
		request_data = request_data.replace(excel_amount, str(amount))
	return request_data


def sql_amount(title):
	db = ExecuteMysql()
	if title in ("正常充值", "正常提现"):
		sql_amount = db.find_one("select leaveamount from member where MobilePhone=13941387738")
		amount = sql_amount[0]
		# leaveamount = eval(case.expected_data)["data"]["leaveamount"]
		return amount


def token():
	request = HTTPRequest()
	method = 'post'
	url = conf.get("env", "url1") + '/admin/login'
	request_data = '{"password": "123456", "username": "ceshijiagoushi"}'
	response = request.request(method=method, url=url, json=json.loads(request_data))
	token = response.json()["data"]["token"]
	return token






# 登录方法
def login(method, url, data):
	request = HTTPRequest()
	request.request(method=method, url=url, data=data)



if __name__ == '__main__':
	file_name = conf.get("excel", "file_name1")
	wb = ReadExcel(os.path.join(DATE_DIR, file_name), "search")
	cases = wb.read_line_date()
	request = HTTPRequest()
	token1 = token()
	for case in cases:
		url = case
		case.headers = case.headers.replace('#token', token1)
		response = request.request(method=case.method, url=url, json=json.loads(case.request_data))
		print(response)







