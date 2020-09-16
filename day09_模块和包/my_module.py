#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/16 17:44

__all__ = ['a'] # 通过 from a import * 只能导入括号里的变量和方法

a = 100

_age = 23 #私有变量或方法，建议值在本模块使用


def sum(b):
    return a + b



print('hehehheeh')


# __name__：当直接运行这个py文件时，值是__main__
# 如果这个py作为一个模块导入的时候，值是文件名
if __name__ == '__main__':
    print('我是main方法')

# 只能内部使用
del _age




