import unittest
from fonction_geom import *

class testGeom(unittest.TestCase):
    def test_geom(self):
        self.assertEqual(isGeom([]),False)
        self.assertEqual(isGeom([3]),False)
        self.assertEqual(isGeom([2,4,8]),True)
        self.assertEqual(isGeom([4,8,0]),False)
        self.assertEqual(isGeom([6,12,24,48]),True)


if __name__ == '__main__':
    unittest.main()
