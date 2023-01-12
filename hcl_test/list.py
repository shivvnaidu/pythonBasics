import unittest
def listmax(l):
    for each in l:
        return(max(l))
class My_Test(unittest.TestCase):
    def test(self):
        l=[86,48,90,45,67,99]
        r=listmax(l)
        self.assertEqual(r,99)
