#!/usr/bin/python3
"""

Unittest for max_integer([..])

"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list_len(self):
        # Test when len(list) == 0
        self.assertFalse(max_integer([]))

    def test_list_values(self):
        # Test if value errors are raised
        self.assertRaises(TypeError, max_integer, [1, 2, "Hello"])

    def test_output(self):
        # Test when values meet required parameters
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        
    def test_list_items(self):
        # Test if type errors are raised
        self.assertTrue(max_integer([1, 2, 3, False]), TypeError)
