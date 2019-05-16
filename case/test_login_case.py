#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver
from pages.login_page import LoginPage


class ZenTaoLogin(unittest.TestCase):

    # 前置条件，只需执行一次
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.zentao =LoginPage(cls.driver)
        # cls.driver.maximize_window()
        sleep(2)

    # 前置条件，每次执行用例前都需执行
    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get('http://zt.huolail.com/user-login-Lw==.html')



    # 用例1：登录正确账号和密码
    def test01(self):
        '''登录正确账号和密码'''
        self.zentao.login('tancichao', 'huolaile123')
        sleep(2)
        self.assertTrue( self.zentao.is_alert())

    # 用例2：登录错误账号和密码
    def test02(self):
        '''登录错误账号和密码'''
        self.zentao.login('cccc', 'ccccccc')
        sleep(2)
        self.assertTrue(self.zentao.is_alert())



    # 后置条件，只需执行一次
    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    # 后置条件，每次执行完用例都需执行
    # def tearDown(self):
    #     self.driver.delete_all_cookies()
    #     self.driver.refresh()

if __name__ == '__main__':
    unittest.main()