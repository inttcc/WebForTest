#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from mytools import HTMLTestRunner_cn
import os

casePath='./case'
rule='test*.py'
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath='./report/result.html'
# reportPath=r'C:\Users\Administrator\Desktop\result.html'
fp=open(reportPath,'wb')
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='登录禅道', description='测试登录模块')
runner.run(discover)
fp.close()
print('生成测试报告文件result.html，路径为：'+os.path.abspath(reportPath))