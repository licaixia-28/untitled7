# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/4

E-mail:530103946@qq.com

=================================


"""
import requests
from requests.sessions import Session
import logging
from common import logger


# 不记录cookies信息给下一次使用
class HTTPRequest1(object):
	def request(self, method, url, params=None, data=None, headers=None, cookies=None, json=None):
		# 将字符串里的大写转换成小写
		method = method.lower()
		if method == "post":
			# 判断是否使用json传参
			if json:
				logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, json))
				return requests.post(url=url, json=json, headers=headers, cookies=cookies)
			else:
				logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, data))
				return requests.post(url=url, data=data, headers=headers, cookies=cookies)
		elif method == "get":
			logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, params))
			return requests.get(url=url, params=params, headers=headers, cookies=cookies)


class HTTPRequest(object):
    """记录cookies信息给下一次请求使用"""

    def __init__(self):
        # 创建session对象
        self.session = Session()

    def request(self, method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):

        method = method.lower()
        if method == "post":
            # 判断是否使用json来传参（适用于接口项目有使用json传参）
            if json:
                logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, json))
                return self.session.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, data))
                return self.session.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == "get":
            logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, params))
            return self.session.get(url=url, params=params, headers=headers, cookies=cookies)

    def close(self):
        self.session.close()


if __name__ == '__main__':
	# logging.info("kk")
	httprequest = HTTPRequest1()
	url = "http://118.24.221.133:8081/futureloan/mvc/api/member/login"
	method = "post"
	data = {'mobilephone': '', 'pwd': '123456'}
	response = httprequest.request(method=method, url=url, data=data)
	print(response.status_code)
	print(response.json())


