#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 10:21

# 进制转换：将int类型以不同的进制变现出来
# 类型转换：将一个类型的数据转换为其他类型的数据
# int=>str str=>int ...

age = input('请输入您的年龄：')
# 用户输入的内容保存的结果都是字符串
# 如果str和数字做运算。直接报错，这个时候需要做类型转换
# print(age+1)

print(type(age))
# 使用int 内置类做类型转换
new_age = int(age)
print(type(new_age))
print(new_age+1)



