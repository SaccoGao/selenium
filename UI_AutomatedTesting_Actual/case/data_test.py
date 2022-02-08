# coding = UTF-8
import ddt
import unittest

@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @ddt.data(['1','2'])
    @ddt.unpack
    def test_add(self, a, b):
        print(a+b)


if __name__ == '__main__':
    unittest.main()