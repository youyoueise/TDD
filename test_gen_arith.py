import unittest
from fonction_gen_arith import *

class testGenArith(unittest.TestCase):
    def test_gen_arith(self):
        self.assertEqual(genArith([2,4,6],3),[True,[8,10,12]])
        self.assertEqual(genArith([1,2,4],4),False)
        self.assertEqual(genArith([2],6),False)

if __name__ == '__main__':
    unittest.main()
