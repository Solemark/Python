import unittest
from reverse_array import reverse_array

class test_reverse_array(unittest.TestCase):
    def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])