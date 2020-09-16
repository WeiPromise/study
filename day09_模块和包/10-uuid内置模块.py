#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/16 16:11

# 用来生成全局唯一的模块

import uuid

# 5563b462-f7f4-11ea-8d5d-e470b8b48599，基于mac地址，时间戳，随机数来生成的，全球唯一
print(uuid.uuid1())


# 生成固定的uuid,根据传入的字符串根据指定算法算出来的
print(uuid.uuid3(uuid.NAMESPACE_DNS,'zhangsan'))
print(uuid.uuid5(uuid.NAMESPACE_DNS,'zhangsan'))

# 使用的最多的
print(uuid.uuid4())