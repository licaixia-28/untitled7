# -*- coding: utf-8 -*-
"""

=================================
Author: LCX
Created on: 2020/3/2

E-mail:530103946@qq.com

=================================


"""
import smtplib
from email.mime.text import MIMEText        # 构造邮件文本内容
from email.header import Header      # 构造邮件标题
from email.mime.application import MIMEApplication      # 发送带附件的邮件
from email.mime.multipart import MIMEMultipart      # 发送带附件的邮件


class SendEmail(object):
	@staticmethod
	def send_qq_file_email(title, message, file_path):

		# 创建一个smtp对象，并连接smtp服务
		s = smtplib.SMTP_SSL("smtp.qq.com", 465)

		# 登录SMTP服务器
		msg_from = "1454491097@qq.com"
		password = "dwwdbapbcqgmbadh"
		msg_to = ["530103946@qq.com", "281831647@qq.com"]
		s.login(user=msg_from, password=password)


		# 构建邮件内容
		# 创建一个邮件文本类型
		content = MIMEText(message, _charset="utf8")

		# 构建附件
		part = MIMEApplication(open(file_path, "rb").read(), _subtype=False)
		part.add_header('content-disposition', 'attachment', filename='report18.html')

		# 封装邮件，添加邮件主题
		msg = MIMEMultipart()

		# 添加文本内容和附件
		msg.attach(content)
		msg.attach(part)

		msg['Subject'] = Header(title, 'utf-8')
		msg['From'] = msg_from  # 可以修改成任意名称
		msg['To'] = ','.join(msg_to)

		# 发送邮件
		try:
			s.sendmail(from_addr=msg_from, to_addrs=msg["To"].split(','), msg=msg.as_string())
			print("Send qq_email successfully")
		except Exception as e:
			print("Send qq_mail failed")
			raise e
		finally:
			s.quit()



if __name__ == '__main__':
	import os
	from common.dir_config import LOGS_DIR
	file_path = os.path.join(LOGS_DIR, "api_automation_2020-03-02 15:05.log")
	print(file_path)
	SendEmail.send_qq_file_email("测试邮件", "测试邮件", file_path=file_path)

