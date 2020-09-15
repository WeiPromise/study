#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/15 17:38

# 在python里一个py文件，就可以理解为一个模块
# 不是所有的py文件都能作为一个模块来导入
# 如果想要让一个py文件能被导入，模块名称必须要遵守命名规则
# python为了方便我们开发，提供了很多内置模块

import time # 使用import 模块名直接导入一个模块

# 导入模块后，就可以使用这个模块里的方法和变量
print(time.time())

from random import randint # from 模块名 import 函数名，导入一个模块里的方法或者变量

print(randint(0,10)) # 生成0-10的随机数

from math import * # from 模块名 import *，导入一个模块里的"所有"方法和变量

print(pow(2,4))


import datetime as dt # 导入一个模块并给他起别名

print(dt.MAXYEAR)


from copy import deepcopy as dp #  from 模块名 import 函数名 as 别名，导入一个模块里的方法或者变量，并起别名

dp(['hello','good',11])

