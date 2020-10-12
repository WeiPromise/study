#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/10 15:15

def add_user():
    print('添加用户')


def del_user():
    print('删除用户')


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
        print('''----------------------\n名片管理系统 V1.0\n1：添加名片\n2：删除名片\n3：修改名片\n4：查询名片\n5：显示所有名片\n6：退出系统\n-----------------------''')
        
        operator = input('请输入要进行的操作(数字)：')
        
        if operator == '1': # 名片添加
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