import HtmlTestRunner
import unittest
import os 
import sys
path = os.path.abspath(os.getcwd())
finalpath =  os.path.join(path, "pystandalonehtml")
sys.path.insert(0,finalpath)

print("The pystandalone path is ",finalpath)

finalpath2 =  os.path.join(path, "tests")
sys.path.insert(0,finalpath2)

print("The test path is ",finalpath2)

from test_cli import test_cli

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_cli_code(self):
        test_cli()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))