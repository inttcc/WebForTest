#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# flag = EC.title_is("百度一下")(driver)
# print(flag)
# flag = EC.title_contains("百度一下")(driver)
# print(flag)
#
# loc1 = ('link text', '设置')
# flag = EC.text_to_be_present_in_element(loc1, '设置')(driver)
# print(flag)
# driver.quit()
driver.get('https://www.126.com/')
# driver.switch_to.frame(driver.find_element_by_css_selector('#loginDiv>iframe'))
driver.switch_to.frame(0)
driver.find_element_by_name('email').send_keys('654684')