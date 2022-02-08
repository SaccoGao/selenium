import time

from UI_AutomatedTesting_Base import read_init
from UI_AutomatedTesting_Base import open_browser

read_ini = read_init.ReadIni('E:\Python_study\\UI_AutomatedTesting_Base\config\localElement.ini')
selenium_driver = open_browser.SeleniumDriver('Chrome')
data = read_ini.get_value('element', 'username')
data_info = data.split(',')
username_by = data_info[0]
username_local = data_info[1]
selenium_driver.get_url('http://www.imooc.com/')
time.sleep(5)
selenium_driver.click_element('xpath', '//*[@id="js-signin-btn"]')
time.sleep(3)
selenium_driver.send_value(username_by, username_local, '15007534131')
time.sleep(3)
selenium_driver.close_driver()