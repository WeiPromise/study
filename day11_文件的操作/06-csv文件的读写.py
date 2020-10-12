#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/7 17:04
import csv

# 写
# file = open('demo.csv','w',encoding='utf-8',newline='')
# writer = csv.writer(file)

# writer.writerow(['name','age','sex','city'])
# writer.writerow(['zhangsan',12,'男','北京'])
# writer.writerow(['李四',12,'男','武汉'])
# writer.writerows([
#     ['name','age','sex','city'],
#     ['zhangsan',12,'男','北京'],
#     ['李四',12,'男','武汉']
# ])
# file.close()

# 读
file = open('info.csv','r',encoding='utf-8')
reader = csv.reader(file)

for line in reader:
    print(line)

file.close()