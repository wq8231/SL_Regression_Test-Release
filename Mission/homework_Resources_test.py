import requests
import re
import unittest
from common import CommonClass
import math
import os


class BaseStuTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.tchmd5psw = CommonClass()._md5('123456')  #
        self.tchname = '27717'
        self.tchtoken = CommonClass().getpadtoken(self.tchname, self.tchmd5psw)
        self.stumd5psw = CommonClass()._md5('111111')
        self.stuname = '27819'
        # self.token = '6cb42a26500049bc98d28689d5fc0137'
        self.stutoken = CommonClass().getpadtoken(self.stuname, self.stumd5psw)
        self.stuheaders = {
            'token': self.stutoken,
            'userid': self.tchname,
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'okhttp/3.6.0'}
        self.tchheaders = {
            'token': self.tchtoken,
            'userid': self.stuname,
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'okhttp/3.6.0'}

    def test_01(self):
        url = "http://api.slothtek.com/api/v1/file/uptoken?filename=Screenshot_20200225_212851_com.tencent.mm.jpg"
        headers = {
            'User-Agent': 'okhttp/3.2.0'
        }
        result = requests.get(url, headers=headers)
        globals()["fileKey"] = result.json()['data']['fileKey']
        globals()["filetoken"] = result.json()['data']['token']
        print(url)
        print(result.text)
        self.assertEqual(result.json()['code'], 200)

    def test_02(self):
        import requests

        url = "http://upload.qiniu.com/"
        path = os.path.join(os.getcwd(), r"timg.jpg")

        payload = {'key': globals()["fileKey"],
                   'token': globals()['filetoken'],
                   'Content-Type': 'application/octet-stream',
                   'Content-Disposition': 'form-data; name="file"; filename="Screenshot_20200225_212851_com.tencent.mm.jpg"'}
        files = [
            ('file', open(path, 'rb'))
        ]
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'QiniuAndroid/7.3.3 (9; HUAWEI-PCT-AL10; 1582685243370634; dawobP8ofeZsgaUR)'
        }

        result = requests.post(url, headers=headers, data=payload, files=files)
        print(url)
        print(result.text)
        self.assertEqual(result.json()['fileKey'],globals()["fileKey"] )

