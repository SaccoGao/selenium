from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
from UI_AutomatedTesting_Actual.util import code_demo_API

# 打开浏览器，跳转到登录页
driver = webdriver.Edge()
driver.maximize_window()
driver.get('http://www.5itest.cn/register')

# 通过title判断跳转的页面
assert_title = EC.title_contains('注册 - 快乐学 - 快乐学习 - Powered By EduSoho')
print(assert_title(driver))

# 显式等待
element = driver.find_element(By.ID, 'register-btn')
locator = (By.ID, 'register-btn')
a = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))

time.sleep(5)

# 截取整个页面，保存为png
now_time = time.strftime('%Y%m%d-%H%M%S')
file_name = 'C:\\Users\\GAOBO\\Desktop\\test\\{0}.png'.format(now_time)
driver.save_screenshot(file_name)

# 获取验证码图片的坐标
code_element = driver.find_element(By.ID, 'getcode_num')
left = code_element.location['x']*1.25
top = code_element.location['y']*1.25
right = code_element.size['width']*1.25+left
height = code_element.size['height']*1.25+top

# 截取验证码图片，保存为png
code_file_name = 'C:\\Users\\GAOBO\\Desktop\\test\\{0}_1.png'.format(now_time)
im = Image.open(file_name)
img = im.crop((left, top, right, height))
img.save(code_file_name)

# 通过验证码图片，破解验证码
code = code_demo_API.code_demo(code_file_name)
print(code)

# 输入信息进行注册
useremail = driver.find_element(By.ID, 'register_email')
useremail.send_keys('Sacco@163.com')

username = driver.find_element(By.ID, 'register_nickname')
username.send_keys('Sacco')

password = driver.find_element(By.ID, 'register_password')
password.send_keys('Sacco')

codedemo = driver.find_element(By.ID, 'captcha_code')
codedemo.send_keys(code)

time.sleep(20)

driver.quit()