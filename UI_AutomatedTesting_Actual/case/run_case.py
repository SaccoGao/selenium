import os.path
import unittest

class  RunCase(unittest.TestCase):
    def test_case_01(self):
        case_path = os.getcwd()
        suite = unittest.defaultTestLoader.discover(case_path, 'unittest_case*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()

# case_path = os.path.join(os.getcwd(),'case')
# print(case_path)