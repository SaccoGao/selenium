# coding = utf-8
import unittest
import ddt
from UI_AutomatedTesting_Actual.business.resgister_business import ResgisterBusiness
from UI_AutomatedTesting_Actual.util.get_code import GetCode
from UI_AutomatedTesting_Actual.util.excel_util import ExcelUtil
from selenium import webdriver
import HTMLTestRunner
import os
import time

ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.now_time = time.strftime('%Y%m%d%H%M%S')
        # cls.file_name = os.path.join(os.getcwd(),
        #                              '\\Python_study\\UI_AutomatedTesting_Actual\\image_code\\code_image.png')

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
                case_name = self._testMethodName  # 获取运行的case名称
                file_path = os.path.join(os.getcwd(), \
                                         '\\Python_study\\UI_AutomatedTesting_Actual\\image_error\\{0}-{1}.png' \
                                         .format(case_name, self.now_time))
                self.driver.get_screenshot_as_file(file_path)
        self.driver.close()
    '''
    @ddt.data(
    ['12', 'Sacco', '111111', 'E:/Python_study/UI_AutomatedTesting_Actual/image_code/code_image.png', 'email', '请输入正确的邮箱'],
    ['Sa@163.com', 'Sa', '111111', 'E:/Python_study/UI_AutomatedTesting_Actual/image_code/code_image.png', 'username', '请输入正确的用户名'],
    ['Sa@163.com', 'Sacco', '1122', 'E:/Python_study/UI_AutomatedTesting_Actual/image_code/code_image.png','password', '请输入正确的密码'],
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_regiser_case(self, data):
        email, username, password, file_name, assertCode, assertText = data
        email_error = self.login.regist_function(email, username, password, file_name, assertCode, assertText)
        self.assertFalse(email_error, 'case执行成功')

if __name__ == '__main__':
    now_time = time.strftime('%Y%m%d%H%M%S')
    file_path = os.path.join(os.getcwd(),
    '\\Python_study\\UI_AutomatedTesting_Actual\\resport\\测试报告-{0}.html'.format(now_time))
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='{0}自动化测试报告'.format(now_time))
    runner.run(suite)