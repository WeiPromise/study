#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/13 18:32
import re

# 在re模块里，可以使用re.方法调用，还可以调用re.compile得到一个对象

content = 'hello wrold good morining l love you baby good'

m = re.search(r'good',content) # <_sre.SRE_Match object; span=(12, 16), match='good'>
pattern = re.compile(r'good')
n = pattern.search(content)
print(n) # <_sre.SRE_Match object; span=(12, 16), match='good'>


