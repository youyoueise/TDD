import unittest
from fonction_geom import *

class testArith(unittest.TestCase):
    def test_arith(self):
        self.assertEqual(isGeom([]),False)
        self.assertEqual(isGeom([3]),False)
        self.assertEqual(isGeom([2,4,6]),True)
        self.assertEqual(isArith([4,8,0]),False)
        self.assertEqual(isGeom([6,12,18,24]),True)


if __name__ == '__main__':
    unittest.main()
