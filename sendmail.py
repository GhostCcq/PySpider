#!/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.exmail.qq.com'
mail_user = 'xxxx@qq.com'
mail_paas = '123456'

sender = 'xxxx@qq.com'
receivers = [
    'xxxx@qq.com'
]

message = MIMEText('Python 邮件测试发送~~~', 'plain', 'utf-8')
message['From'] = Header('chenquan@esharex.com', 'utf-8')
message['To'] = Header('friend', 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8').encode()

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_paas)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except Exception as e:
    print(e)
    print('邮件发送失败')