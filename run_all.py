#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
import os

# from BeautifulReport import BeautifulReport as b

casePath = './case'
reportPath='./report/result.html'
# reportPath = r'C:\Users\Administrator\Desktop\result.html'


def all_case():
    rule = 'test*.py'
    discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
    suite = unittest.TestSuite()
    suite.addTest(discover)
    print(discover)
    return suite


if __name__ == '__main__':
    fp = open(reportPath, 'wb')
    runner = HTMLTestRunner(stream=fp, title='登录禅道', description='测试登录模块')
    runner.run(all_case())
    # runner.report(filename='result', description='测试deafult报告', log_path=r'C:\Users\Administrator\Desktop')
    fp.close()
    print('生成测试报告文件result.html，路径为：' + os.path.abspath(reportPath))

    # fp=open(reportPath,'a')
    # runner=unittest.TextTestRunner(stream=fp)
    # runner.run(all_case())
    # fp.close()
    # print('生成测试报告文件result.txt，路径为：'+os.path.abspath(reportPath))
