import unittest
from fonction_arith import *

class testArith(unittest.TestCase):
    def test_arith(self):
        self.assertEqual(isArith([4,12,43]),False)
        self.assertEqual(isArith([1]),False)
        self.assertEqual(isArith([2,4,6]),True)
        self.assertEqual(isArith([1,2,3]),True)
        self.assertEqual(isArith([]),False)


if __name__ == '__main__':
    unittest.main()
