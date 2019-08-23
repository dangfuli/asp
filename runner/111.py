# coding=utf-8
# import smtplib
# from email.header import Header
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# mail = MIMEMultipart()
#
# mail['From'] = Header('623037035@qq.com','utf-8')
# mail['To'] = Header('623037035@qq.com','utf-8')
# mail['Subject']=Header('title','utf-8')
#
# mail.attach(MIMEText('zhengwen','plain','utf-8'))
#
# send = smtplib.SMTP_SSL('smtp.qq.com',465)
# send.login('623037035@qq.com','xspwqntmjvqwbcbd')
# send.sendmail('623037035@qq.com','623037035@qq.com',mail.as_string())
#

# import re
# s = '''
# 不计免赔险(车损) 投保 0.12
# 不计免赔险(三者) 投保 0.00
# 不计免赔险(乘客) 投保 0.00
# 不计免赔险(司机) 投保 0.00
# 商业险保费合计 0.00'''
#
# ## 正则提取 ['不计免赔险(车损) 投保 0.12', '不计免赔险(三者) 投保 0.00', '不计免赔险(乘客) 投保 0.00', '不计免赔险(司机) 投保 0.00', '商业险保费合计 0.00']
# d = re.findall('\n(.*)',s)
#
# ## 处理数据,循环，以此处理
# for i in d:
#     ## 先排除合计，无用的数据
#     ## 重新赋值一下
#     i = i.split(' ')    #['不计免赔险(车损)', '投保', '0.12']
#     if len(i) < 3:
#         print('这个是合计，不做处理')
#     else:
#         if '不计免赔险(车损)' in i[0]:
#             print(f'不计免赔险存在，且价钱为：{i[2]}')
#             print('这里处理数据，想怎么处理怎么处理')
#         if '不计免赔险(三者)' in i[0]:
#             print(f'不计免赔险(三者)，且价钱为：{i[2]}')
#             print('这里处理数据，想怎么处理怎么处理')
#         if '不计免赔险(乘客)' in i[0]:
#             print(f'不计免赔险(乘客)，且价钱为：{i[2]}')
#             print('这里处理数据，想怎么处理怎么处理')
#
#         ## 后面同理，不写了
# from flask import Flask,request
# import json
# app = Flask(__name__)
# @app.route("/test_1.0",methods=["GET"])
# def check():
#     return_dict= {'return_code': '200', 'return_info': '处理成功', 'result': False}
#     if request.args is None:
#         return_dict['return_code'] = '5004'
#         return_dict['return_info'] = '请求参数为空'
#         return json.dumps(return_dict, ensure_ascii=False)
#         # 获取传入的参数
#     get_data = request.args.to_dict()
#     name = get_data.get('name')
#     age = get_data.get('age')
#     # 对参数进行操作
#     return_dict['result'] = tt(name, age)
#     return json.dumps(return_dict, ensure_ascii=False)
#
# def tt(name, age):
#     result_str = "%s今年%s岁" % (name, age)
#     return result_str
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


# import requests
# import threading
# import time
# url = "http://fb.creativecatapp.com/lucky/api/users/lottery"
#
# headers1 = {
#     'Content-Type': "application/json",
#     'Host': "fb.creativecatapp.com",
#     "authorization":"Bearer a550fde74873b00005028a0759d4703f",
#     "eid":"1",
#     "version":"1.0",
#     "clientDate":"1563428871",
#     'Postman-Token': "8dd77528-796e-4e4b-bb6e-4ad60591ff1a,0a44f14e-76a4-4b95-a491-f2842734703b"
#     }
# data = "{\n\t\"ticket_id\":79,\n\t\"ticket_num\":\"38,12,36,9,7,43\"\n}"
# def t():
#     print(time.time())
#     r = requests.post(url, headers=headers1,data=data)
#     print(r.json())
#
# threads = []
# for i in range(20):
#     thread = threading.Thread(target=t)
#     threads.append(thread)
#     # 创建2个线程
# for n in threads:
#     n.start()
# for k in threads:
#     k.join()

## flask
# from flask import Flask,request
# import json
# app = Flask(__name__)
# @app.route('/test',methods=['GET'])
# def check():
#     return_dict = {'code':0,'msg':"success","data":None}
#     print(request.args)
#     if request.args is None:
#         return_dict['code'] = 5004
#         return_dict['msg'] = '请求参数为空'
#         return json.dumps(return_dict)
#     get_data = request.args.to_dict()
#     name = get_data.get('name')
#     age = get_data.get('age')
#     return_dict['data'] = tt(name,age)
#     return json.dumps(return_dict,ensure_ascii=False)
#
# def tt(name,age):
#     return '%s今年%s岁'%(name,age)
#
# if __name__ == '__main__':
#     app.run(debug=True)

# # 冒泡排序
# # 先定一个一个需要排序的列表
# l = [7,2,3,1,4,5,6,9,8]
# # 统计一下长度
# n = len(l)
# ## 先遍历所有元素
# for i in range(len(l)):
#     ## 最后还剩多少个元素需要对比排序，因为本身自己不需要排序，所以-1，之前已经拍过多少个数字了，还剩下多少就需要把i也减去
#     for j in range(n-i-1):
#         ## 对比，如果当前的数字比后面的数字大，则对换
#         if l[j] > l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)

# 二分算法
# def erfen(list1,num):
#     headIndex = 0       ## 首索引
#     endIndex = len(list1)-1         ## 结尾索引
#     count = 0          ## 计数用
#     while headIndex <= endIndex:       ## 循环查找
#           midIndex = (headIndex+endIndex)//2    ## 每次重新赋值中间索引
#           count +=1
#           #if len(list1)%2 == 0:
#           if num == list1[midIndex]:         ## 判断是否找到
#               print(f'查找 {num} 共计执行 {count} 次')
#               return num
#           if num > list1[midIndex]:          ## 如果目标数字比中间索引的数值大，首索引则赋值为中间索引加一，加一是为了处理最后一个位置的数值
#               headIndex = midIndex +1
#           if num < list1[midIndex]:          ## 如果目标数字比中间索引的数值小，末尾索引则赋值为中间索引减一，减一是为了处理开头位置的数值
#               endIndex = midIndex  -1
#     else:
#         print('没有找到这个数字')
#
# ## 这里测试一下
# l = [1,2,3,4,5,6,7,8,9,10]
# for i in range(1,11):
#     erfen(l,i)

# import unittest
# class Test(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.g = globals()
#
#     def test_a(self):
#         ## 假设这个是这个接口的返回值
#         return_valueA = {'code':1}
#         print(f'这个接口返回为{return_valueA}')
#
#         ## 这里使用globals()
#         ## A接口的返回值
#         self.g['a'] = return_valueA
#     def test_b(self):
#         ## 假设这个接口要用这个data
#         ## B接口需要用到A接口的返回值
#         print(f'这里是需要用到的test_b的返回值的函数:%s'%self.g['a'])
#         ## 假设他是b接口的返回值
#         return_valueB = {'messge':"ok"}
#         ## 直接用globals()赋值就ok了
#         self.g['b'] = return_valueB
#
#     def test_c(self):
#         ## 假设这个是C接口，需要用到B接口的返回值
#
#         print(f'这里是需要用到的test_b的返回值的函数:%s'%self.g['b'])
#
# if __name__ == '__main__':
#     unittest.main()

# ## 装饰器
# #类装饰器
# class Decorator:
#     def __init__(self,func):
#         ## 赋值函数
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         ## 一call顶万物
#         print('假设这里开始执行其他的代码')
#         self.other_func()
#         self.func(*args, **kwargs)
#         self.other_func2()
#         print('假设这里在执行完这个函数后，执行了其他的代码')
#         return
#     def other_func(self):
#         print('这是一个打酱油的函数')
#
#     @staticmethod
#     def other_func2():
#         print('这是一个吃瓜的函数')
#
# ## 测试一下
# @Decorator
# def test_a(a,b):
#     print(f'print a :{a}')
#     print(f'print b :{b}')
#     c = a+b
#     print(c)
#     return c
#
# test_a(1,2)
# #函数装饰器
# def zsq_func(func):
#     print('这是一个函数装饰器')
#     def wrapper(*args,**kwargs):
#         try:
#             print('开始前，执行的代码')
#             func(*args,**kwargs)
#             print('结束了，执行的代码')
#             return
#         except:
#             print('出错了的处理')
#
#     print('执行装饰器函数前可以执行其他代码')
#     return wrapper
#
# ## 测试一下
# @zsq_func
# def func(a,b):
#     print(f'print a :{a}')
#     print(f'print b :{b}')
#     c = a+b
#     print(c)
#     return c
# func(1,2)

# ## mock使用
# from unittest import mock
# def need_mock():
#     a = 1
#     b = 2
#     ## 假设他的实际返回值为a+b
#     return a+b
#
# def use_mock_func():
#     ## 使用mock的函数
#     print(need_mock())
#
# ## 这里mock对应函数
# need_mock = mock.Mock(return_value='123')
#
# ## 调用测试一下
# use_mock_func()

## 定时器
# from apscheduler.schedulers.background import BackgroundScheduler
# import time
# # 目标函数，需要被定时执行的函数
# def need_sheduler():
#     print('123')
#
# ## 实例
# aps = BackgroundScheduler()
#
# ## 第一个参数为目标函数，第二个为内置的一个名称，seconds为执行的间隔
# aps.add_job(need_sheduler,'interval',seconds=3)
#
# ## 雷同与线程，启动线程任务
# aps.start()
#
# ## 测试一下
# while 1:
#     try:
#         ## 等2s
#         print('按control+c停止')
#         print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#         time.sleep(2)
#     except:
#         ## 结束进程
#         aps.shutdown()
#         print('end')


# import multiprocessing
# import threading
# import time
# import requests
# import json
#
# ## 线程执行的函数
# def func():
#     url = 'https://api1.wisroomtest.100tal.com/nzoth-org/v5/teacher/preLogin'
#     data = {
#         "loginId": "18231012910",
#         "password": "123456"
#     }
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Linux; Android 9; Redmi K20 Pro Build/PKQ1.181121.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand0 NetType/WIFI Language/zh_CN",
#         "charset":"utf-8",
#         "content-type":"application/json",
#         "referer":"https://servicewechat.com/wx49744c468ae0af58/0/page-frame.html",
#         "Accept-Encoding":"gzip"
#     }
#     print('start tread:',threading.current_thread())
#     print(time.time(), '\n')
#     r = requests.post(url=url,data=json.dumps(data),headers=headers)
#     print(r.json())
#
# ## 线程执行的函数
# def bar():
#
#     ## 线程池
#     threads = []
#     ##这里添加x个线程
#     for _ in range(500):
#         threads.append(threading.Thread(target=func))
#     ## 启动线程
#     for thread in threads:
#         thread.start()
#     for t in threads:
#         t.join()
#
# ## 进程池
# multiprocess = []
#
# ## 有几核心cpu启动几个
# for i in range(2):
#     multiprocess.append(multiprocessing.Process(target=bar))
# for j in multiprocess:
#     j.start()
# ## 启动进程
# for p in multiprocess:
#     p.join()


# ## 多进程
# import multiprocessing
# ## 进程需要执行的函数
# def func():
#     print('process',multiprocessing.current_process())
#
# ## 有几个cpu核心添加几个进程
# for _ in range(2):
#     multiprocessing.Process(target=func).start()

# ## 多线程
# import threading
# import multiprocessing
# ## 线程执行函数
# def func():
#     print('thread:',threading.current_thread())
#
# ## 线程池
# threads = []
#
# ## 添加线程
# for _ in range(5):
#     threads.append(threading.Thread(target=func))
#
# ## 启动线程
# for thread in threads:
#     thread.start()
#     thread.join()

import inspect
## 函数获取函数名称
def a():
    print('当前函数名称:',inspect.stack()[1][3])

def use_a():
    ## 使用a函数
    a()

## 调用使用a函数
print('------函数调用------')
use_a()

##类获取函数名称
class TestSys:
    def testa(self):
        print('当前函数名称:', inspect.stack()[1][3])

    def testb(self):
        self.testa()
## 一个类时
print('------单个类时内部调用------')
t = TestSys()
t.testb()


class Testsys:
    def testc(self):
        TestSys().testa()

## 两个类时，第二个类调用第一个类
print('------多个类时内部调用------')
t = Testsys()
t.testc()
