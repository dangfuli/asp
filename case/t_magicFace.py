# coding=utf-8
import requests
import unittest,os,time,random
# from lib.getConfig import getConfig
from doc.constant import *

# headers = getConfig(os.path.join(os.path.dirname(os.path.dirname(__file__)),'config/commonHeader.json'))
##
headers = {}
headers['version'] = '1.7.0'
headers['platform'] = '01'

class GetSettings(unittest.TestCase):
    ## getSettings根据APP版本，获取对应的配置
    @classmethod
    def setUpClass(cls):
        cls.url = MF_URI + 'getSettings'
        cls.param = {
            "key": "",
            "appVersion": ""
        }
    def test001(self):
        '''安卓获取全部配置

        1、key为空
        2、appVersion为空
        '''
        headers['platform'] = '01'
        ## 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        self.assertIsNotNone(r.json())

    def test002(self):
        '''
        安卓获取配置，version为空。。结果返回为空

        1、key为空
        2、header中version为空
        '''
        ## headers中version置为空
        headers['platform'] = '01'
        headers['version'] = ''
        ## 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        headers['version'] = '1.7.0'
        ## 断言返回为空dict
        self.assertDictEqual({},r.json())
        time.sleep(3)
    def test003(self):
        '''
        安卓获取配置，header中version为其他任意数据，返回为空
        1、key为空
        2、header中version为其他类型数据
        '''
        ## header中version设置为数字
        headers['platform'] = '01'
        headers['version'] = ')_)_()'
        ### 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        headers['version'] = '1.7.0'
        ## 断言返回为空dict
        self.assertDictEqual({}, r.json())

    def test004(self):
        '''
        安卓获取配置，param中key指定subscribe_first
        1、key为subscribe_first
        2、verison为空
        '''
        headers['platform'] = '01'
        ## param设置key为subscribe_first
        self.param['key'] = 'subscribe_first'
        ## 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subscribe_first',r.json())

    def test005(self):
        '''
        安卓获取配置，param中key指定subscribe_frequency
        1、key为subscribe_frequency
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为subscribe_frequency
        self.param['key'] = 'subscribe_frequency'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subscribe_frequency', r.json())

    def test006(self):
        '''
        安卓获取配置，param中key指定subscribe_switch
        1、key为subscribe_switch
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为subscribe_switch
        self.param['key'] = 'subscribe_switch'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subscribe_switch', r.json())

    def test007(self):
        '''
        安卓获取配置，param中key指定mark_n
        1、key为mark_n
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为mark_n
        self.param['key'] = 'mark_n'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('mark_n', r.json())

    def test008(self):
        '''
        安卓获取配置，param中key指定mark_m
        1、key为mark_m
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为mark_m
        self.param['key'] = 'mark_m'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('mark_m', r.json())

    def test009(self):
        '''
        安卓获取配置，param中key指定subscribe_goods
        1、key为subscribe_goods
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为subscribe_goods
        self.param['key'] = 'subscribe_goods'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subscribe_goods', r.json())

    def test010(self):
        '''
        安卓获取配置，param中key指定subscribe_button
        1、key为subscribe_button
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为subscribe_button
        self.param['key'] = 'subscribe_button'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subscribe_button', r.json())

    def test011(self):
        '''
        安卓获取配置，param中key指定subscribe_check
        1、key为subscribe_check
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为subscribe_check
        self.param['key'] = 'subscribe_check'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subscribe_check', r.json())

    def test012(self):
        '''
        安卓获取配置，param中key指定reward_switch
        1、key为reward_switch
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为reward_switch
        self.param['key'] = 'reward_switch'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('reward_switch', r.json())

    def test013(self):
        '''
        安卓获取配置，param中key指定reward_list
        1、key为reward_list
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为reward_list
        self.param['key'] = 'reward_list'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('reward_list', r.json())

    def test014(self):
        '''
        安卓获取配置，param中key指定rate_switch
        1、key为rate_switch
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为rate_switch
        self.param['key'] = 'rate_switch'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('rate_switch', r.json())

    def test015(self):
        '''
        安卓获取配置，param中指定key为不存在的配置名称
        1、key为其他任意不存在的配置
        2、version为空
        '''
        headers['platform'] = '01'
        ## param设置key为任意其他不存在的配置数据
        self.param['key'] = '不存在的配置'
        ## 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        self.param['key'] = ''
        ## 断言返回为空
        self.assertDictEqual({},r.json())

    def test016(self):
        '''ios获取全部配置

        1、key为空
        2、appVersion为空
        '''
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        self.assertIsNotNone(r.json())

    def test017(self):
        '''
        ios获取配置，version为空。。结果返回为空

        1、key为空
        2、header中version为空
        '''
        ## headers中version置为空
        headers['version'] = ''
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        headers['version'] = '1.7.0'
        ## 断言返回为空dict
        self.assertDictEqual({},r.json())

    def test018(self):
        '''
        ios获取配置，header中version为其他任意数据，返回为空
        1、key为空
        2、header中version为其他类型数据
        '''
        ## header中version设置为数字
        headers['version'] = ')_)_()'
        headers['platform'] = '02'
        ### 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        headers['version'] = '1.7.0'
        ## 断言返回为空dict
        self.assertDictEqual({}, r.json())

    def test019(self):
        '''
        ios获取配置，param中key指定subs_goods
        1、key为subs_goods
        2、verison为空
        '''
        ## param设置key为subs_goods
        self.param['key'] = 'subs_goods'
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url,headers=headers,params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subs_goods',r.json())

    def test020(self):
        '''
        ios获取配置，param中key指定subs_ch
        1、key为subs_ch
        2、version为空
        '''
        ## param设置key为subs_ch
        self.param['key'] = 'subs_ch'
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subs_ch', r.json())

    def test021(self):
        '''
        ios获取配置，param中key指定subs_sw
        1、key为subs_sw
        2、version为空
        '''
        ## param设置key为subs_sw
        self.param['key'] = 'subs_sw'
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subs_sw', r.json())

    def test022(self):
        '''
        ios获取配置，param中key指定subs_button
        1、key为subs_button
        2、version为空
        '''
        ## param设置key为subs_button
        self.param['key'] = 'subs_button'
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subs_button', r.json())

    def test023(self):
        '''
        ios获取配置，param中key指定mark_m
        1、key为mark_m
        2、version为空
        '''
        ## param设置key为mark_m
        self.param['key'] = 'mark_m'
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('mark_m', r.json())

    def test024(self):
        '''
        ios获取配置，param中key指定mark_n
        1、key为mark_n
        2、version为空
        '''
        ## param设置key为mark_n
        self.param['key'] = 'mark_n'
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('mark_n', r.json())

    def test025(self):
        '''
        ios获取配置，param中key指定subs_frequency
        1、key为subs_frequency
        2、version为空
        '''
        ## param设置key为subs_frequency
        self.param['key'] = 'subs_frequency'
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subs_frequency', r.json())

    def test026(self):
        '''
        ios获取配置，param中key指定subs_first
        1、key为subs_first
        2、version为空
        '''
        ## param设置key为subs_first
        self.param['key'] = 'subs_first'
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url, headers=headers, params=self.param)
        self.param['key'] = ''
        ## 断言返回这个字段
        self.assertIn('subs_first', r.json())

class GetScore(unittest.TestCase):
    ## getSettings获取运势分数及对应的文案
    @classmethod
    def setUpClass(cls):
        cls.url = MF_URI + 'getScore'

    def test001(self):
        '''
        安卓获取运势
        1、headers中platform为01
        '''
        ## 修改platform为01
        headers['platform'] = '01'
        ## 请求接口
        r = requests.get(self.url,headers=headers)
        ## 断言返回的结果
        self.assertIn('avgScore',r.json())

    def test002(self):
        '''
        ios获取运势
        1、headers中platform为02
        '''
        ## 修改platfrom为02
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url,headers=headers)
        ## 断言返回的结果
        self.assertIn('avgScore',r.json())

class GetItems(unittest.TestCase):
    ##getItems获取首页列表信息
    @classmethod
    def setUpClass(cls):
        cls.url = MF_URI + 'getItems'

    def test001(self):
        '''
        安卓获取首页列表信息
        1、headers中platform为01
        '''
        ## 修改platform为01
        headers['platform'] = '01'
        ## 请求接口
        r = requests.get(self.url,headers=headers)
        ## 断言返回的结果
        self.assertIsNotNone(r.json())

    def test002(self):
        '''
        iOS获取首页列表信息
        1、headers中platform为02
        '''
        ## 修改platform为01
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url,headers=headers)
        ## 断言返回的结果
        self.assertIsNotNone(r.json())

class Login(unittest.TestCase):
    ## mg_user/login按照 IMEI 区分存储用户信息（分组信息等）
    @classmethod
    def setUpClass(cls):
        cls.url = MF_URI + 'mg_user/login'
    def test001(self):
        '''
        安卓login,a分组
        '''
        headers['platform'] = '01'
        data = {
            'imei':'86{0}0'.format(random.randrange(10000000000,100000000000))
        }
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=data)
        ## {'code': 0, 'data': {'id': 491472, 'imei': '86578420739050', 'type': 'a'}}
        ## 断言返回的结果
        self.assertEqual('a',r.json()['data']['type'])

    def test002(self):
        '''
        安卓login,b分组
        '''
        headers['platform'] = '01'
        data = {
            'imei': '86{0}1'.format(random.randrange(10000000000, 100000000000))
        }
        #请求接口
        r = requests.post(self.url,headers=headers,data=data)
        ##断言返回的结果
        self.assertEqual('b',r.json()['data']['type'])

    def test003(self):
        '''
        ios login,a分组
        '''
        headers['platform'] = '02'
        data = {
            'imei': '86{0}0'.format(random.randrange(10000000000, 100000000000))
        }
        # 请求接口
        r = requests.post(self.url, headers=headers, data=data)
        ##断言返回的结果
        self.assertEqual('a', r.json()['data']['type'])

    def test004(self):
        '''
        ios login,b分组
        '''
        headers['platform'] = '02'
        data = {
            'imei': '86{0}1'.format(random.randrange(10000000000, 100000000000))
        }
        # 请求接口
        r = requests.post(self.url, headers=headers, data=data)
        ##断言返回的结果
        self.assertEqual('b', r.json()['data']['type'])

class Feedback(unittest.TestCase):
    ## /mg_user/feedback,用户意见反馈
    @classmethod
    def setUpClass(cls):
        cls.url = MF_URI + 'mg_user/feedback'
        cls.data = {
            "email":"623037035@qq.com",
            "type":"string",
            "content":"test"
        }
    def test001(self):
        '''
        安卓意见反馈，email为空，错误参数
        '''
        ## 设置平台为安卓
        headers['platform'] = '01'
        ## 设置email为空
        self.data['email'] = ''
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['email'] = '623037035@qq.com'
        ## 断言返回
        self.assertEqual(1,r.json()['code'])

    def test002(self):
        '''
        安卓意见反馈，email为非邮件类型，data为None
        '''
        headers['platform'] = '01'
        ##设置email为错误类型
        self.data['email'] = '234234fddsf'
        ##请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['email'] = '623037035@qq.com'
        ## 断言返回
        self.assertEqual(None,r.json()['data'])
        time.sleep(1)

    def test003(self):
        '''
         安卓意见反馈，email超长，返回data为空
        '''
        headers['platform'] = '01'
        ## 设置email为超长数据
        self.data['email'] = '623037035@qq.com'*100
        ##请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data = '623037035@qq.com'
        ## 断言
        self.assertEqual(None,r.json()['data'])

    def test004(self):
        '''
        安卓意见返回，type为空，返回错误参数
        '''
        headers['platform'] = '01'
        ## 设置type为空
        self.data['type'] = ''
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['type'] = 'string'
        ##断言
        self.assertEqual(1,r.json()['code'])

    def test005(self):
        '''
        安卓意见返回，type为任意类型
        '''
        headers['platform'] = '01'
        ## 设置type为任意类型
        self.data['type'] = 'dfgsdgsdgsf'
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['type'] = '1'
        ## 断言
        self.assertEqual(None,r.json()['data'])

    def test006(self):
        '''
        安卓意见反馈，返回content为空,参数错误
        '''
        headers['platform'] = '01'
        ##设置content为空
        self.data['content'] = ''
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['content'] = 'test'
        ## 断言
        self.assertEqual(1,r.json()['code'])

    def test007(self):
        '''
        安卓意见反馈，返回content超长，
        '''
        headers['platform'] = '01'
        ## 设置content为空
        self.data['content'] = 'test' * 1000
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['content'] = 'test'
        ##  断言
        self.assertEqual(0,r.json()['code'])

    def test008(self):
        '''
        ios意见反馈，email为空，错误参数
        '''
        ## 设置平台为安卓
        headers['platform'] = '02'
        ## 设置email为空
        self.data['email'] = ''
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['email'] = '623037035@qq.com'
        ## 断言返回
        self.assertEqual(1,r.json()['code'])

    def test009(self):
        '''
        ios意见反馈，email为非邮件类型，data为None
        '''
        headers['platform'] = '02'
        ##设置email为错误类型
        self.data['email'] = '234234fddsf'
        ##请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['email'] = '623037035@qq.com'
        ## 断言返回
        self.assertEqual(None,r.json()['data'])

    def test010(self):
        '''
         ios意见反馈，email超长，返回data为空
        '''
        headers['platform'] = '02'
        ## 设置email为超长数据
        self.data['email'] = '623037035@qq.com'*100
        ##请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data = '623037035@qq.com'
        ## 断言
        self.assertEqual(None,r.json()['data'])

    def test011(self):
        '''
        ios意见返回，type为空，返回错误参数
        '''
        headers['platform'] = '02'
        ## 设置type为空
        self.data['type'] = ''
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['type'] = 'string'
        ##断言
        self.assertEqual(1,r.json()['code'])

    def test012(self):
        '''
        ios意见返回，type为任意类型
        '''
        headers['platform'] = '02'
        ## 设置type为任意类型
        self.data['type'] = 'dfgsdgsdgsf'
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['type'] = '1'
        ## 断言
        self.assertEqual(None,r.json()['data'])

    def test013(self):
        '''
        ios意见反馈，返回content为空,参数错误
        '''
        headers['platform'] = '02'
        ##设置content为空
        self.data['content'] = ''
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['content'] = 'test'
        ## 断言
        self.assertEqual(1,r.json()['code'])

    def test014(self):
        '''
        ios意见反馈，返回content超长，
        '''
        headers['platform'] = '02'
        ## 设置content为空
        self.data['content'] = 'test' * 1000
        ## 请求接口
        r = requests.post(self.url,headers=headers,data=self.data)
        self.data['content'] = 'test'
        ##  断言
        self.assertEqual(0,r.json()['code'])

class Sub_up(unittest.TestCase):
    ## 检查订阅页是否需要更新 /sub_up
    @classmethod
    def setUpClass(cls):
        cls.url = MF_URI + 'sub_up'

    def test001(self):
        '''
        安卓请求sub_up
        '''
        ## 请求接口
        r = requests.get(self.url,headers=headers)
        ## 断言
        self.assertEqual(0,r.json()['code'])

    def test002(self):
        '''
        iOS请求sub_up
        '''
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url,headers=headers)
        headers['platform'] = '01'
        ## 断言
        self.assertEqual(0,r.json()['code'])

class  Quizzes(unittest.TestCase):
    ## /quizzes,获取趣味问答数据列表
    @classmethod
    def setUpClass(cls):
        cls.url = MF_URI + 'quizzes'

    def test001(self):
        '''
        安卓请求趣味问答
        '''
        ## 请求接口
        r = requests.get(self.url,headers=headers)
        ## 断言
        self.assertEqual([],r.json())

    def test002(self):
        '''
        ios请求趣味问答
        '''
        headers['platform'] = '02'
        ## 请求接口
        r = requests.get(self.url,headers=headers)
        ## 断言
        self.assertEqual([],r.json())

if __name__ == '__main__':
    unittest.main()

