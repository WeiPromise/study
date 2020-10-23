#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/23 13:25

from pymongo import MongoClient

client = MongoClient(host='172.21.0.16',port=27017)

db = client.school

for sudent in db.students.find():
    print(sudent)
