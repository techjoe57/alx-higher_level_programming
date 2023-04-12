#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list_len(self):
        # Test when list is empty
        self.assertFalse(max_integer([]))

    def test_one_item(self):
        # Test if list has only an item
        self.assertAlmostEqual(max_integer([23]), 23)

    def test_list_values(self):
        # Test if value errors are raised
        self.assertRaises(TypeError, max_integer, [1, 2, "Hello"])

    def test_output(self):
        # Test when values meet required parameters
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        
    def test_list_items(self):
        # Test if type errors are raised
        self.assertTrue(max_integer([1, 2, 3, False]), TypeError)

    def test_negative_items(self):
        # Test for maximum if all items are negative
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)

    def test_one_negative(self):
        # Test for maximum if one negative number exists
        self.assertAlmostEqual(max_integer([23, 0, -1]), 23)

    def test_maximum_middle(self):
        # Test for maximum if maximum item is in middle
        self.assertAlmostEqual(max_integer([23, 100, -1]), 100)
