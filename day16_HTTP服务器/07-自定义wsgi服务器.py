#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/21 16:06


from wsgiref.simple_server import make_server


def demo_app(environ,start_response):
    # environ是一个字典
    # print(environ)
    path = environ.get('PATH_INFO',' Not Found')
    print('path = {}'.format(path))
    start_response("200 OK", [('Content-Type','text/html; charset=utf-8')])
    return ['hello world'.encode('utf8')]



if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户的请求
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    # 打开电脑的浏览器，并在浏览器输入地址，可以不用
    import webbrowser
    webbrowser.open('http://localhost:8000/hello?abc')

    httpd.serve_forever()





