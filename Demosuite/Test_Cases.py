import CalcMode as cm
import unittest
print(cm.name)
print(cm.version)
class my_Test(unittest.TestCase):
    def test_add(self):
        result=cm.add_int(10,30)
        self.assertEqual(result,40)
    def test_mul(self):
        result=cm.mul(2,6)
        self.assertEqual(result,12)
    def test_div(self):
        result=cm.div(2,4)
        self.assertNotEqual(result,2)

if '__name__' == '__main__':
    unittest.main()