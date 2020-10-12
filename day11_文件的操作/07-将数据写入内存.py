#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/7 17:21

# 将数据写入到内存涉及到StringIO和BytesIO两个类
# 使用场景：先把信息存在内存里，等需要的时候在拿出来用
from io import StringIO,BytesIO

s_io = StringIO()
s_io.write('hello')
s_io.write(' good')
print(s_io.getvalue(),file=open('study.log','w'))


b_io = BytesIO()
b_io.write('你好'.encode('utf-8'))
print(b_io.getvalue().decode('utf-8'))