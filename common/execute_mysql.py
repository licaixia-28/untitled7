# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/3

E-mail:530103946@qq.com

=================================


"""
import pymysql
from common.config import conf


class ExecuteMysql(object):
	def __init__(self):
		# 连接数据库
		self.con = pymysql.connect(
			host=conf.get("mysql", "host"),
			port=conf.getint("mysql", "port"),
			user=conf.get("mysql", "user"),
			password=conf.get("mysql", "password"),
			database=conf.get("mysql", "database"),
			charset="utf8"
		)
		# 创建游标 使用游标来执行SQL语句
		self.cur = self.con.cursor()

	# 查询一条结果，如果查询到多个结果则只获取第一个结果，没有则返回None
	def find_one(self, sql):
		# 执行SQL语句
		self.cur.execute(sql)
		# 刷新数据并返回查询结果
		self.con.commit()
		return self.cur.fetchone()

	#查询多条结果
	def find_many(self, sql, num):
		# 执行SQL语句
		self.cur.execute(sql)
		# 刷新数据并返回查询结果
		self.con.commit()
		return self.cur.fetchmany(num)

	# 查询全部结果
	def find_all(self, sql):
		# 执行SQL语句
		self.cur.execute(sql)
		# 刷新数据并返回查询结果
		self.con.commit()
		return self.cur.fetchall()

	# 查询个数，没有则返回0
	def find_count(self, sql):
		count = self.cur.execute(sql)
		self.con.commit()
		return count


if __name__ == '__main__':
	db = ExecuteMysql()
	# 查询一条结果，查询结果有多条时只取第一条，没有时返回None
	sql = "select LeaveAmount from member where Id=90;"
	res = db.find_one(sql=sql)[0]
	print(res)
	# 查询多条结果
	# sql = "select * from member where Id>88;"
	# res = db.find_many(sql=sql, num=3)
	# print(res)
	# 查询全部结果,没有返回0
	# sql = "select * from member where Id<88;"
	# res = db.find_all(sql=sql)
	# print(res)
	# 查询个数,没有返回0
	# sql = "select * from member where Id<88;"
	# res = db.find_count(sql=sql)
	# print(res)






