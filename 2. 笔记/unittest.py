import unittest
import ddt
import xlrd

'''
启用unittest框架
在创建类的时候继承unittest.TestCase
class FirstCase01(unittest.TestCase): 
实例见UI_AutomatedTesting_Actual -> case -> unittest_case_01模块
'''

# 全局前置条件，在所有用例执行前执行
@classmethod
def setUpClass(cls):
    a = '执行内容'

# 全局后置条件，在所有用例执行完之后执行
@classmethod
def tearDownClass(cls):
    a = '执行内容'

# 前置条件，在每条用例执行前执行
def setUp(self) -> None:
    a = '执行内容'

# 后置条件，在每条用例执行后执行
def tearDown(self) -> None:
    a = '执行内容'

'''
执行用例的方法名以test开头
1. 执行全部用例写法如下：普通模式
if __name__ == '__main__':
    unittest.main()
unittest会自动识别test开头的方法，并作为用例执行

2. 执行部分用例的方法：容器模式
2.1 addTest
if __name__ == '__main__':
    suite = unittest.TestSuite() # 创建容器suite
    suite.addTest(类名('方法名')) # 往suite内加入用例
    unittest.TextTestRunner().run(suite) # 执行容器内的用例
    
2.2 addTests
if __name__ == '__main__':
    suite = unittest.TestSuite() # 创建容器suite
    suite.addTests(map,(类名, ['方法名1', '方法名2'])) # 往suite内加入用例
    unittest.TextTestRunner().run(suite) # 执行容器内的用例
'''


'''
控制执行顺序及跳过case
1. 普通模式下，case的执行顺序：与case的方法名有关而与方法的摆放顺序无关
2. 容器模式下，与case的添加顺序有关，suite.addTest(类名('方法名'))
3. 跳过执行，在case前添加装饰器@unittest.skip，如：
@unittest.skip
def test_case01(self):
    a = '执行内容'
'''

'''
批量运行不同py文件内的case，实例见UI_AutomatedTesting_Actual -> case -> run_case模块
创建一个新的py文件，作为入口文件
def test_case_01(self):
    case_path = os.getcwd() # 获取当前文件的工作目录
    
    # discover()方法，参数1-当前文件的工作目录，参数2-要运行的py文件的模糊文件名
    suite = unittest.defaultTestLoader.discover(case_path, 'unittest_case*.py')
    
    # 运行选定的文件
    unittest.TextTestRunner().run(suite)

额外内容：os.path
os.getcwd() - 获取当前文件的工作目录
os.path.join('11','22') - 以路径的形式拼接字符串，如：11\22
'''

'''
assert方法
assertFalse(方法名, '执行正确后提示') # 判断方法返回是否为False
'''

'''
测试报告 - HTMLTestRunner
f = open('测试报告路径及文件名', 'wb') # 定义存放测试报告的路径及测试报告文件名
runner = HTMLTestRunner.HTMLTestRunner(stream = f, title, description) # 文件文件路径，测试报告名称，测试报告描述
runner.run(suite) # 执行容器内的用例
f.close() # 关闭文件
'''

'''
捕捉case执行过程中的错误
可以在teardown下进行捕捉：
for method_name, error in self._outcome.errors: # self._outcome.errors，返回的是case执行过程中的错误列表，list格式
    if error: # 如果error不为空
        self.driver.get_screenshot_as_file(file_path) # 执行截图操作，记录错误截图
        
额外知识：
case_name = self._testMethodName # 可以获取本次运行运行的case名称
'''









