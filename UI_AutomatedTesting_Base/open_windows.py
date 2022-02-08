from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.imooc.com/user/newlogin/from_url/')
time.sleep(3)
driver.find_element_by_name('email').send_keys('15007534131')  # send_keys，输入
driver.find_element_by_name('password').send_keys('BECAUSEZZZ002')
driver.find_element_by_class_name('moco-btn').click()  # click，点击
time.sleep(2)
driver.get('https://www.imooc.com/user/setbindsns')
driver.find_elements_by_class_name('inner-i-box')[1].find_element_by_class_name('moco-btn-normal').click()
hend_list = driver.window_handles  # 获取句柄
current_handle = driver.current_window_handle # 获取当前页面句柄
time.sleep(15)

for i in hend_list:
    if i != current_handle:
        driver.switch_to.window(i)  # 切换到句柄对应的页面
        if EC.title_contains('网站连接')(driver) == True:
            break

driver.find_element_by_class_name('qr-change-logo').click()
time.sleep(2)
driver.find_element_by_id('username').send_keys('test')

time.sleep(3)
driver.close()