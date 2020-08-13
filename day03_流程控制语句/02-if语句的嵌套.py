#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/8/13 17:26
ticket = input('是否买票了？N/Y：')

if ticket == 'Y':
    print('买票了，可以进站')
    safe = input('安检是否通过？Y/N：')
    if safe == 'Y':
        print('通过')
    else:
        print('不通过')
else:
    print('滚')
