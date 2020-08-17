#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 18:25

# 集合是一个不重复的无序，可以使用{}或者set 来表示

# {} 有两种意思：字典、集合
# 字典：键值对
# 集合：单个值

person = {'name': 'zhangsan', 'age': 18, 'score': 652.5}  # 字典
x = {'hello', 1, 'world'}

# 如果有重复的数据，会自动去重
names = {'lw', 'lw', 'qyt'}
print(names)

# 添加元素

x.add('python')

print(x)

# 清空集合,空集合：set(),{}空字典

# x.clear()

# 删除一个
x.pop()

# 删除一个指定的元素,没有返回值
a = x.remove('hello')

# 将多个集合合并生成一个行的集合
y = {'haah', 123}

z = x.union(y)

# print(x, z, sep='\n')
# 将A 拼接到B里

x.update(y)

print(x, z, sep='\n')
