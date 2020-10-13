#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/12 16:56

from day13_学生管理系统 import file_manager
from day13_学生管理系统 import model

teacher_name = ''


def add_student():
    data = file_manager.read_json(teacher_name + '.json', {})
    students = data.get('all_student', [])

    while True:
        while True:
            s_name = input('请输入学生姓名：')
            for student in students:
                if student['name'] == s_name:
                    print('该学生已存在，请重新输入')
                    break
            else:
                break

        s_age = input('请输入学生年龄：')
        s_gender = input('请输入学生性别：')
        s_tel = input('请输入学生电话：')

        num = data.get('num', 0)
        # zfill(4) ,字符串前面补0
        s_id = 'stu_' + str(num + 1).zfill(4)
        s = model.Student(s_id, s_name, s_age, s_gender, s_tel)
        students.append(s.__dict__)
        data = {'all_student': students, 'num': len(students)}

        file_manager.write_json(teacher_name + '.json', data)

        chioce = input('添加成功！\n1、继续\n2、返回\n请选择：')

        if chioce == '2':
            break


def show_student():
    operator = input('1、查看所有学生\n2、根据姓名查找\n3、根据学号查找\n4.其他：返回\n请选择：')

    data = file_manager.read_json(teacher_name + '.json', {})
    students = data.get('all_student', [])

    key = value = ''

    if operator == '1':
        pass
    elif operator == '2':
        value = input('请输入学生姓名：')
        key = 'name'
    elif operator == '3':
        value = input('请输入学生学号：')
        key = 's_id'
    else:
        return
    # 这里需要转换成list,不然判空有问题，迭代器没有判空这个说法
    students = list(filter(lambda student: student.get(key, '').find(value) >= 0, students))

    if not students:
        print('未找到学生')
        return

    for student in students:
        print('学号：{s_id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**student))


def modify_studxent():
    pass


def del_student():
    data = file_manager.read_json(teacher_name + '.json', {})
    students = data.get('all_student', [])

    if not students:
        print('该老师还没有学生，请先添加')
        return

    operator = input('1、按姓名删\n2、按学号删\n其他：返回\n请选择：')

    key = value = ''

    if operator == '1':
        value = input('请输入学生姓名：')
        key = 'name'
    elif operator == '2':
        value = input('请输入学生学号：')
        key = 's_id'
    else:
        return

    del_students = list(filter(lambda student: student.get(key, '') == value, students))

    if not del_students:
        print('未找到符合条件的学生')
        return

    for i, student in enumerate(del_students):
        print('序号：{},学号：{s_id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(i, **student))

    num = input('请输入需要删除学生的序号(0~{})：'.format(len(del_students) - 1))

    if num.isdigit() and 0 <= int(num) <= len(del_students) - 1:
        students.remove(del_students[int(num)])
    else:
        print('输入序号不合法')
        return

    data['num'] = len(students)

    file_manager.write_json(teacher_name + '.json', data)


def show_manager():
    content = file_manager.read_file('student_page.txt').format(teacher_name)
    while True:
        operator = input(content + '\n请选择(1-5):')

        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            modify_studxent()
        elif operator == '4':
            del_student()
        elif operator == '5':
            print('返回')
            break
        else:
            print('输入错误')
