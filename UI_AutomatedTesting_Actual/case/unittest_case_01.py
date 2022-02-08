import unittest

class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有case执行前的前置条件')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行后的后置条件')

    def setUp(self) -> None:
        print('这是一个前置条件')

    def tearDown(self) -> None:
        print('这是一个后置条件')

    def test_case01(self):
        print('这是case01')

    def test_case02(self):
        print('这是case02')

    def test_case03(self):
        print('这是case03')

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase01('test_case02'))
    # unittest.TextTestRunner().run(suite)
