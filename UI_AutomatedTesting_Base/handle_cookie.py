from selenium import webdriver
import configparser
import time

driver = webdriver.Chrome()
driver.get('https://order.imooc.com/myorder')
time.sleep(2)
driver.delete_all_cookies()
cookie = {
    'domain': '.imooc.com',
    'expiry': 1638632028,
    'httpOnly': False,
    'name': 'apsid',
    'path': '/',
    'secure': False,
    'value': 'E3NTM4OWY1ZWM0ODc0MDJkM2Q1NTJjYWIzYzEyYzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMTAwMzcxMzIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADkxNDU1MTIwZGFlYWQwZDFlN2EzMDQyZTZjNmU1OWMx3U%2BiYYAu%2BWA%3DZW'
    }
time.sleep(2)
driver.add_cookie(cookie)
time.sleep(2)
driver.get('https://order.imooc.com/myorder')
time.sleep(5)

'''
driver.get('http://www.imooc.com/')

cf = configparser.ConfigParser()
cf.read('E:\Python_study\\UI_AutomatedTesting_Base\config\localElement.ini', encoding = 'UTF-8')
login = cf.get('element', 'login').split(',')[1]
username = cf.get('element', 'username').split(',')[1]
password = cf.get('element', 'password').split(',')[1]
print(login+'/'+username+'/'+password)

driver.find_element_by_id(login).click()
time.sleep(2)
driver.find_element_by_name(username).send_keys('15007534131')
driver.find_element_by_name(password).send_keys('BECAUSEZZZ002')
driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input').click()
time.sleep(3)

cookie_list = driver.get_cookies()
print(cookie_list)
'''

driver.close()