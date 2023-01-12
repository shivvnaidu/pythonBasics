import unittest
def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
def pow(a,b):
    return a**b
class my_Test(unittest.TestCase):
    def test1(self):
        a=10
        b=20
        r=sum(a,b)
        self.assertEqual(r,30)
    def test2(self):
        a=29
        b=30
        r=mul(a,b)
        self.assertNotEqual(r,20)
    def test3(self):
        a=20
        b=10
        r=pow(a,b)
        self.assertNotEqual(r,10)
    def test4(self):
        a=10
        b=10
        r=sum(a,b)
        self.assertEqual(r,20)
    def test5(self):
        a=19
        b=20
        r=sum(a,b)
        self.assertNotEqual(r,10)






