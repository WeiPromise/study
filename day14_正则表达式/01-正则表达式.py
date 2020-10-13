#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/13 16:10

# 用来处理字符串，对字符串进行检索和替换的
# 1、查找；2、替换

import re

content = 'hello\\nworld' # hello\nworld

# 在正则表达式里，如果想要匹配一个 \ ，需要使用 \\\\

# 第一个参数：正则表示大规则
# 第二个参数：匹配的字符串

m = re.search('\\\\',content)
print(m) # <_sre.SRE_Match object; span=(5, 6), match='\\'>


# 字符串前面加r,表示原生字符串
n = re.search(r'\\',content)
print(n) # <_sre.SRE_Match object; span=(5, 6), match='\\'>

# search和match方法执行的结果是一个Match类型的对象


