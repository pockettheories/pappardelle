import unittest, sys
from pappardelle import string_or_default

sys.path.append('pappardelle')  # Include the subdir in the PythonPath

class TestStringHelpers(unittest.TestCase):
    """Test cases for string_helpers module."""

    def test_string_or_default_with_valid_primary(self):
        """Test string_or_default when primary value is valid."""
        result = string_or_default("hello", "default")
        self.assertEqual(result, "hello")

    def test_string_or_default_with_whitespace_primary(self):
        """Test string_or_default when primary value has leading/trailing whitespace."""
        result = string_or_default("  hello  ", "default")
        self.assertEqual(result, "  hello  ")

    def test_string_or_default_with_empty_string_primary(self):
        """Test string_or_default when primary value is empty string."""
        result = string_or_default("", "default")
        self.assertEqual(result, "default")

    def test_string_or_default_with_whitespace_only_primary(self):
        """Test string_or_default when primary value is only whitespace."""
        result = string_or_default("   ", "default")
        self.assertEqual(result, "default")

    def test_string_or_default_with_tab_whitespace_primary(self):
        """Test string_or_default when primary value is only tab characters."""
        result = string_or_default("\t", "default")
        self.assertEqual(result, "default")

    def test_string_or_default_with_newline_whitespace_primary(self):
        """Test string_or_default when primary value is only newline characters."""
        result = string_or_default("\n", "default")
        self.assertEqual(result, "default")

    def test_string_or_default_with_mixed_whitespace_primary(self):
        """Test string_or_default when primary value is mixed whitespace."""
        result = string_or_default(" \t\n ", "default")
        self.assertEqual(result, "default")

    def test_string_or_default_with_none_primary(self):
        """Test string_or_default when primary value is None."""
        result = string_or_default(None, "default")
        self.assertEqual(result, "default")

    def test_string_or_default_with_empty_secondary(self):
        """Test string_or_default when secondary value is empty string."""
        result = string_or_default("a", "")
        self.assertEqual(result, "a")

    def test_string_or_default_with_none_secondary(self):
        """Test string_or_default when secondary value is None."""
        result = string_or_default("", None)
        self.assertEqual(result, None)

    def test_string_or_default_with_both_empty(self):
        """Test string_or_default when both values are empty."""
        result = string_or_default("", "")
        self.assertEqual(result, "")

    def test_string_or_default_with_both_none(self):
        """Test string_or_default when both values are None."""
        result = string_or_default(None, None)
        self.assertEqual(result, None)

    def test_string_or_default_with_complex_strings(self):
        """Test string_or_default with complex string values."""
        result = string_or_default("Hello, World!", "Fallback")
        self.assertEqual(result, "Hello, World!")

    def test_string_or_default_with_special_characters(self):
        """Test string_or_default with special characters."""
        result = string_or_default("!@#$%^&*()", "default")
        self.assertEqual(result, "!@#$%^&*()")

    def test_string_or_default_with_numbers_as_strings(self):
        """Test string_or_default with numeric strings."""
        result = string_or_default("12345", "default")
        self.assertEqual(result, "12345")

    def test_string_or_default_with_zero_as_string(self):
        """Test string_or_default with zero as string."""
        result = string_or_default("0", "default")
        self.assertEqual(result, "0")

    def test_string_or_default_with_false_as_string(self):
        """Test string_or_default with 'False' as string."""
        result = string_or_default("False", "default")
        self.assertEqual(result, "False")
