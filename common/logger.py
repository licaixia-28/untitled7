# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/2

E-mail:530103946@qq.com

=================================


"""
import logging
from logging.handlers import RotatingFileHandler
import os
import time

from common.dir_config import LOGS_DIR

# 定义日志输出的格式
# 时间、日志级别、代码所在的文件名、打印日志的当前函数、代码行号、日志信息
fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"

# 指定日期格式
date_fmt = '%a, %d %b %Y %H:%M:%S'
date_fmt1 = '%y %m %d %H:%M:%S'


# 将日志输出到控制台
handler_1 = logging.StreamHandler()

cur_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

log_name = LOGS_DIR + "/api_automation_{0}.log".format(cur_time)

# 将日志保存起来
handler_2 = RotatingFileHandler(log_name, backupCount=20, encoding="utf-8")

# 配置日志输出的格式
# format:使用指定字符串格式 datefmt：使用指定日期和时间的格式  level:日志输出的等级 handlers:
logging.basicConfig(format=fmt, datefmt=date_fmt, level=logging.INFO, handlers=[handler_1, handler_2])

if __name__ == '__main__':
    logging.info("哈哈")
    logging.debug("噢噢噢")
