#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
'''
1.正确用户名，密码登录
2.正确用户名，密码登录，点保持登录
3.用户名为空点击登录
4.密码为空点击登录
5.用户名和密码都为空点击登录
6.错误用户名或错误密码登录
7.点击忘记密码
8.用ENTER键代替登录按钮登录

'''


class ZentaoLoginPage(unittest.TestCase):
    '''整个登录页面的测试'''

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.zentao=LoginPage(cls.driver)


    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get(self.zentao.login_url)

    def test_01(self):
        '''正确用户名，密码登录'''
        self.zentao.input_user('tancichao')
        self.zentao.input_psw('huolaile123')
        self.zentao.click_login_button()
        self.assertTrue(not self.zentao.is_alert())

    def test_02(self):
        '''正确用户名，密码登录，点保持登录'''
        self.zentao.input_user('tancichao')
        self.zentao.input_psw('huolaile123')
        self.zentao.click_keep_login()
        self.zentao.click_login_button()
        self.assertTrue(not self.zentao.is_alert())

    def test_03(self):
        '''用户名为空点击登录'''
        self.zentao.input_user()
        self.zentao.input_psw('huolaile123')
        self.zentao.click_login_button()
        self.assertTrue(self.zentao.is_alert())

    def test_04(self):
        '''密码为空点击登录'''
        self.zentao.input_user('tancichao')
        self.zentao.input_psw()
        self.zentao.click_login_button()
        self.assertTrue(self.zentao.is_alert())

    def test_05(self):
        '''用户名和密码都为空点击登录'''
        self.zentao.input_user()
        self.zentao.input_psw()
        self.zentao.click_login_button()
        self.assertTrue(self.zentao.is_alert())

    def test_06(self):
        '''错误用户名或错误密码登录'''
        self.zentao.input_user('tancichao64654')
        self.zentao.input_psw('huolaile123897987')
        self.zentao.click_login_button()
        self.assertTrue(self.zentao.is_alert())

    def test_07(self):
        '''点击忘记密码'''
        self.zentao.click_forget_psw()
        self.assertTrue(self.zentao.is_refresh_exist())

    def test_08(self):
        '''用ENTER键代替登录按钮登录'''
        self.zentao.input_user('tancichao')
        self.zentao.input_psw('huolaile123')
        self.zentao.press_enter()
        self.assertTrue(not self.zentao.is_alert())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()