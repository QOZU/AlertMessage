# test_alertmessage.py
"""
Tests for AlertMessage module.
"""

import unittest
from alertmessage import AlertMessage

class TestAlertMessage(unittest.TestCase):
    """Test cases for AlertMessage class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AlertMessage()
        self.assertIsInstance(instance, AlertMessage)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AlertMessage()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
