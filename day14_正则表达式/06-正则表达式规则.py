#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/13 21:26

import re

# 1、数字和字母都表示它本身

#字母x表示它本身
re.search(r'x','hello xyz')
re.search(r'5','helloasd234255 xyz')


# 2、很多字母前面添加\会有特殊含义

print(re.search(r'd','good')) # 字母d是普通的字符 <_sre.SRE_Match object; span=(3, 4), match='d'>
print(re.search(r'\d','good')) # \d 有特殊含义,不在表示字母d None
print(re.search(r'\d','ajhsdhja2sk')) # \d :表示匹配数字 <_sre.SRE_Match object; span=(8, 9), match='2'>

# 3、绝大多数标点符号都有特殊含义（重点）

#  print(re.search(r'+','+ajda ')) # 不能直接使用，+ 有特殊含义

print(re.search(r'\+','+ajda ')) # 加 \转义 <_sre.SRE_Match object; span=(0, 1), match='+'>
