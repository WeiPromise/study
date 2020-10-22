#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/22 21:20

import redis

client = redis.Redis(host='172.21.0.16',port=6379)

client.set('username','admin')

client.hset('student','name','hao')

print(client.keys('*'))

print(client.get('username'))

print(client.hgetall('student'))
