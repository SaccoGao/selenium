from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytesseract
from PIL import Image

driver = webdriver.Edge()
driver.maximize_window()
driver.get('http://www.5itest.cn/register')
time.sleep(6)

# 截全图
now_time = time.strftime('%Y%m%d-%H%M%S')
driver.save_screenshot('C:\\Users\\GAOBO\\Desktop\\test\\{0}.png'.format(now_time))

# 定位验证码图片坐标
code_element = driver.find_element(By.ID, 'getcode_num')
left = code_element.location['x']*1.25
top = code_element.location['y']*1.25
right = code_element.size['width']*1.25+left
height = code_element.size['height']*1.25+top

# 截取验证码图片
image = Image.open('C:\\Users\\GAOBO\\Desktop\\test\\{0}.png'.format(now_time))
image = image.crop((left, top, right, height))
image.save('C:\\Users\\GAOBO\\Desktop\\test\\{0}_1.png'.format(now_time))

# 读取图片上的文字
text = pytesseract.image_to_string(image)
print(text)

driver.quit()
