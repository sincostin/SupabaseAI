# test_supabase.py
"""
Tests for Supabase module.
"""

import unittest
from supabase import Supabase

class TestSupabase(unittest.TestCase):
    """Test cases for Supabase class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Supabase()
        self.assertIsInstance(instance, Supabase)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Supabase()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
