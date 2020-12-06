#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'FangJiong'

import os,sys,json, requests, ddt
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from DemoAPI.lib.readexcel import ReadExcel
testDatad = ReadExcel().read_data()


@ddt.ddt()
class SendRequests():
    """发送请求数据"""
    @ddt.data(*testDatad)
    def sendRequests(self,apiData):
        print(apiData)
        try:
            #从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            print(method)
            url = apiData["url"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            # if apiData["headers"] == "":
            #     h = None
            # else:
            #     # eval()函数用来执行一个字符串表达式，并返回表达式的值。
            #     h = eval(apiData["headers"])
            # if apiData["body"] == "":
            #     body_data = None
            # else:
            #     body_data = eval(apiData["body"])
            # type = apiData["type"]
            # v = False
            # if type == "data":
            #     body = body_data
            # elif type == "json":
            #     # json.dumps()
            #     # 用于将字典形式的数据转化为字符串，
            #     # json.loads()
            #     # 用于将字符串形式的数据转化为字典
            #
            #     body = json.dumps(body_data)
            # else:
            #     body = body_data

            #发送请求
            # re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=v)
            s = requests.sessions()
            re = s.request(method=method,url=url,params=par)
            return re
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print(SendRequests().sendRequests(testDatad))
