import unittest
from math import pi
from circles import circle_area

class test_circle(unittest.TestCase):
    #Test areas when radius >= 0
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)

    #Make sure value errors are raised
    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)

    #Raise type error when necessary
    def test_types(self):
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")