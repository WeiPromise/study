#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/16 15:22

# 用来进行数据加密的

# hashlib主要有MD5和sha加密

import hashlib
import hmac


# 生成一个MD5对象
md5 = hashlib.md5()
# 加密
md5.update('12356890'.encode('utf8'))
# 获取密文
print(md5.hexdigest())

# 现在sha加密更安全
h1 = hashlib.sha1('123456'.encode())
print(h1.hexdigest())


# hmac加密可以字段密钥
h = hmac.new('leiwei'.encode(),'haah'.encode())
print(h.hexdigest())

