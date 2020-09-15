#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/9/15 17:10

# def play_game(name,game,clock):
#     if clock > 22:
#         print('太晚了，不能玩了')
#         return
#     print('{}正在玩{}'.format(name,game))

def can_play(fn):
    def inner(name,game,*args,**kwargs):
        if args[0] > 22:
            print('太晚了，不能玩了')
        else:
            fn(name,game)
    return inner


@can_play
def play_game(name,game):
    print('{}正在玩{}'.format(name,game))

play_game('zhangsan','wangzhe',21)
play_game('lishi','judi',18)


