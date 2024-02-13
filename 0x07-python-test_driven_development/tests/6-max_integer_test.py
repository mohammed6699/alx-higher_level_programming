#!/usr/bin/python3

"""Max_integer Module"""

import unittest
max_integer = __import__("6-max_integer_test").max_integer

class MaxInteger(unittest.TestCase):
    def test_no_arg(self):
        self.assertEqual(max_integer(), None)

    def empty_list(self):
        self.assertEqual(max_integer([]), None)

    def one_number(self):
        self.assertEqual(max_integer([100]), 100)

    def two_numbers(self):
        self.assertEqual(max_integer([1, 2]), 2)
    
    def same_arg(self):
        self.assertEqual(max_integer[4, 4, 4, 4, 4]), 4)

    def list_even_numbers(self):
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def list_odd_numbers(self):
        self.assertEqual(max_integer([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]), 19)

    def list_of_positive_numbers(self):
        self.assertEqual(max_integer([100, 150, 200, 250, 300, 400, 800]), 800)

    def list_of_positive_floats(self):
        self.assertEqual(max_integer([100.5, 100.8, 200.5, 200.8, 300.6, 300.7]), 300.7)

    def unordered_positive_float(self):
        self.assertEqual(max_integer[300.7, 100.5, 200.8, 200.6, 100.8, 300.6]), 300.7)

    def unordered_positive_int(self):
        self.assertEqual(max_integer([250, 800, 300, 150, 400, 100, 200]), 800)

    def list_of_negative_int(self):
        self.assertEqual(max_integer([-100, -150, -200, -250, -300, -400, -800]), -100)

    def list_of_negative_float(self):
        self.assertEqual(max_integer([-100.5, -100.8, -200.5, -200.8, -300.6, -300.7]), -100.5)

    def unordered_negative_int(self):
        self.assertEqual(max_integer([-150, -800, -100, -200, -300, -250, -400]), -100)

    def unordered_negative_float(self):
        self.assertEqual(max_integer([-300.6, -200.5, -100.5, -100.8, -300.7, -200.8]), -100.5)

    def list_of_positive_and_negative_int(self):
        self.assertEqual(max_integer([2000, -1000, 0, 8000, -5000, -7000, 3500]), 8000)

    def list_of_positive_and_negative_floats(self):
        self.assertEqual(max_integer([-800.5, 9000.7, -10000.98, 1000.97, 7500.45, 12000]), 12000)

    def string_arg(self):
        self.assertEqual(max_integer(["nan"]))

    def mixed_str_int(self):
        self.assertRaises(TypeError)
        max_integer([99, nan])

    def test_None(self):
        self.assertRaises(TypeError)
        max_integer(None)

    def test_dic(self):
        self.assertRaises(TypeError)
        max_integer([{20:25, 100:105}, {a: b, c: d}])

if __name__ = '__main__':
    unittest.main()
