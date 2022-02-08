from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://imooc.com')
now_time = time.strftime('%Y.%m.%d-%H.%M.%S')
print(now_time)
driver.get_screenshot_as_file('{0}.png'.format(now_time))
driver.close()
driver.save_screenshot()
