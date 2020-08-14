#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 14:43

import chardet

# ASCII --> Latinl --> Unicode编码
# 字符 --> 数字编码存在一个对应关系
# chr() / ord() 能查看数字和字符的对应关系
# ord：获取字符对应的编码；chr：根据编码获取对应的字符

print(ord('a'))  # 97
print(chr(65))  # A

# chardet.detect 判断文件编码格式
data = open(u"04-内容分隔.py", "rb").read()
b = chardet.detect(data)
print(b.get("encoding"))

# 编码encode
print('你'.encode('gbk'))
print('hello'.encode('utf-8'))
# 解码decode
print('你好'.encode('utf-8').decode('gbk'))
