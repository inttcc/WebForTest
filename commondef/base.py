#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    '''二次封装'''

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 2
        self.poll_frequency = 0.5

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value")')
        else:
            print('正在定位元素信息，定位方式——>%s，value值——>%s' % (locator[0], locator[1]))
            element = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                lambda x: x.find_element(*locator))
            return element

    def findElementNew(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value")')
        else:
            print('正在定位元素信息，定位方式——>%s，value值——>%s' % (locator[0], locator[1]))
            element = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                EC.presence_of_element_located(locator))
            return element

    def findElements(self, locator):
        try:
            if not isinstance(locator, tuple):
                print('locator参数类型错误，必须传元组类型：loc=("id","value")')
            else:
                print('正在定位元素信息，定位方式——>%s，value值——>%s' % (locator[0], locator[1]))
                elements = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    lambda x: x.find_elements(*locator))
                return elements
        except:
            return []

    def sendKeys(self, locator, text):
        element = self.findElement(locator)
        element.send_keys(text)

    def click(self, locator):
        element = self.findElement(locator)
        element.click()

    def clear(self, locator):
        element = self.findElement(locator)
        element.clear()

    def isSelected(self, locator):
        element = self.findElement(locator)
        flag = element.is_selected()
        return flag

    def title_is(self, title):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(EC.title_is(title))
            return result
        except:
            return False

    def title_contains(self, title):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text_):
        try:
            if not isinstance(locator, tuple):
                print('locator参数类型错误，必须传元组类型：loc=("id","value")')
            else:
                print('正在定位元素信息，定位方式——>%s，value值——>%s' % (locator[0], locator[1]))
                result = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    EC.text_to_be_present_in_element(locator, text_))
                return result
        except:
            return False

    def is_text_in_element_value(self, locator, text_):
        try:
            if not isinstance(locator, tuple):
                print('locator参数类型错误，必须传元组类型：loc=("id","value")')
            else:
                print('正在定位元素信息，定位方式——>%s，value值——>%s' % (locator[0], locator[1]))
                result = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    EC.text_to_be_present_in_element_value(locator, text_))
                return result
        except:
            return False

    def is_alert(self):
        try:
            return WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(EC.alert_is_present())
        except:
            return False

    def isElementExist(self, locator):
        try:
            if not isinstance(locator, tuple):
                print('locator参数类型错误，必须传元组类型：loc=("id","value")')
            else:
                print('正在定位元素信息，定位方式——>%s，value值——>%s' % (locator[0], locator[1]))
                WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                    EC.presence_of_element_located(locator))
                return True
        except:
            return False

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        element=self.findElement(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_by_index(self,locator,index=0):
        '''通过索引定位select选择框，index从0开始'''
        element=self.findElement(locator)#定位select栏
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value=''):
        '''通过value定位select选择框'''
        element=self.findElement(locator)#定位select栏
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本值定位select选择框'''
        element=self.findElement(locator)#定位select栏
        Select(element).select_by_visible_text(text)

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target=self.findElement(locator)
        self.driver.execute_script('argument[0].scrollIntoView();',target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        self.driver.execute_script('window.scrollTo(0,0);')

    def js_scroll_bottom(self):
        '''滚动到底部'''
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')


if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    # driver.get('http://zt.huolail.com/user-login-Lw==.html')
    # zentao = Base(driver)
    # loc1 = ('id', 'account')
    # loc2 = ('name', 'password')
    # loc3 = ('id', 'submit')
    # loc4 = ('css selector', '#login-form > form > table > tbody > tr:nth-child(4) > td > a')
    # loc5 = ('id', 'keepLoginon')
    #
    # zentao.sendKeys(loc1, 'tancichao1')
    # zentao.sendKeys(loc2, 'huolaile123')
    # zentao.click(loc4)
    driver.get('https://hz.58.com/')
    my=Base(driver)
    time.sleep(1)
    # my.js_scroll_bottom()
    # time.sleep(1)
    # my.js_scroll_top()
    my.js_focus_element(('link text','汽车服务'))


