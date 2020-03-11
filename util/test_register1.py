# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/8

E-mail:530103946@qq.com

=================================


"""

# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/3

E-mail:530103946@qq.com

=================================


"""
import unittest
import os
import logging
import time

from common.read_excel import ReadExcel
from common.http_request import HTTPRequest
from common.execute_mysql import ExecuteMysql
from common.dir_config import DATE_DIR, REPORT_DIR
from common.config import conf
from library.ddt import ddt, data
from common.tools import replace_data

# 从配置文件获取数据
file_name = conf.get("excel", "file_name")


@ddt
class RegisterTestCase(unittest.TestCase):

	# 拼接完整的excel路径，读取excel
	wb = ReadExcel(os.path.join(DATE_DIR, file_name), "register")
	cases = wb.read_line_date()


	@classmethod
	def setUpClass(cls):
		logging.info("==================== 准备开始执行注册接口测试 ====================")
		cls.request = HTTPRequest()
		cls.db = ExecuteMysql()

	@classmethod
	def tearDownClass(cls):
		logging.info("==================== 注册接口测试执行完毕====================")
		cls.request.close()

	# 拆包
	@data(*cases)
	def test_register(self, case):
		url = conf.get("env", "url") + case.url
		self.row = case.case_id + 1
		request_data = replace_data(case.request_data)
		response = self.request.request(method=case.method, url=url, data=eval(request_data))

		print()
		print("请求地址：{}".format(url))
		print("请求数据：{}".format(request_data))
		print("期望结果：{}".format(case.expected_data))
		print("服务器响应数据：{}".format(response.json()))

		res = response.json()

		# 查询数据库进行断言
		# phone = eval(request_data)["mobilephone"]
		# count = self.db.find_count("select * from member where MobilePhone=%s;" % phone)
		# self.assertEqual(count, 1)
		# AssertionError
		try:
			# 比较预期结果与实际返回的结果，类型不同不能比较，所以需要用eval转换下格式
			self.assertEqual(eval(case.expected_data), res)
		except AssertionError as e:
			result = "FAIL"
			logging.exception(e)
			raise
		else:
			result = "PASS"
			logging.info("预期结果是：{}, 实际结果是：{},测试通过".format(case.expected_data, res))
		finally:
			self.wb.write_date(self.row, 9, str(res))
			self.wb.write_date(self.row, 10, result)





if __name__ == '__main__':
	pass

# if __name__ == '__main__':
	# file_name = conf.get("excel", "file_name")
	# print(file_name)
	# host = conf.get("mysql", "host")
	# print(host)
	# data_dir = os.path.join(DATE_DIR, "api_automation.xlsx")
	# print(data_dir)