# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/4

E-mail:530103946@qq.com

=================================


"""
import openpyxl


class Case(object):
    # 用这个类来存储用例 attrs为一个zip对象 excel的sheet中有几行 就返回几个zip对象
    def __init__(self, attrs):
        """
        初始化用例
        :param attrs: zip类型--> [（key1,value1),（key2,value2)....]
        """
        # item遍历所有zip对象 并获取每个zip对象内部的所有元素 返回tuple example: ('title', '正常登录')
        for item in attrs:
            # 将key-value组装起来,将第一参数变成属性名，第二个参数变成属性对应的值
            setattr(self, item[0], item[1])


class ReadExcel(object):

	def __init__(self, file_name, sheet_name):
		self.file_name = file_name
		self.sheet_name = sheet_name

	def open(self):
		# 打开工作簿传入指定的文件名
		self.wb = openpyxl.load_workbook(self.file_name)
		# 选取表单传入指定的表单
		self.sheet = self.wb[self.sheet_name]

	def close(self):
		self.wb.close()

	def read_line_date(self):
		# 打开工作薄
		self.open()
		# 按行获取数据并转换成列表
		rows_date = list(self.sheet.rows)
		# print(rows_date)

		# 获取表单的表头信息
		titles = []
		# print(rows_date[0])
		for title in rows_date[0]:
			# 对title的值是否为空做判断，容错机制
			if title.value:
				titles.append(title.value)
		# print(titles)

		# 定义一个空列表来存储测试用例数据
		cases = []
		# print(rows_date[1:-1])
		# 从第二行开始就是测试用例数据
		for case in rows_date[1:]:
			# date用来临时存放每行的用例数据
			date = []
			for cell in case:
				date.append(cell.value)
			# 将title与测试用例组合形成每行测试用例，一行行读取无需加list
			case_date = zip(titles, date)
			# print(case_date)
			# 创建一个Case类的对象用来保存用例数据
			case_obj = Case(case_date)
			# 将该条数据放入cases中
			cases.append(case_obj)
		# 关闭工作薄
		self.close()
		return cases

	def write_date(self, row, column, value):
		# 打开工作薄
		self.open()
		# 指定位置写入数据
		self.sheet.cell(row=row, column=column, value=value)
		# 保存数据
		self.wb.save(self.file_name)
		# 关闭工作薄
		self.close()


if __name__ == '__main__':
	from common.dir_config import DATE_DIR
	import os
	readexcel = ReadExcel(os.path.join(DATE_DIR, "api_automation.xlsx"), "login")
	cases = readexcel.read_line_date()
	# print(cases)
	# for case in cases:
	# 	print(case.api_name, case.url)
	# readexcel.write_date(4, 1, "看看")


