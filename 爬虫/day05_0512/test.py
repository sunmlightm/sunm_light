import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        print('setUp...')
    def testTest(self):
        print('test')
    def tearDown(self):
        print('tearDown()...')

if __name__ == '__main__':
    unittest.main()