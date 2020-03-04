# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/3

E-mail:530103946@qq.com

=================================


"""
from common.config import conf

host = conf.get("mysql", "host")
print(host)