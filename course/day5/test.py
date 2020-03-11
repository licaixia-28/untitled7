# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/10

E-mail:530103946@qq.com

=================================


"""
from common.execute_mysql import ExecuteMysql

if __name__ == '__main__':

	db = ExecuteMysql()
	sql_amount = db.find_one("select LeaveAmount from member where LeaveAmount>0 and RegTime > '2020-02-10'")
	print(type(sql_amount[0]))