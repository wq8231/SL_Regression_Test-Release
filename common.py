import requests
import hashlib
import re
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class CommonClass():
    def getwebtoken(self, name, psw):  # 获取web端token
        url = 'http://yun.slothtek.com/base/api/out/v2/auth/login'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        data = {'name': name, 'password': psw, 'platform': 'WEB'}
        result = requests.session().post(url=url, headers=headers, data=data)
        token=re.findall("token=(.*?);", str(result.headers))  # 在返回头里找到token)
        return token
    def getpadtoken(self,name,psw):  # 获取pad端token
        url = 'http://bip.slothtek.com/api/v1/auth/login'
        headers = {
            'User-Agent': 'okhttp/3.6.0'}
        data = {'name': name, 'password': psw}
        result = requests.session().post(url=url, headers=headers, data=data)
        token = result.json()['data']['token']
        return token

    def _md5(self, psw):
        md5 = hashlib.md5()
        # psw=bytes(psw.encode('utf-8'))
        md5.update(psw.encode('utf-8'))
        md5psw = md5.hexdigest()
        return md5psw
    def sendemail(self,file):
        print("开始发送邮件")
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
            open(file, 'rb').read(),
            'base64', 'utf-8')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
        message.attach(att3)
        smtpObj = smtplib.SMTP_SSL(host=smtpserver, port=port)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, sendto, message.as_string())
        print("邮件发送成功！！！")
        smtpObj.quit()

