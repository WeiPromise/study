#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/21 16:06


from wsgiref.simple_server import make_server


def demo_app(environ,start_response):
    # environ是一个字典
    # print(environ)
    path = environ.get('PATH_INFO',' Not Found')

    param = environ.get('QUERY_STRING','')

    print(param)

    status_code = '200 OK'

    if path == '/login':
        response_body = '欢迎来到登录页'
    elif path == '/register':
        response_body = '欢迎来到注册页'
    elif path == '/':
        response_body = '欢迎来到首页'
    else:
        response_body = '你要查找的页面不存在'
        status_code = '404 Page Not Found'

    print('path = {}'.format(path))
    start_response(status_code, [('Content-Type','text/html; charset=utf-8')])
    return [response_body.encode('utf8')]



if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户的请求
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    # 打开电脑的浏览器，并在浏览器输入地址，可以不用

    httpd.serve_forever()





