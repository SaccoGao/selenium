from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from UI_AutomatedTesting_Base.read_init import readini
from UI_AutomatedTesting_Base.handle_json import handle_json
from selenium.webdriver.support.select import Select
from pykeyboard import PyKeyboard
import time

class SeleniumDriver():
    def __init__(self, browser):  # 把 调用打开浏览器的函数 封装在构造函数内
        self.Driver = self.open_broeser(browser)

    def open_broeser(self, browser):
        '''
        打开浏览器方法
        :param browser: 浏览器名称
        :return:
        '''
        try:  # 容错，如果内部的代码执行错误，会立刻终止，并执行except内的代码
            if browser == 'Chrome':
                options = webdriver.ChromeOptions()
                prefs = {
                    'download.default_directory': 'C:\\Users\GAOBO\Desktop\download_test',
                    'profile.default_content_settings.popups': 0
                }
                options.add_experimental_option('prefs', prefs)
                # 启动Chrome浏览器，启动参数配置默认下载路径
                Driver = webdriver.Chrome(chrome_options = options)
            elif browser == 'Firefox':
                profile = webdriver.FirefoxProfile()
                profile.set_preference('browser.download.dir', 'C:\\Users\GAOBO\Desktop\download_test')
                profile.set_preference('browser.download.folderList', 2)
                profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
                # 启动Firefox浏览器，启动参数配置默认下载路径
                Driver = webdriver.Firefox(firefox_profile = profile)
            else:
                print('不支持该浏览器')
            return Driver
        except:
            print('打开浏览器失败')
            return None

    def get_url(self, url):
        '''
        输入url方法
        :param url: url地址
        :return:
        '''
        if self.Driver != None:
            if 'http://' in url:  # url必须以http://开头
                self.Driver.get(url)  # 输入url地址
            else:
                print('url不合法')
        else:
            print('case执行失败')

    def handle_windows(self, *args):
        '''
        封装浏览器常见操作
        :param args: 代表可以传入任意个参数
        :return:
        '''
        valuse = len(args)  # 通过args的长度，判断传入参数的数量
        if valuse == 1:
            handle = args[0]
            if handle == 'max':
                self.Driver.maximize_window()  # 最大化窗口
            elif handle == 'min':
                self.Driver.minimize_window()  # 最小化窗口
            elif handle == 'back':
                self.Driver.back()  # 后退
            elif handle == 'forward':
                self.Driver.forward()  # 前进
            elif handle == 'resfresh':
                self.Driver.refresh()  # 刷新
        elif valuse == 2:
            self.Driver.set_window_size(args[0], args[1])  # 调整窗口尺寸
        else:
            print('你的输入有误')

    def assert_title(self, title_name=None):
        '''
        判断参数是否为空，不为空则进行与当前页面title判断
        :param title_name:
        :return: 判断结果
        '''
        if title_name != None:
            get_title = EC.title_contains(title_name)  # 判断当前页面的title是否与所传参数一致
            return get_title(self.Driver)  # 返回判断结果，bool值

    def open_url_is_true(self, url, title_name = None):
        '''
        通过title判断页面是否正确
        '''
        self.get_url(url)  # 调用get_url方法
        result = self.assert_title(title_name)  # 调用assert_title方法
        return result

    def close_driver(self):
        self.Driver.close()

    def switch_windows(self, title_name = None):
        '''
        切换页面方法
        :param title_name:
        :return:
        '''
        handle_list = self.Driver.window_handles  # 获取所有句柄
        current_handle = self.Driver.current_window_handle  # 获取当前句柄

        for i in handle_list:
            if i != current_handle:
                time.sleep(1)
                self.Driver.switch_to(i)
                if self.assert_title(title_name) == True:  # 调用assert_title方法，判断页面是否正确，正确则不再切换
                    break

    def element_isdisplayed(self, elememt):
        '''
        判断元素是否可见，可见返回elememt，不可见返回False
        :param elememt: 定位到的元素对象
        :return:
        '''
        flag = elememt.is_displayed()
        if flag == True:
            return elememt
        else:
            return False

    def get_element(self, info):
        '''
        获取定位元素
        :param info: 配置文件内元素的key
        :return: 定位到的元素
        '''
        element = None
        by, value = self.get_local_element(info)
        try:
            if by == 'id':
                element = self.Driver.find_element_by_id(value)
            elif by == 'name':
                element = self.Driver.find_element_by_name(value)
            elif by == 'css':
                element = self.Driver.find_element_by_css_selector(value)
            elif by == 'class':
                element = self.Driver.find_element_by_class_name(value)
            elif by == 'xpath':
                element = self.Driver.find_element_by_xpath(value)
        except:
            print('定位方式:',by, '定位值:',value, '---定位失败，没有找到该元素')
        return self.element_isdisplayed(element)

    def get_elements(self, info):
        '''
        获取元素elements
        :param info: 配置文件内元素的key
        :return elements: 定位到的元素
        '''
        elements = None
        elements_list = []
        by, value = self.get_local_element(info)
        if by == 'id':
            elements = self.Driver.find_elements_by_id(value)
        elif by == 'name':
            elements = self.Driver.find_elements_by_name(value)
        elif by == 'css':
            elements = self.Driver.find_elements_by_css_selector(value)
        elif by == 'class':
            elements = self.Driver.find_elements_by_class_name(value)
        elif by == 'xpath':
            elements = self.Driver.find_elements_by_xpath(value)

        for element in elements:
            if self.element_isdisplayed(element) == False:
                continue
            else:
                elements_list.append(element)
        return elements_list

    def get_list_element(self, info, index):
        '''
        list定位，通过elements方法，获取页面所有相关元素，通过index选择所需元素
        :param info: 配置文件元素对应的key
        :param index: 所需元素的下标
        :return: 所找到的元素
        '''
        elements = self.get_elements(info)
        if len(elements) <= int(index):
            return None
        else:
            elements = elements[index]
            return elements

    def scroll_get_element(self, list_info):
        T = True
        list_element = self.get_elements(list_info)
        js = 'document.documentElement.scrollTop=100000'
        while T:
            for element in list_element:
                title_name = element.find_element_by_tag_name('p').text
                if title_name in 'Mysql系列-事务':
                    element.click()
                    T = False
                    break
            self.Driver.execute_script(js)
            time.sleep(3)

    def scroll_element(self, info):
        '''
        滑动查找元素
        :param info:
        :return:
        '''
        js = 'document.documentElement.scrollTop=1000'
        T = True
        while T:
            try:
                self.get_element(info)
                T = False
            except:
                self.Driver.execute_script(js)



    def send_value(self, info, key):
        '''
        输入事件
        :param info: 配置文件内元素对应的key
        :param key: 想在元素内输入的值
        :return:
        '''
        element = self.get_element(info)
        if element == False:
            print('定位失败，定位元素未展示')
        else:
            if element != None:
                element.send_keys(key)
            else:
                print('输入失败，定位元素未找到')

    def click_element(self, info):
        '''
        点击事件
        :param info: 配置文件内元素对应的key
        :return:
        '''
        element = self.get_element(info)
        if element == False:
            print('定位失败，定位元素未展示')
        else:
            if element != None:
                element.click()
            else:
                print('点击失败，定位元素未找到')

    def check_box_isselected(self, info, check = None):
        '''
        判断勾选框是否选中，并进行操作
        :param info: 配置文件内元素对应的key
        :param check: 是否需要勾选，check代表需要勾选，None代表不勾选
        :return:
        '''
        element = self.get_element(info)
        if element == False:
            print('定位失败，定位元素未展示')
        else:
            flag = element.is_selected()
            if flag == True:
                if check == 'check':
                    pass
                else:
                    self.click_element(info)
            else:
                if check == 'check':
                    self.click_element(info)

    def get_selected(self, info, method, value, index = None):
        '''
        通过select方法，获取下拉框对象，然后选中所需的选项
        :param info: 配置文件内元素对应的key
        :param method: 选中选项的方式
        :param value: 所选选项对应的值
        :param index: 采用elements定位时，元素的index
        :return:
        '''
        selectd_element = None
        if index == None:
            selected_element = self.get_element(info)
        else:
            selectd_element = self.get_list_element(info, index)

        if method == 'index':
            Select(selectd_element).select_by_index(value)
        elif method == 'value':
            Select(selectd_element).select_by_value(value)
        elif method == 'text':
            Select(selectd_element).select_by_visible_text(value)

    def upload_file(self, file_name):
        '''
        非input类型上传文件(建议上传文件均用这个方法)
        :param file_name: 文件路径
        :return:
        '''
        pykey = PyKeyboard()
        pykey.tap_key(pykey.shift_l_key)  # 点击shift，切换输入法
        pykey.type_string('C:\\Users\\GAOBO\\Desktop\\fifteen.png')  # 输入文件所在的路径
        time.sleep(2)
        pykey.tap_key(pykey.enter_key)  # 键盘事件，点击enter键

    def download_file(self, info):
        '''
        下载文件
        :param info: 配置文件内元素对应的key
        :return:
        '''
        self.click_element(info)

    def get_local_element(self, info):
        '''
        读取配置文件，处理配置文件的内容
        :param info: 配置文件内元素对应的key
        :return:
        '''
        data = readini.get_value(info)
        data_info = data.split(',')
        # username_by = data_info[0]
        # username_local = data_info[1]
        # return self.get_element(username_by, username_local)
        return data_info

    def js_execute_calendar(self, info):
        local = self.get_local_element(info)
        by = local[0]
        value = local[1]
        if by == 'id':
            by_key = 'getElementById'
            js = "documenet.{0}('{1}').removeAttrubute('readonly')".format(by_key, value)
        elif by == 'class':
            by_key = 'getElementsByClassName'
            js = "documenet.{0}('{1}')[1].removeAttrubute('readonly')".format(by_key, value)
        self.Driver.execute_script(js)


    def calendar(self, info, value):
        element = self.get_element(info)
        try:
           element.get_attribute('readonly')
           self.js_execute_calendar(info)
        except:
            print('非只读属性')
        element.clear()
        self.send_value(info, value)

    def moveto_element_mouse(self, info):
        '''
        移动鼠标到某个元素上
        :param info: 配置文件内元素对应的key
        :return:
        '''
        element = self.get_element(info)
        ActionChains(self.Driver).move_to_element(elment).perform()

    def refresh_f5(self):
        '''
        强制刷新，会清空cookie
        :return:
        '''
        actionchains = ActionChains(self.Driver)
        actionchains.key_down(Keys.CONTROL).send_keys(Keys.F5)
        actionchains.key_up(Keys.CONTROL)
        actionchains.perform()

    def switch_iframe(self, info = None):
        '''
        切换iframe
        :param info: 配置文件内元素对应的key
        :return:
        '''
        if info != None:
            iframe_element = self.get_element(info)
            self.Driver.switch_to.frame(iframe_element)
        else:
            self.Driver.switch_to.default_content()

    def switch_alert(self, info, value = None):
        '''
        系统级弹窗处理
        :param info: 需要进行的操作，确认或取消
        :param value: 弹窗可输入时的输入值
        :return:
        '''
        windows_alert = self.Driver.switch_to.alert
        if info == 'accept':
            if value == None:
                pass
            else:
                windows_alert.send_keys(value)
            windows_alert.accept()
        else:
            windows_alert.dismiss()

    def get_cookie(self):
        '''
        获取cookie
        :return:
        '''
        cookie = self.Driver.get_cookies() # 获取cookie方法，get_cookies()
        handle_json.writh_data(cookie)

    def set_cookie(self):
        '''
        植入cookie
        :return:
        '''
        cookie = handle_json.get_data()
        self.Driver.delete_all_cookies()
        time.sleep(1)
        self.Driver.add_cookie(cookie)
        time.sleep(2)

    def save_png(self):
        now_time = time.strftime('%Y%m%d.%H.%M.%S')
        self.Driver.get_screenshot_as_file('%s.png' %now_time)

if __name__ == '__main__':
    selenium_driver = SeleniumDriver('Chrome')
    selenium_driver.handle_windows('max')
    selenium_driver.get_url('http://www.imooc.com/')
    # selenium_driver.handle_windows('refresh')
    # selenium_driver.check_box_isselected('id', 'auto-signin', 'check')
    time.sleep(2)
    selenium_driver.click_element('login')
    time.sleep(2)
    selenium_driver.send_value('username', '15007534131')
    time.sleep(2)


