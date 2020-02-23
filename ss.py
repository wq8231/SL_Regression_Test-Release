import requests
import time
# url = 'http://yun.slothtek.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
# result = requests.get(url=url, headers=headers)
# print(result)
# def test_f():  # pad登录老师账号
#     url = 'http://bip.slothtek.com/api/v1/auth/login'
#     headers = {
#         'User-Agent': 'okhttp/3.6.0'}
#     data = {'name': '19222', 'password': '96e79218965eb72c92a549dd5a330112'}
#     result = requests.session().post(url=url, headers=headers, data=data)
#     print(result.json())
#     print(result.json()['data']['name'])
#     print(result.json()['code'])
# test_f()
# def test_g(self):  # pad登录学生账号
#     url = 'http://bip.slothtek.com/api/v1/auth/login'
#     headers = {
#         'User-Agent': 'okhttp/3.6.0'}
#     data = {'name': self.stuname, 'password': self.stumd5psw, 'platform': 'WEB'}
#     result = requests.session().post(url=url, headers=headers, data=data)
#     self.assertEqual(result.text,
#                      '{"code":200,"msg":"登录成功","data":null,"params":null,"sysSign":null,"succeed":true}')


def getpadtoken( name, psw):  # 获取pad端token
    url = 'http://bip.slothtek.com/api/v1/auth/login'
    headers = {
        'User-Agent': 'okhttp/3.6.0'}
    data = {'name': name, 'password': psw}
    result = requests.session().post(url=url, headers=headers, data=data)
    token = result.json()['data']['token']
    print(token)

getpadtoken('19222','96e79218965eb72c92a549dd5a330112')
