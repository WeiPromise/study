#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/10 15:15

user_list = [
    {'name': 'zhangsan', 'qq': '2342', 'tel': '112432'},
    {'name': 'lisi', 'qq': '2113e21', 'tel': 'qwe'},
    {'name': 'wangwu', 'qq': '2342', 'tel': '1232431'}
]


def add_user():
    # 用户输入信息
    name = input('请输入用户姓名：')
    # 用户名检查
    for u in user_list:
        if u['name'] == name:
            print('用户名已被占用,name = {}'.format(name))
            return
    tel = input('请输入用户手机号：')
    qq = input('请输入用户QQ：')
    # 信息拼接成字典
    user = {'name': name, 'tel': tel, 'qq': qq}
    # 把创建好的用户，添加到列表
    user_list.append(user)
    print(user_list)


def del_user():
    # 接受用户输入
    number = input('请输入要删除的序号：')
    # 判断输入的数字是否合法
    if check_number(number):
        # 列表里删除用户
        # remove : 删除指定元素
        # pop ：删除指定位置的元素，默认最后一个
        answer = input('确认删除？(yes/no)：')
        if answer.lower() =='yes':
            print('删除用户')
            user_list.pop(int(number)-1)

    print(user_list)


def check_number(number):
    if number.isdigit():
        number = int(number)
        return 0 < number <= len(user_list)
    return False


def modify_user():
    print('修改用户')


def search_user():
    print('查找用户')


def show_all():
    print('显示用户列表')


def exit_system():
    code = input('确认退出？（yes or no）: ')
    return code.lower() == 'yes'


def start():
    while True:
        print(
            '''----------------------\n名片管理系统 V1.0\n1：添加名片\n2：删除名片\n3：修改名片\n4：查询名片\n5：显示所有名片\n6：退出系统\n-----------------------''')

        operator = input('请输入要进行的操作(数字)：')

        if operator == '1':  # 名片添加
            add_user()
        elif operator == '2':
            del_user()
        elif operator == '3':
            modify_user()
        elif operator == '4':
            search_user()
        elif operator == '5':
            show_all()
        elif operator == '6':
            if exit_system():
                print('感谢使用，拜拜')
                break
            else:
                print('请继续使用')

        else:
            print('您输入的选项不合法，请重新输入：')


if __name__ == '__main__':
    start()
