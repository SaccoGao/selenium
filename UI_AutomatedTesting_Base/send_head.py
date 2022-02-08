# coding = UTF-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pykeyboard import PyKeyboard  # 键盘事件，集成与PyUserInput包中
import time

driver = webdriver.Chrome()
driver.get('http://www.imooc.com')
driver.maximize_window()
driver.find_element_by_id('js-signin-btn').click()
time.sleep(1)
driver.find_element_by_name('email').send_keys('15007534131')
time.sleep(1)
driver.find_element_by_name('password').send_keys('BECAUSEZZZ002')
driver.find_element_by_class_name('moco-btn').click()
time.sleep(1)
driver.get('https://www.imooc.com/user/setprofile')
time.sleep(1)
driver.find_element_by_class_name('avator-img').click()
time.sleep(1)
driver.find_element_by_class_name('update-avator').click()
time.sleep(1)

# 上传文件,html标签为input
driver.find_element_by_id('upload').send_keys('C:\\Users\\GAOBO\\Desktop\\贝拉拉与钱多多.png')
time.sleep(3)
# driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div/div[2]/div/a[1]').click()

# 上传文件，html标签非input
driver.find_element_by_class_name('avator-btn-fake').click()
time.sleep(2)

pykey = PyKeyboard()
pykey.tap_key(pykey.shift_l_key) # 点击shift，切换输入法
pykey.type_string('C:\\Users\\GAOBO\\Desktop\\fifteen.png') # 输入文件所在的路径
time.sleep(5)
pykey.tap_key(pykey.enter_key) # 键盘事件，点击enter键
time.sleep(5)
driver.close()