#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 16:29

person = {'name': 'zhangsan', 'age': 18, 'score': 652.5}

# =======================查==========================
print(person.get('name'))
# key 不存在，返回None
print(person.get('name11'))
# key 不存在，返回指定的默认值
print(person.get('name11', 'heeh'))

print(person['age'])
# key 不存在，报错
# print(person['age11'])

# =======================增加，修改==========================
# 如果key 不存在，添加，如果存在，更新
person['sex'] = '男'
person['age'] = 27

# =======================删除==========================
# 删除，返回删除的元素的值
a = person.pop('sex')

# 删除一个元素，结果返回这个元素组成的键值对（删除那个不确定)
b = person.popitem()

print(person, a, b, sep='\n')


