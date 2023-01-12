import unittest
def yr_c(n):
    if n in [1,3,5,7,8,10,12]:
        return 31
    elif n in [4,6,9,11]:
        return 30
    else:
        return 28
def login(un,ps):
    if (un == "hcluser" and ps == "12345"):
        return 1
    else:
        return 0
class my_Test(unittest.TestCase):
    def test(self):
        n=2
        result=yr_c(n)
        self.assertEqual(result,28)
    def test1(self):
        un="hcluser"
        ps="12345"
        result= login(un,ps)
        self.assertEqual(result,1)


