# coding=utf-8
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "/Python_study")))

from UI_AutomatedTesting_Actual.business.resgister_business import ResgisterBusiness
from UI_AutomatedTesting_Actual.util.get_code import GetCode
from UI_AutomatedTesting_Actual.log.user_log import UserLog
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time

user = UserLog()
class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log = user.get_log()
        cls.now_time = time.strftime('%Y%m%d%H%M%S')
        cls.file_name = os.path.join(os.getcwd(),\
                            '\\Python_study\\UI_AutomatedTesting_Actual\\image_code\\code_image_{0}.png'\
                            .format(cls.now_time))

    @classmethod
    def tearDownClass(cls):
        user.close_handel()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.5itest.cn/register')
        self.login = ResgisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        a = self._outcome.errors
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName # 获取运行的case名称
                # now_time = time.strftime('%Y%m%d%H%M%S')
                file_path = os.path.join(os.getcwd(),\
                            '\\Python_study\\UI_AutomatedTesting_Actual\\image_error\\{0}-{1}.png'\
                            .format(case_name,self.now_time))
                self.driver.get_screenshot_as_file(file_path)
        self.driver.close()


    def test_login_useremail_error(self):
        '''
        验证注册时，邮箱错误
        :return:
        '''
        tsetname = 'test_login_useremail_error'
        email_error = self.login.login_email_error('Sacco', 'Sacco', 'Becausezzz000', self.file_name)
        self.assertFalse(email_error, 'case:{0}执行成功'.format(tsetname))

    def test_login_username_error(self):
        '''
        验证注册时，用户名错误
        :return:
        '''
        tsetname = 'test_login_username_error'
        username_error = self.login.login_name_error('Sacco@163.com', 'Sa', 'Becausezzz000', self.file_name)
        self.assertFalse(username_error, 'case:{0}执行成功'.format(tsetname))

    def test_login_password_error(self):
        '''
        验证注册时，密码错误
        :return:
        '''
        tsetname = 'test_login_password_error'
        password_error = self.login.login_passworde_error('Sacco@163.com', 'Sacco', '1122', self.file_name)
        self.assertFalse(password_error, 'case:{0}执行成功'.format(tsetname))

    def test_login_codetext_error(self):
        '''
        验证注册时，验证码错误
        :return:
        '''
        tsetname = 'test_login_codetext_error'
        codetext_error = self.login.login_codetext_error('Sacco@163.com', 'Sacco', 'Becausezzz000', '11111')
        self.assertFalse(codetext_error, 'case:{0}执行成功'.format(tsetname))

    def test_login_succes(self):
        '''
        登录成功
        :return:
        '''
        tsetname = 'test_login_succes'
        success = self.login.user_base('Sacco@163.com', 'Sacco', 'Becausezzz000', self.file_name)
        self.assertTrue(success, 'case:{0}执行成功'.format(tsetname))

'''
def main():
    first = FirstCase()
    first.test_login_useremail_error()
    first.test_login_username_error()
    # first.test_login_password_error()
    # first.test_login_codetext_error()
    # first.test_login_succes()
'''

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(map(FirstCase, ['test_login_useremail_error','test_login_username_error']))
    # unittest.TextTestRunner().run(suite)
    now_time = time.strftime('%Y%m%d%H%M%S')
    file_path = os.path.join(os.getcwd(),
    '\\Python_study\\UI_AutomatedTesting_Actual\\resport\\测试报告-{0}.html'.format(now_time))
    f = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = f, title = '测试报告', description = '{0}自动化测试报告'.format(now_time))
    runner.run(suite)
    f.close()