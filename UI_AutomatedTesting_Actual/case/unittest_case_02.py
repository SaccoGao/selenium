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

    def test_case001(self):
        print('这是case001')

    def test_case002(self):
        print('这是case002')

    def test_case003(self):
        print('这是case003')

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase01('test_case02'))
    # unittest.TextTestRunner().run(suite)
