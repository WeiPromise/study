#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/12 11:57


import hashlib


def encrypt_password(password, x='ascachasb'):
    h = hashlib.sha256()
    h.update(password.encode('utf-8'))
    h.update(x.encode('utf-8'))
    return h.hexdigest()
