import requests
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qt import Ui_btneu6

class mywindow(Ui_btneu6):
    def login_button(self):
        username = self.titleEdit.text()
        password = self.authorEdit.text()
        browser = login_btneu6(url_search,username,password)
    def search_button(self):
        keyword = self.reviewEdit.text()
        searchKey(browser,keyword)

def browser_init(isWait):
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\Users\\Halouccr\\Desktop\\BT'}
    options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
    browser.maximize_window()  #最大化屏幕
    #browser.set_window_size(500,500)
    if isWait:
        browser.implicitly_wait(10)
    return browser

def login_btneu6(url,username,key):
    browser.get(url)
    browser.implicitly_wait(5)
    try:
        user_name = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[starts-with(@id,"username_L")]')))
        user_name.send_keys(username)
        pass_word = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[starts-with(@id,"password3_L")]')))
        pass_word.send_keys(key)
        browser.find_element_by_name('loginsubmit').send_keys(Keys.ENTER)
    except:
        browser.quit()
        print('没有登录成功')
    return browser

def searchKey(browser,keyword):
    element = browser.find_element_by_id('srchtxt_1')
    element.send_keys(keyword)
    browser.implicitly_wait(2)
    element.send_keys(Keys.ENTER)
##########################为什么搜索按钮不能输入
    #search_button = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME,'searchsubmit')))
    #search_button.send_keys(Keys.ENTER)


if __name__=="__main__":

    url_head = "http://bt.neu6.edu.cn"
    href = 'search.php'
    url_search = url_head + '/' + href

    for num in range(100):
        print ('*',end='')
    print (' ')

    browser = browser_init(True)

    app = QtWidgets.QApplication(sys.argv)
    new_window = mywindow()
    new_window.show()
    sys.exit(app.exec_())

##这段代码不能用是因为，想根据id找到href，但是找到的tag的属性只有id
    # search_link = bt_soup.find('li',id="mn_Ne008")
    # print (search_link)
    # print (type(search_link))

    # print(search_link.attrs)
    # print(search_link.name)

    # match = bt_soup.find_all(string = "search.php")
    # print (match)
    # #match = re.search('href',search_link)
    # print (match)

