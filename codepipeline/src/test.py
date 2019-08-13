# code/foo/api testing functions/asserts go here
#

import unittest
from lambda_function import functions
from lambda_function import lambda_handler


class TestMyFoo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(functions['/'],'root (/)')

    def test_2(self):
        self.assertEqual(functions['/test'],'/test')

    def test_3(self):
        self.assertEqual('foo'.upper(),'FOO')


if __name__ == '__main__':
  unittest.main()
