# coding=utf-8
from UI_AutomatedTesting_Actual.page.resgister_page import ResgisterPage
from UI_AutomatedTesting_Actual.util.get_code import GetCode

class ResgisterHandle():
    def __init__(self, driver):
        self.driver = driver
        self.resgister_p = ResgisterPage(driver)

    def send_user_email(self, email):
        '''
        输入邮箱
        :param email: 邮箱
        :return:
        '''
        self.resgister_p.get_email_element().send_keys(email)

    def send_user_name(self, name):
        '''
        输入用户名
        :param name: 用户名
        :return:
        '''
        self.resgister_p.get_username_element().send_keys(name)

    def send_user_password(self, password):
        '''
        输入密码
        :param password: 密码
        :return:
        '''
        self.resgister_p.get_password_element().send_keys(password)

    def send_user_code(self, file_name):
        '''
        输入验证码
        :param code: 验证码
        :return:
        '''
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(file_name)
        self.resgister_p.get_codetext_element().send_keys(code)

    def click_resgister_button(self):
        '''
        点击注册按钮
        :return:
        '''
        self.resgister_p.get_button_element().click()

    def get_user_text(self, info, user_info):
        '''
        获取错误信息标签的文本信息
        :param info: 标签名称，如email、username等
        :param user_info:
        :return:
        '''
        if info == 'email':
            text = self.resgister_p.get_email_error_elemenet().get_attribute('textContent')
        elif info == 'username':
            text = self.resgister_p.get_username_error_elemenet().get_attribute('textContent')
        elif info == 'password':
            text = self.resgister_p.get_password_error_elemenet().get_attribute('textContent')
        elif info == 'codetext':
            text = self.resgister_p.get_code_error_elemenet().get_attribute('textContent')
        else:
            text = None
        return text

    def get_resgister_text(self):
        return self.resgister_p.get_button_element().text