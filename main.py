# -*- coding: utf-8 -*-
import time
import unittest
# from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def suite():
    start_dir = "/var/lib/jenkins/workspace/SL_Regression_Test(Release)"
    top = ".\SL_Regression_Test(Release)"
    print(start_dir)
    suite = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern='*test.py', top_level_dir=None)
    return suite


if __name__ == '__main__':
    localtime = time.localtime(time.time())
    now = str(localtime.tm_year) + '.' + str(localtime.tm_mon) + '.' + str(localtime.tm_mday) + '.' + str(
        localtime.tm_hour) + '.' + str(localtime.tm_min)
    fp = open('/var/lib/jenkins/workspace/SL_Regression_Test(Release)/SL_Test_Report(%s).html' % now, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='{ SL_Test_Report }',
        # description='',
        description="wq"
    )
    suite = suite()
    runner.run(suite)
    fp.close()
    smtpserver = "smtp.qq.com"  # 发件服务器
    port = 465  # 端口
    sender = "64439772@qq.com"  # 发送端
    password = "pcsxctftwxkobgcb"
    sendto = "64439772@qq.com"
    title = "test-report"
    message = MIMEMultipart()
    username = "wangqian"
    message['From'] = username
    message['To'] = sendto
    message['Subject'] = Header(title, 'utf-8')
    message.attach(MIMEText('测试报告', 'plain', 'utf-8'))
    att3 = MIMEText(
        open('/var/lib/jenkins/workspace/SL_Regression_Test(Release)/SL_Test_Report(%s).html' % now, 'rb').read(),
        'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
    message.attach(att3)
    smtpObj = smtplib.SMTP_SSL(host=smtpserver, port=port)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
    smtpObj.login(sender, password)
    smtpObj.sendmail(sender, sendto, message.as_string())
    print("邮件发送成功！！！")
    smtpObj.quit()
