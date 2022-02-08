from selenium import webdriver
driver = webdriver.Chrome
driver.get('日历控件')
element = driver.find_element_by_id('定位元素值')  # 定位控件元素
element.clear()  # 清除原有的值
element.send_keys('2021-11-17')  # 输入所需日期

driver.get('日历控件，JS中设置了readonly')
element = driver.find_element_by_id('定位元素值')  # 定位控件元素
js = "documenet.getElementById('定位元素值').removeAttrubute('readonly')"  # 使用js去除readonly属性
driver.execute_script(js)  # execute_script()，在当前页面执行js
element.clear()  # 清除原有的值
element.send_keys('2021-11-17')  # 输入所需日期
driver.close()