import unittest
from check_palindrome import check_palindrome

class test_check_palindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(check_palindrome("DAD"), True)
        self.assertEqual(check_palindrome("Dad"), False)
        self.assertEqual(check_palindrome("ABCDCBA"), True)
        self.assertEqual(check_palindrome("ABCDcba"), False)
        self.assertEqual(check_palindrome(1881), False)
        self.assertEqual(check_palindrome(True), False)
        self.assertEqual(check_palindrome([]), False)