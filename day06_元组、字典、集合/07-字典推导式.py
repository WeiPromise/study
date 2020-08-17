#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/17 17:33


dict1 = {'a': 100, 'b': 200, 'c': 300}

dict2 = {}

# for k, v in dict1.items():
#     dict2[v] = k


# 字典推导式

dict1 = {v: k for k, v in dict1.items()}
print(dict1)


