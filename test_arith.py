import unittest
from fonction_arith import *

class testArith(unittest.TestCase):
    def test_arith(self):
        self.assertEqual(isArith([2,4]))
        self.assertEqual(isArith([1,2,3]),True)
        self.assertEqual(isArith([]),False)
        self.assertEqual(isArith(["Miam","Manger"]),False)


if __name__ == '__main__':
    unittest.main()
