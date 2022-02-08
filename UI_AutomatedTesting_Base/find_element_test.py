from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.imooc.com')
# element_name = driver.find_element_by_name('password')
time.sleep(5)
# element_text = driver.find_element_by_link_text('Python工程师')
# element_text = driver.find_element_by_partial_link_text('Python工程师')
# element_css = driver.find_element_by_css_selector('')  # corppath插件
# element_xpth = driver.find_element_by_xpath('')
time.sleep(2)

LOCATOR = (By.XPATH, "id")
EC.visibility_of_element_located(LOCATOR)
# WebDriverWait().until(a)

EC.visibility_of_all_elements_located()

driver.close()


