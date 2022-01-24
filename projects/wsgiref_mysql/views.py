def error(env):
    return '404 error'

def index(env):
    return 'index'

def login(env):
    return 'login'

def xxx(env):
    with open(r'templates/my_xxx.html','r',encoding='utf-8') as f:
        return f.read()

import  datetime
def get_time(env):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %X')
    # 如何将后端获取到的数据"传递"给html文件
    with open(r'templates/my_time.html','r',encoding='utf-8') as f:
        data = f.read()
        # data就是一堆字符串
    data = data.replace('nico',current_time)
    return data

from jinja2 import Template
def get_dict(env):
    user_dic = {'username':'jason','age':18,'hobby':'read'}  # 字典 模板语法之jinja2模块 pip3 install jinja2
    with open(r'templates/get_dict.html','r',encoding='utf-8') as f:
        data = f.read()
    tmp = Template(data)
    res = tmp.render(user=user_dic)
    #给get_dict.html传递了一个值 页面上通过变量名user就能够拿到user_dict
    return res



import pymysql
def get_user(env):
    # 去数据库中获取数据 传递给html页面 借助于模板语法 发送给浏览器
    conn = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        password = 'SLNico295666',
        db='hello',
        charset = 'utf8',
        autocommit = True  # 自动提交
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'select * from helloworld'
    affect_rows = cursor.execute(sql)
    data_list = cursor.fetchall()  # [{},{},{}]
    # 将获取到的数据传递给html文件
    with open(r'templates/get_data.html','r',encoding='utf-8') as f:
        data = f.read()
    tmp = Template(data)
    res = tmp.render(user_list=data_list)
    #给get_data.html传递了一个值 页面上通过变量名user就能够拿到user_dict
    return res

    #print(data_list)
if __name__ == '__main__':
    get_user(111)

