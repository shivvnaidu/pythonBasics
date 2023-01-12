import unittest
import calc
class my_Test(unittest.TestCase):
    def test1(self):
        r=calc.add(10,5)
        self.assertEqual(r,15)
    def test2(self):
        r=calc.add(-2,-3)
        self.assertEqual(r,-5)
        self.assertNotEquals(r,-6)

    def test3(self):
        r=calc.sub(5,3)
        self.assertEqual(r, 2)
    def test4(self):
        self.assertEqual(calc.sub(4,2),2)

