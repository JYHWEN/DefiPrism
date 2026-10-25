# test_defiprism.py
"""
Tests for DefiPrism module.
"""

import unittest
from defiprism import DefiPrism

class TestDefiPrism(unittest.TestCase):
    """Test cases for DefiPrism class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DefiPrism()
        self.assertIsInstance(instance, DefiPrism)

    def test_run_method(self):
        """Test the run method."""
        instance = DefiPrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
