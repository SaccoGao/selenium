# coding=utf-8

from UI_AutomatedTesting_Actual.base.find_element import FindElement

class ResgisterPage():
    def __init__(self, driver):
        self.fd = FindElement(driver)

    def get_email_element(self):
        '''
        查找email_element
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'useremail')


    def get_username_element(self):
        '''
        查找username_element
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'username')

    def get_password_element(self):
        '''
        查找password_element
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'password')

    def get_codetext_element(self):
        '''
        查找codetext_element
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'codetext')

    def get_button_element(self):
        '''
        查找注册按钮button_element
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'register')

    def get_email_error_elemenet(self):
        '''
        查找邮箱错误email_error_elemenet
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'useremail_error')

    def get_username_error_elemenet(self):
        '''
        查找用户名错误username_error_elemenet
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'username_error')

    def get_password_error_elemenet(self):
        '''
        查找密码错误password_error_elemenet
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'password_error')

    def get_code_error_elemenet(self):
        '''
        查找验证码错误code_error_elemenet
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'codetext_error')

    def get_code_text_image(self):
        '''
        获取验证码元素
        :return:
        '''
        return self.fd.get_element('RegisterElement', 'codetext_image')