from flask import request
import json, flask

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get','post'])
def login():
    # 获取通过url请求传参的数据
    username = request.values.get('name')
    # 获取url请求传的密码，明文
    password = request.values.get('pwd')
    # 判断用户名、密码都不为空
    if username and password:
        if username == 'xiaoming' and password == '111':
            result = {'code':200, 'message':'登錄成功'}
            #想输出真正的中文
            return json.dumps(result, ensure_ascii=False)
        else:
            result = {'code':-1, 'message':'賬號密碼錯誤'}
            return json.dumps(result, ensure_ascii=False)
    else:
        result = {'code':10001, 'message':'賬號密碼不能爲空'}
        return json.dumps(result, ensure_ascii=False)

if __name__ == '__main__':
    #開啓debug模式
    server.run(debug=True,port=8888, host='127.0.0.1')