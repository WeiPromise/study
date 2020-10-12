#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/12 11:50



class Teacher(object):
    def __init__(self,t_name,t_pass):
        from day13_学生管理系统 import tools
        self.t_name = t_name
        self.t_pass = tools.encrypt_password(t_pass)


class Student(object):
    def __init__(self,s_id,name,age,gender,tel):
        self.s_id = s_id
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel

