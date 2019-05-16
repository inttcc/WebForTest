#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from pages.add_bug import AddBugDef
from selenium import webdriver
from pages.login_page import LoginPage
import time

class ZentaoAddBug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.zentao_add_bug=AddBugDef(cls.driver)
        cls.zentao_login=LoginPage(cls.driver)

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get('http://zt.huolail.com/user-login-Lw==.html')

    def test_add_bug(self):
        self.zentao_login.login('tancichao','huolaile123')
        timestr = time.strftime('(%Y-%m-%d %H:%M:%S)')
        bug_title = "bug的标题" + timestr
        repeat_steps = "bug的重现步骤"
        self.zentao_add_bug.add_bug(bug_title,repeat_steps)
        self.assertTrue(self.zentao_add_bug.is_add_bug_success(bug_title))
        
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()