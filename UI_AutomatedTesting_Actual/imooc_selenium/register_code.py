from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from UI_AutomatedTesting_Actual.util import code_demo_API
import time
import random

driver = webdriver.Chrome()

# 浏览器初始化
def driver_init():
    driver.maximize_window()
    driver.get('http://www.5itest.cn/register')
    time.sleep(5)

# 获取element信息
def get_element(by, value):
    if by == 'ID':
        element = driver.find_element(By.ID, value)
    else:
        element = None
        print('请输入正确的by和value')
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklmn', 8))
    return user_info

# 获取验证码图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = get_element('ID', 'getcode_num')
    left = code_element.location['x'] * 1.25
    top = code_element.location['y'] * 1.25
    right = code_element.size['width'] * 1.25 + left
    height = code_element.size['height'] * 1.25 + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    img.save(file_name)

# 解析图片获取验证码
def code_online(file_name):
    code = code_demo_API.code_demo(file_name)
    return code

# 运行主程序
def run_main():
    user_info = get_range_user()
    user_email = user_info + '@163.com'
    user_name = user_info
    pass_word = 'Abcd1234'
    file_name = '/UI_AutomatedTesting_Actual/image/Test01.png'
    driver_init()
    get_element('ID', 'register_email').send_keys(user_email)
    get_element('ID', 'register_nickname').send_keys(user_name)
    get_element('ID', 'register_password').send_keys(pass_word)
    get_code_image(file_name)
    text = code_online(file_name)
    get_element('ID', 'captcha_code').send_keys(text)
    get_element('ID', 'register-btn').click()
    driver.quit()

run_main()