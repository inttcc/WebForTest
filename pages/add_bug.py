#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from commondef.base import Base


class AddBugDef(Base):
    '''禅道提交bug的封装'''

    loc_test = ("link text", "测试")#测试模块
    loc_bug = ("css selector", "#modulemenu > ul > li:nth-child(2) > a")#bug模块
    loc_add_bug = ("css selector", "#createActionMenu > a")#提bug按钮
    loc_affect_version = ("css selector", "#openedBuild_chosen > ul")#影响版本
    loc_trunk = ("css selector", "#openedBuild_chosen > div > ul")#主干
    loc_bug_titile = ("id", "title")#bug标题

    #需切换到iframe
    loc_repeat_steps=("class name","article-content")#重现步骤
    loc_save_bug=("id","submit")#保存

    #新增的列表
    loc_new=("xpath","//*[@id='datatable-bugList']/div[2]/div[1]/div/table/tbody/tr[1]/td[5]/a")

    def add_bug(self,bug_title,repeat_steps):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_add_bug)
        self.click(self.loc_affect_version)
        self.click(self.loc_trunk)
        self.sendKeys(self.loc_bug_titile,bug_title)

        self.driver.switch_to.frame(0)
        self.clear(self.loc_repeat_steps)
        self.sendKeys(self.loc_repeat_steps,repeat_steps)
        self.driver.switch_to_default_content()
        self.click(self.loc_save_bug)


    def is_add_bug_success(self,text_):
      return  self.is_text_in_element(self.loc_new,text_)

if __name__ == '__main__':
    from pages.login_page import LoginPage
    from selenium import webdriver
    import time
    driver=webdriver.Chrome()
    driver.get('http://zt.huolail.com/user-login-Lw==.html')
    zentao = LoginPage(driver)
    zentao.login('tancichao', 'huolaile123')
    zentao=AddBugDef(driver)
    timestr=time.strftime('(%Y-%m-%d %H:%M:%S)')
    bug_title="bug的标题"+timestr
    repeat_steps="bug的重现步骤"
    zentao.add_bug(bug_title,repeat_steps)
    result=zentao.is_add_bug_success(bug_title)
    print(result)