# coding=utf-8

from UI_AutomatedTesting_Actual.handle.resgister_handle import ResgisterHandle

class ResgisterBusiness():
    def __init__(self, driver):
        self.resgister_h = ResgisterHandle(driver)

    def regist_function(self, email, username, password, file_name, assertCode, assertText):
        self.user_base(email, username, password, file_name)
        if self.resgister_h.get_user_text(assertCode, assertText) == None:
            # print('邮箱不检验成功')
            return True
        else:
            return False

    def user_base(self, email, name, password, file_name):
        self.resgister_h.send_user_email(email)
        self.resgister_h.send_user_name(name)
        self.resgister_h.send_user_password(password)
        self.resgister_h.send_user_code(file_name)
        self.resgister_h.click_resgister_button()

    def resgister_succes(self):
        '''
        判断是否登录成功
        :return:
        '''
        if self.resgister_h.get_resgister_text() == None:
            return True
        else:
            return False

    def login_email_error(self, email, name, password, file_name):
        '''
        执行邮箱错误的登录操作
        '''
        self.user_base(email, name, password, file_name)
        if self.resgister_h.get_user_text('email', '请输入有效的电子邮件地址') == None:
            print('邮箱不检验成功')
            return True
        else:
            return False

    def login_name_error(self, email, name, password, file_name):
        '''
        执行用户名错误的登录操作
        '''
        self.user_base(email, name, password, file_name)
        if self.resgister_h.get_user_text('username', '字符长度必须大于等于4，一个中文字算2个字符') == None:
            print('用户名不检验成功')
            return True
        else:
            return False

    def login_passworde_error(self, email, name, password, file_name):
        '''
        执行密码错误的登录操作
        '''
        self.user_base(email, name, password, file_name)
        if self.resgister_h.get_user_text('password', '最少需要输入 5 个字符') == None:
            print('密码不检验成功')
            return True
        else:
            return False

    def login_codetext_error(self, email, name, password, file_name):
        '''
        执行验证码错误的登录操作
        '''
        self.user_base(email, name, password, file_name)
        if self.resgister_h.get_user_text('codetext', '验证码错误') == None:
            print('验证码不检验成功')
            return True
        else:
            return False