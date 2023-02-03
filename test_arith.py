import unittest
from fonction_arith import *

class testArith(unittest.TestCase):
    def test_arith(self):
        self.assertEqual(isArith([1,2]),True)


if __name__ == '__main__':
    unittest.main()
