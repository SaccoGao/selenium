from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://www.imooc.com')
element = driver.find_element_by_class_name('menuContent').find_elements_by_class_name('item')[0]
ActionChains(driver).move_to_element(element).perform()
time.sleep(2)
driver.find_element_by_partial_link_text('前端工具').click()
time.sleep(3)
driver.close()