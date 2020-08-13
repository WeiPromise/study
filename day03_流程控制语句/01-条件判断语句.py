#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 16:32

# 支持 if / if else /if elif elif else
# 不支持 switch case

# 注意：
#   1、区间判断，可以不用and 连接，可以使用10>a>2;
#   2、隐式类型转换：if 3：
#   3、三元表达式：x=num1 if num1>num2 else num2

# if 条件判断
# age = input('请输入您的年龄：')

# if int(age) < 18:
#     print("小朋友")
#
# if int(age) < 18:
#     print('小朋友')
# else:
#     print('大朋友')

score = int(input('请输入学生成绩：'))

if score < 60:
    print('不及格')
elif 60 <= score < 80:
    print('良好')
elif 100 >= score >= 80:
    print('优秀')
else:
    print('大煞笔')
