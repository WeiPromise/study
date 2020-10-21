#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/21 18:41

# requests 模块是第三方的模块，可以用来发送网络连接
# pip install requests

import requests

response = requests.get('http://127.0.0.1:8000')

# print(response) # 结果是一个Response对象

# content 指的是返回的结果，是一个二进制可以用来传递图片
# print(response.content.decode('utf8'))

# text 获取的就是一个文本
print(response.text)

print(response.status_code)

# 如果返回结果是一个json字符串，json方法可以解析
response1 = requests.get('http://127.0.0.1:8000/test')
print(response1.json())
print(type(response1.text))  # <class 'str'>
print(type(response1.json()))  # <class 'dict'>
