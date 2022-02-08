import time
import random
from selenium import webdriver
from PIL import Image
from UI_AutomatedTesting_Actual.base.find_element import FindElement
from util.code_demo_API import code_demo

class RegisterFunction():
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    def get_driver(self, url, i):
        '''
        获取driver，并且获取url
        :param url:
        :return:
        '''
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        elif i == 3:
            driver = webdriver.Edge()
        driver.maximize_window()
        driver.get(url)
        return driver

    def send_user_info(self, section, key, data):
        self.get_user_element(section, key).send_keys(data)

    def get_user_element(self, section, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(section, key)
        return user_element

    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmn', 8))
        return user_info

    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element('RegisterElement', 'codetext_image')
        left = code_element.location['x'] * 1.25
        top = code_element.location['y'] * 1.25
        right = code_element.size['width'] * 1.25 + left
        height = code_element.size['height'] * 1.25 + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    def code_online(self, file_name):
        code = code_demo(file_name)
        return code

    def main(self):
        user_info = self.get_range_user()
        user_email = user_info + '@163.com'
        user_name = user_info
        pass_word = 'Abcd1234'
        file_name = 'E:\\Python_study\\UI_AutomatedTesting_Actual\\image\\Test01.png'
        self.get_code_image(file_name)
        code_text = self.code_online(file_name)
        self.send_user_info('RegisterElement', 'useremail', user_email)
        self.send_user_info('RegisterElement', 'username', user_name)
        self.send_user_info('RegisterElement', 'password', pass_word)
        self.send_user_info('RegisterElement', 'codetext', code_text)
        self.get_user_element('RegisterElement', 'register').click()
        time.sleep(3)
        code_error = self.get_user_element('RegisterElement', 'codetetx_error')
        if code_error == None:
            print('注册成功')
        else:
            self.driver.save_screenshot('E:\\Python_study\\UI_AutomatedTesting_Actual\\image\\codeerror.png')
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(1,4):
        register_function = RegisterFunction('http://www.5itest.cn/register', i)
        register_function.main()