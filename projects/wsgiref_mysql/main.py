from wsgiref.simple_server import make_server
from urls import urls
from views import *



def run(env,response):
    """

    :param env: 请求相关的所有数据
    :param response: 相应相关的所有数据
    :return: 返回给浏览器的数据
    """
    # print(env)  # 大字典  wsgiref模块处理好了http格式的数据 封装成了字典
    # 从env中取
    response('200 OK',[])  # 响应首行 响应头
    current_path = env.get('PATH_INFO')
    # if current_path == '/index':
    #     return [b'index']
    # elif current_path == '/login':
    #     return [b'login']
    # return [b'404 error']
    # 定义一个变量 存储匹配到的函数名
    func = None # 视图函数
    for url in urls:  # url (),()
        if current_path == url[0]:  # 0表示取url (),()的第一个元素 0为索引
            # 将url对应的函数名赋值给func
            func= url[1]
            break  #结束当前循环 匹配到一个以后like结束for循环
    #判断func是否有值 是否匹配到
    if func:
        res = func(env)
    else:
        res = error(env)
    return [res.encode('utf-8')]  # 统一编码更加合理 不需要在视图函数每次编码

    # return [b'hello wsgiref']

if __name__ == '__main__':
    server = make_server('127.0.0.1',8080,run)
    """
    会实时监听127.0.0.1:8080地址 只要有客户端来了
    都会交给run函数处理(触发run函数的运行)
    
    flask启动源码
        make_server('127.0.0.1',8080,obj)
        __call__
    """
    server.serve_forever()  # 启动服务端



