from selenium import webdriver # webdriver包
from selenium.webdriver.support import expected_conditions as EC # EC模块，封装了判断的方法
from selenium.webdriver.support.select import Select # 封装了处理下拉框的方法
from selenium.webdriver.support.wait import WebDriverWait # 显示等待
from selenium.webdriver.common.by import By # by定位
from selenium.webdriver.common.action_chains import ActionChains # 封装了操作鼠标的方法
from selenium.webdriver.common.keys import Keys # 封装了键盘上的按钮
import time
import configparser # 封装了读取配置文件的方法
from pykeyboard import PyKeyboard # 键盘事件，集成与PyUserInput包中
import random # 随机方法
from PIL import Image # 处理图片的方法

'''
web自动化基础封装思路
1. 初始化浏览器（打开浏览器、相关浏览器操作：窗口大小，前进后退刷新、切换窗口）
2. 网页操作（进入网页、判断网页正确性）
3. 获取元素
4. 操作元素（点击事件、输入事件、下拉框处理）
'''

# open_browser  打开浏览器
driver = webdriver.Chrome()

# 启动Chrome浏览器的默认参数
options = webdriver.ChromeOptions()  # 实例化Chrome浏览器启动参数配置的方法
prefs = {'启动参数1':'配置1', '启动参数2':'配置2'}  # 对需要的参数进行编写
options.add_experimental_option('prefs', prefs)  # 配置启动参数
driver = webdriver.Chrome(chrome_options = options)  # 启动浏览器，并把参数输入到chrome_options中
'''
Chrome常用启动参数
1. 'download.default_directory':'C:\\Users\GAOBO\Desktop\download_test' - 默认浏览器下载文件的地址
2. 'profile.default_content_settings.popups':0 - 下载文件时不打开弹窗
'''

# 启动Firefox浏览器的默认参数
profile = webdriver.FirefoxProfile()  # 实例化Firefox浏览器启动参数的方法
profile.set_preference('启动参数1', '配置1')
Driver = webdriver.Firefox(firefox_profile = profile)# 启动浏览器，并把参数输入到firefox_profile中
'''
Firefox常用启动参数
1. 'browser.download.dir', 'C:\\Users\GAOBO\Desktop\download_test' - 新增下载地址
2. 'browser.download.folderList', 2 - 选择配置的第二个下载地址（填1则为默认地址）
3. 'browser.helperApps.neverAsk.saveToDisk', 'application/文件类型' - 文件类型，如zip、exe等，配置后下载此类文件不弹确认弹窗
'''

# 浏览器常见操作
driver.maximize_window()  # 窗口最大化
driver.minimize_window()  # 窗口最小化
driver.set_window_size()  # 指定窗口尺寸
driver.back()  # 后退
driver.forward()  # 前进
driver.refresh()  # 刷新
driver.get('url')  # 输入地url

# assert_title  通过html的title判断打开的页面是否正确（代码见UI_AutomatedTesting_Base -> assert_title模块）
assert_title_1 = EC.title_contains('慕课网')  # 模糊匹配
result_1 = assert_title_1(driver)  # 使判断结果为bool值

assert_title_2 = EC.title_is('慕课网')  # 精确匹配
result_2 = assert_title_2(driver)  # 使判断结果为bool值

# open_windows  切换窗口（代码见UI_AutomatedTesting_Base -> open_windows模块）
handle_list = driver.window_handles  # 获取句柄列表
current_handle = driver.current_window_handle  # 获取当前页面的句柄
driver.switch_to.window('句柄')  # 切换到指定的句柄页

# 定位元素
driver.find_element_by_id()  # 通过id定位元素
driver.find_element_by_class_name()  # 通过class定位元素
driver.find_elements_by_class_name()[1] # 通过class查找整个页面的元素，取其中的第2个，可嵌套class使用
driver.find_element_by_link_text()  # 通过文本定位
driver.find_element_by_partial_link_text()  # 通过正则表达式文本定位
driver.find_element_by_css_selector('')  # css定位，corppath插件可找到css地址
driver.find_element_by_xpath('')  # xpth定位

# 等待
# 显式等待
'''
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
driver:浏览器驱动
timeout：最长超时时间，单位秒
poll_frequency:检测的间隔时长，默认0.5s
ignored_exceptions:超时后的异常信息，默认情况下抛NoSuchElementException
'''
locator = (By.ID, '定位元素值')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)) # 判断页面元素是否出现
WebDriverWait(driver,10).until(EC.title_is("title")) # 判断title是否出现，精确判断
WebDriverWait(driver,10).until(EC.title_contains("title")) # 判断title是否出现，模糊判断

# 页面操作
driver.find_element_by_class_name().send_keys()  # send_key()，输入
driver.find_element_by_class_name().click()  # click，点击
driver.find_element_by_class_name().is_selected()  # 用于判断勾选框是否被勾选，如果被勾选则为True
driver.find_element_by_class_name().send_keys('文件路径') #用于上传文件，html标签为input
driver.find_element_by_class_name().clear() # 清除当前输入框的内容
driver.find_element_by_class_name().get_attribute() # 获取标签的值

# 鼠标事件（代码见UI_AutomatedTesting_Base -> action_mouse模块）
actionmouse = ActionChains(driver) # 实例化ActionChains类，参数需要传入driver对象
actionmouse.move_to_element(element) # 把鼠标移动到对应的元素上
actionmouse.key_down(Keys.键位名) # Keykey_down() 按下某个键盘上的键，结合Keys类使用
actionmouse.key_up(Keys.键位名) # Keykey_up() 松开之前按下的键，结合key_down、Keys类使用
actionmouse.执行链.perform() # perform()提交执行链的操作，不提交则不执行

# 键盘事件（PyKeyboard，代码见UI_AutomatedTesting_Base -> send_head模块）
pykey = PyKeyboard() # 实例化PyKeyboard类，使用这个类，对键盘进行操作
pykey.type_string('') # 向当前光标所在输入内容，不限于html网页
pykey.tap_key(pykey.enter_key) # 点击回车键，一般用于切换输入法
pykey.tap_key(pykey.shift_key) # 点击shift键，默认左shift
pykey.tap_key(pykey.shift_l_key) # 点击左shift键
pykey.tap_key(pykey.shift_r_key) # 点击右shift键

# 键盘上的键（Keys类）
Keys.键位名

# 读取配置文件，使用configparser包（代码见UI_AutomatedTesting_Base -> read_init模块）
cf = configparser.ConfigParser() # 实例化ConfigParser类
cf.read('配置文件路径') # 读取配置文件
cf.get('setion', 'key') # 获取配置文件内指定的内容，返回key对应的字符串，可通过

# 弹窗处理
driver.switch_to.alert.accept()  # 定位内嵌式弹窗，点击确定
driver.switch_to.alert.dismiss()  # 定位内嵌式弹窗，点击取消
driver.switch_to.alert.send_keys('')  # 定位内嵌式弹窗，输入（如果有输入框）

# 切换iframe元素
driver.switchTo().frame("framename or id") # 进入iframe
driver.switchTo().defaultContent() # 跳出iframe

# 模态框及焦点切换
driver.switch_to.active_element.send_keys('')  # 跳转后，系统已自动定位焦点，此时可以不通过元素定位，直接输入

# 下拉框处理（代码见UI_AutomatedTesting_Base -> select_element模块）
select_element = driver.find_elements_by_name('job')[1]
Select(select_element).select_by_value() # 根据value值定位
Select(select_element).select_by_index() # 根据index定位
Select(select_element).select_by_visible_text() # 根据文本定位

# 向html网页发送js代码（代码见UI_AutomatedTesting_Base -> calendar_demo模块）
driver.execute_script(js)
'''
常用js
1. documenet.getElementById('定位元素值').removeAttrubute('readonly') - 删除input的只读属性
2. document.documentElement.scrollTop=100000 - 滑动到页面底部
'''

# 常用的数据处理方法
random.sample() # 数据源、截取长度；用于抽取随机的元素
''.join('序列') # 用于符号连接序列内的值，生成字符串

# 截图(代码见save_png)
driver.get_screenshot_as_file('地址/名称.png')
driver.save_screenshot('地址/名称.png')

# 图片处理
driver.find_element(By.ID, '元素值').location # 获取元素左上角的xy坐标，以字典的形式保存{'x':x, 'y':y}
driver.find_element(By.ID, '元素值').size # 获取元素的长和高，以字典的形式保存{'width':w, 'height':h}
left = element.location['x']
top = element.location['y']
right = element.size['width']+left
height = element.size['height']+top
im = Image.open('图片地址') # 打开图片
img = im.corp((left, top, right, height)) # 对打开的图片进行截图
img.save('路径/名称') # 保存截图
