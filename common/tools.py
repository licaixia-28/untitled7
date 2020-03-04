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

def time_custom(before_year=None, before_month=None, before_days=None, before_hours=None, before_minute=None, now=None):
	time_style = "%Y-%m-%d %H:%M"
	now = datetime.datetime.now()
	# if before_year:
	delta = datedelta.datedelta(years=before_year, months=before_month)
	before = now - delta
	return before.strftime(time_style)


if __name__ == '__main__':
	now = time_custom(before_year=1, before_month=1)
	print(type(now))
	print(now)