from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('http://www.imooc.com/')
title_name = driver.title # 获取html的title
if '慕课网' in title_name:
    print('打开正确')
else:
    print('打开错误')

titlr_a = EC.title_is('慕课网') # 精确匹配html title
print(titlr_a(driver))

title_b = EC.title_contains('慕课网') # 模糊匹配html title
print(title_b(driver))

