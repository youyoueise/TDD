import unittest
from fonction_gen_geom import *

class testGenGeom(unittest.TestCase):
    def test_gen_geom(self):
        self.assertEqual(genGeom([2,4,8],3),[True,[8,10,12]])
        self.assertEqual(genGeom([1,2,5],4),False)
        self.assertEqual(genGeom([2],6),False)

if __name__ == '__main__':
    unittest.main()
