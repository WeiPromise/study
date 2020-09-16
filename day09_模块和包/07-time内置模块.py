#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/16 14:55

# 操作时间的
import time

# 获取当前时间的时间戳
print(time.time())

# 按照指定格式输出时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# Wed Sep 16 14:58:39 2020
print(time.asctime())

# Wed Sep 16 14:58:39 2020
print(time.ctime(123212434))

# 休眠

print('hello')
print(time.sleep(10))
print('heheh')