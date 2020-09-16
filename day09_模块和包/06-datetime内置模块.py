#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/16 14:46

# 用来显示日期时间
import datetime as dt

# 获取当前时间日期
print(dt.datetime.now())

# 创建一个日期
print(dt.date(2020, 2, 28))

# 创建一个时间
print(dt.time(18,23,45))

# 计算三天以后的日期时间
print(dt.datetime.now()+dt.timedelta(-3))
