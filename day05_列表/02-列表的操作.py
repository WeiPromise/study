#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/14 16:04

# 列表是有序的，可变的，可进行CRUD操作
names = ['zansan', 'lisi', 'wangwu', 'zhaoliu', 'ake', 'yingzhneg', 'zhaoliu', 'hangxing', 'huangzhong']

# ========================增加=======================================
# C 添加
# append 列表末尾添加元素
# insert 列表指定位置之前插入数据
names.insert(names.index('ake'), 'lidema')

# extend 末尾追加可迭代对象 a.extend(b),a变b不变
new_names = ['derenjie', 'mkbl']
names.extend(new_names)

print(names)

# ========================删除=======================================
# pop()：删除指定位置元素，默认最后一位，返回被删除值
# remove()：删除指定元素,没返回值
# clear()：清空
# del() : 建议不要用，删除对象

# print(names.pop())
# print(names.remove('zhaoliu'))
# names.clear()
# print(names)

# ========================查询=======================================
# 查询某个元素第一次出现位置
print(names.index('zhaoliu'))
# 查询某个元素出现次数
print(names.count('zhaoliu'))

# in 运算符
if 'zhaoliu' in names:
    print(names.index('zhaoliu'))

# ========================修改=======================================
names[3] = 'luguannan'
print(names)

# ========================反转=======================================
names[3] = 'luguannan'
names.reverse()
print(names)
