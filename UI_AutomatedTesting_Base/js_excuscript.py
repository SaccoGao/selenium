from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.imooc.com/article/follow')


# driver.execute_script(js)
js = 'document.documentElement.scrollTop=100000'
t = True
while t:
    elements = driver.find_elements_by_class_name('article-lwrap')
    for element in elements:
        course_name = element.find_element_by_tag_name('p').text
        print(course_name)
        if course_name == 'Mysql系列-事务':
            element.click()
            t = False
            print('已找到对应的元素')
            break
    driver.execute_script(js)
    time.sleep(3)

time.sleep(10)
driver.close()