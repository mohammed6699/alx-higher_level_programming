#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest, TestCase):
    """Unittest for MaxInteger"""
    def test_no_args([..]):
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        self.assertEqual(max_integer[], None)

    def test_one_arg(self):
         self.assertEqual(max_integer[10], 10)

    def test_identical_arg(self):
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
    
    def test_max_start(self):
        self.assertEqual(max_integer([4, 2, 1, 3, 0]), 4)

    def test_ordered_arg(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_ordered_bigger_arg(self):
        self.assertEqual(max_integer([5, 10, 15, 20, 25, 30, 35, 40]), 40)

    def test_unordered_arg(self):
        self.assertEqual(max_integer([2, 5, 4, 8, 1]), 8)

    def test_unordered_bigger_arg(self):
        self.assertEqual(max_integer([35, 8, 60, 45, 12, 10, 5, 7, 90]), 90)

    def test_positive_arg(self):
        self.assertEqual(max_integer([-23, -12, 5, 500, -50, 100]), 500)

    def test_positive_and_negative_arg(self):
        self.assertEqual(max_integer([-2000, -5000, 100, -500, 4508, 5504, -9800, 1000,
                                    -8000, 5680, 7000, -8000, 10000, 10545, 12450, -12500]), 12450)

    def test_negative_arg(self):
        self.assertEqual(max_integer([-2, -5, -8, -12, -90, -15]), -2)

    def test_init_and_float_arg(self):
        self.assertEqual(max_integer([5, 5.5, 999.5, 10540.90, 10.5, 1000.910, 9999, 50.50]), 9999)

    def test_inits_and_float_bigger_arg(self):
        self.assertEqual(max_integer([10000.50, 11542, 10000.50, 15000, 3000.98745601, 17804598, 57485.1235, 
                                    9999999.541, 87954613354, 4875.125698, 475.2315978, 1000000.56978, 569870.987456]),
                                    87954613354)

    def test_floats(self):
        self.assertEqual(max_integer([0.125, 0.5, 0.89, 0.99, 0.875, 0.90, 0.4, 0.1, 0.25]), 0.99)

    def test_floats_bigger_arg(self):
        self.assertEqual(max_integer([0.125, 0.2598, 10.254, 25.789, 0.2697, 30.259, 45.400, 25.265, 0.125,
                                        50.2654, 7.987, 65.20, 90.2365, 5.412, 0.5487, -90.87]), 90.2365)

    def test_numeric_string(self):
        self.assertEqual(max_integer("1987452367"), "9")

    def test_str_list(self):
        self.assertEqual(max_integer("Holberton"), "t")

    def test_list(self):
        self.assertEqual(max_integer([[], [5], [50], [9], [2, 9]]), [50])

    def test_str_list(self):
        self.assertEqual(max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]), ["sic"])

    def test_inf(self):
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]), float('inf'))

    def test_nan(self):
        self.assertEqual(max_integer([99, 100, float('nan')]), 100)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    if __name__ == '__main__':
        unittest.main()

