# coding = UTF-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
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
driver.find_element_by_class_name('pull-right').click()
time.sleep(3)

# 下拉框处理
select_element = driver.find_elements_by_name('job')[1]
Select(select_element).select_by_index(5)
time.sleep(3)
Select(select_element).select_by_visible_text('Python工程师')
time.sleep(5)
driver.close()
# driver.get('')