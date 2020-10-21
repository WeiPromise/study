#!/usr/bin/env python3.5
# encoding: utf-8
# Created by leiwei on 2020/10/21 16:06


from wsgiref.simple_server import make_server, demo_app


# 第1个参数：表示环境（电脑的环境，请求路径相关的环境）
# 第2个参数：是一个函数，用来返回响应头
# 这个函数需要一个返回值，返回值是一个列表
# 列表里只有一个元素，是一个二进制，表示返回给浏览器的数据
def demo_app(environ,start_response):
    start_response("200 OK", [('Content-Type','text/plain; charset=utf-8')])
    return ['hello world'.encode('utf8')]



if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户的请求
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    # 打开电脑的浏览器，并在浏览器输入地址，可以不用
    import webbrowser
    webbrowser.open('http://localhost:8000/xyz?abc')

    # 只处理一次请求
    # httpd.handle_request()  # serve one request, then exit
    # 死循环，一直运行
    httpd.serve_forever()

    httpd.server_close()




