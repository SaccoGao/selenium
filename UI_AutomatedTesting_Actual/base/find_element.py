# coding=utf-8

from UI_AutomatedTesting_Actual.util.read_config import readini_element
from selenium.webdriver.common.by import By
import time
import os

class FindElement():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, section, key):
        data = readini_element.get_value(section, key)
        by = data.split(',')[0]
        value = data.split(',')[1]
        try:
            if by == 'ID':
                element = self.driver.find_element(By.ID, value)
            elif by == 'CLASS_NAME':
                element = self.driver.find_element(By.CLASS_NAME, value)
            return element
        except:
            # now_time = time.strftime('%Y%m%d%H%M%S')
            # file_path = os.path.join(os.getcwd(),'\\Python_study\\UI_AutomatedTesting_Actual\\image\\{0}.png'.format(now_time))
            # self.driver.save_screenshot(file_path)
            return None