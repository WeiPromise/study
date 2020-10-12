#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/9 15:18

def can_paly(clock):
    print('最外层函数被调用了，clock = {}'.format(clock))
    def handle_action(fn):
        def do_action(name,game):
            if clock < 21:
                fn(name,game)
            else:
                print('太晚了，不要玩了')
        return do_action
    return handle_action



@can_paly(22) # 装饰器函数带参数
def play_game(name,game):
    print('{}正在玩儿{}'.format(name,game))


play_game('张三','王者')
