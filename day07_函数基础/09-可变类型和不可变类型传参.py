#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/19 10:56

# 函数传参：传的地址值
#   如果参数是不可变类型（Number（数字）、String（字符串）、Tuple（元组）：则在函数中修改参数值不影响实参的值，只是给形参一个新的地址值
#   如果参数是可变类型(dict,list,set)：则在函数中修改参数值影响实参的值

def my_test(a):
    print('修改前地址,id = {}'.format(id(a)))
    a = 100
    print('修改后地址,id = {}'.format(id(a)))

def demo(nums):
    print('修改前地址,nums = {}'.format(id(nums)))
    nums[0] = 10
    print('修改后地址,nums = {}'.format(id(nums)))

x = 1
my_test(x)
print(x) # x =1

y = [2, 3, 4, 5]
demo(y)
print(y) # y = [10, 3, 4, 5]
