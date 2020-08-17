#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 17:03

# 练习 1
chars = ['a', 'b', 'b', 'c', 'd', 'd', 'a', 'd', 'e', 'r', 'r', 'g', 'g', 'a']

char_count = {}

for char in chars:
    # if char in char_count:
    #     char_count[char] += 1
    # else:
    #     char_count[char] = 1
    if char not in char_count:
        char_count[char] = chars.count(char)

print(char_count)

vs = char_count.values()

max_count = max(vs)

for k, v in char_count.items():
    if v == max_count:
        print(k, v, sep='=')

# 练习 2

persons = [
    {'name': 'zhansan', 'age': 18},
    {'name': 'lisi', 'age': 17},
    {'name': 'wangwu', 'age': 28},
    {'name': 'zhaoliu', 'age': 38},
    {'name': 'tianqi', 'age': 23}
]

name = input('请输入您的姓名：')

for person in persons:
    if person['name'] == name:
        print('存在')
        break
else:
    new_person = {'name': name}
    age = input('请输入您的年龄：')

    while not age.isdigit():
        age = input('请重新输入您的年龄(数字)：')

    new_person['age'] = int(age)

    persons.append(new_person)

    print('用户添加成功')


