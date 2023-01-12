import unittest
from Test_Cases import my_Test
from testcal import my_Test
def my_suite():
    suite=unittest.TestSuite()
    result=unittest.TestResult()
    suite.addTests(unittest.makeSuite(my_Test))
    suite.addTests(unittest.makeSuite(my_Test))
    runner=unittest.TextTestRunner(verbosity=2)
    print(runner.run(suite))
my_suite()