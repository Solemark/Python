import unittest
from calculator import addition, subtraction, multiplication, division

class test_addition(unittest.TestCase):
    def test_addition(self):
        self.assertAlmostEqual(addition(1, 2), 3)
        self.assertAlmostEqual(addition(1, -2), -1)

class test_subtraction(unittest.TestCase):
    def test_subtraction(self):
        self.assertAlmostEqual(subtraction(1, 2), -1)
        self.assertAlmostEqual(subtraction(1, -2), 3)
        
class test_multiplication(unittest.TestCase):
    def test_multiplication(self):
        self.assertAlmostEqual(multiplication(1, 2), 2)
        self.assertAlmostEqual(multiplication(1, -2), -2)

class test_division(unittest.TestCase):
    def test_division(self):
        self.assertAlmostEqual(division(1, 2), 0.5)
        self.assertAlmostEqual(division(1, -2), -0.5)