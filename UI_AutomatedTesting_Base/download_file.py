from selenium import webdriver

options = webdriver.ChromeOptions()  # Chrome浏览器启动参数配置
prefs = {
    'download.default_directory':'C:\\Users\GAOBO\Desktop\download_test',
    'profile.default_content_settings.popups':0
        }
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options = options)
driver.get('http://www.imooc.com/mobile/app')
driver.find_elements_by_class_name('btn-download')[1].click()
