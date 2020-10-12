#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/12 11:20

base_dir = './files/'

def read_file(file_name):
    try:
        with open(base_dir+file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError as e:
        print(e)


def write_json(file_name,data):
    with open(base_dir+file_name,'w',encoding='utf-8') as file:
        import json
        json.dump(data,file)


def read_json(file_name,default_data={}):
    try:
        with open(base_dir+file_name, 'r', encoding='utf-8') as file:
            import json
            return json.load(file)
    except FileNotFoundError:
        return default_data