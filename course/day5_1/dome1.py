# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/7

E-mail:530103946@qq.com

=================================


"""
import os
import json

from common.config import conf
from common.dir_config import DATE_DIR
from common.read_excel import ReadExcel



file_name = conf.get("excel1", "file_name")
wb = ReadExcel(os.path.join(DATE_DIR, file_name), "login")
cases = wb.read_line_date()
for case in cases:
	a = case.request_data
b = json.loads(a)
print(type(b))
print(a)
