#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/12 11:01


from day13_学生管理系统 import file_manager
from day13_学生管理系统 import model


def login():
    data = file_manager.read_json('data.json', {})
    teacher_name = input('请输入账号(3-6位)：')

    if teacher_name not in data:
        print('用户名不存在')
        return
    teacher_pass = input('请输入密码(6-12位)：')

    from day13_学生管理系统 import tools

    if data[teacher_name] == tools.encrypt_password(teacher_pass):
        print('登录成功，跳转至学生管理页面')
        from day13_学生管理系统 import student_manager
        student_manager.teacher_name = teacher_name
        student_manager.show_manager()
    else:
        print('密码错误，请重新登录')





def register():

    data = file_manager.read_json('data.json',{})

    while True:
        teacher_name = input('请输入账号(3-6位)：')
        if not 3 <= len(teacher_name) <= 6:
            print('账号不符合要求，请重新输入')

        elif teacher_name in data:
            print('账号已存在，请重新输入')
        else:
            break

    while True:
        teacher_pass = input('请输入密码(6-12位)：')
        if not 6 <= len(teacher_pass) <= 12:
            print('密码不符合要求，请重新输入')
        else:
            break

    t = model.Teacher(teacher_name,teacher_pass)
    data[t.t_name] = t.t_pass
    file_manager.write_json('data.json',data)


def start():
    content = file_manager.read_file('welcome.txt')

    while True:
        operator = input(content + '\n请选择(1-3):')

        if operator == '1':
            login()
        elif operator == '2':
            register()
        elif operator == '3':
            print('退出')
            exit(0)
        else:
            print('输入错误')


if __name__ == '__main__':
    start()
