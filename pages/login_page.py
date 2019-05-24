#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.keys import Keys

from commondef.base import Base


class LoginPage(Base):
    '''登录页的封装类'''
    login_url = 'http://zt.huolail.com/user-login-Lw==.html'

    loc_user = ('id', 'account')  # 用户名
    loc_psw = ('name', 'password')  # 密码
    loc_submit = ('id', 'submit')  # 登录按钮
    loc_keep_login = ('id', 'keepLoginon')  # 保持登录按钮
    loc_forget_psw = ('link text', '忘记密码')  # 忘记密码

    loc_forgetpswpage_refresh = ('class name', 'btn')  # 点击忘记密码后跳转页面下的刷新按钮

    def login(self, username, password, keep_login=False):
        '''登录的调用方法'''
        self.input_user(username)
        self.input_psw(password)
        if keep_login: self.click_keep_login()
        self.click_login_button()

    def input_user(self, username=""):
        self.sendKeys(self.loc_user, username)

    def input_psw(self, password=""):
        self.sendKeys(self.loc_psw, password)

    def click_keep_login(self):
        self.click(self.loc_keep_login)

    def click_login_button(self):
        self.click(self.loc_submit)

    def click_forget_psw(self):
        self.click(self.loc_forget_psw)

    def is_refresh_exist(self):
        return self.isElementExist(self.loc_forgetpswpage_refresh)

    def press_enter(self):
        self.sendKeys(self.loc_psw, Keys.ENTER)

    def is_alert(self):
        '''判断是否弹出提示框，弹出提示框表示登录失败'''
        try:
            self.driver.switch_to.alert
        except:
            return False
        else:
            sleep(1)
            self.driver.switch_to.alert.accept()
            return True


if __name__ == '__main__':
    from selenium import webdriver
    from pykeyboard import PyKeyboard

    driver = webdriver.Chrome()
    zentao = LoginPage(driver)
    driver.get(zentao.login_url)
    zentao.login('tancichao','huolaile123')
    driver.get('http://zt.huolail.com/bug-create-11-0-moduleID=0.html')
    zentao.click(('name','files[]'))
    sleep(3)
    k=PyKeyboard()
    k.type_string(r'C:\Users\Administrator\Desktop\tu\a.jpg')
    k.tap_key(k.enter_key)
    k.tap_key(k.enter_key)