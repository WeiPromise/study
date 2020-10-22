#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/22 15:31


import pymysql, hashlib

location = input('请输入城市:')
total_count = input('请输入数量:')

# 进行 md5 加密
# h = hashlib.md5()
# h.update(password.encode('utf8'))
# password = h.hexdigest()

db = pymysql.connect(host='localhost',
                     user='root',
                     password='888520',
                     database='big_data',
                     port=3306,
                     charset='utf8')
cursor = db.cursor()

sql = 'select * from location_count where location=%s and total_count=%s'
print(sql)
# 执行sql语句
cursor.execute(sql, (location, total_count))

cursor.close()
db.commit()
db.close()

result = cursor.fetchone()
if not result:
    print('用户名或者密码错误')
else:
    print('欢迎回来{},您的信息是{}'.format(location, result))