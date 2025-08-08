import unittest, sys
from pappardelle import string_or_default, is_null_or_whitespace, str_ignorecase_startswith

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

    def test_string_or_default_with_three_params(self):
        """Test string_or_default with None twice and a non-empty string."""
        result = string_or_default(None, None, "nonagon")
        self.assertEqual(result, "nonagon")

    def test_is_null_or_whitespace_with_null(self):
        """Test is_null_or_whitespace with a null"""
        result = is_null_or_whitespace(None)
        self.assertEqual(result, True)

    def test_is_null_or_whitespace_with_empty(self):
        """Test is_null_or_whitespace with an empty string"""
        result = is_null_or_whitespace('')
        self.assertEqual(result, True)

    def test_str_ignorecase_startswith_diff_capitalization(self):
        """Test str_ignorecase_startswith with the same string but with different capitalization"""
        result = str_ignorecase_startswith('Nita', 'nita')
        self.assertEqual(result, True)

    def test_str_ignorecase_startswith_diff_str(self):
        """Test str_ignorecase_startswith with different strings"""
        result = str_ignorecase_startswith('Jagravi', 'urmi')
        self.assertEqual(result, False)

    def test_str_ignorecase_startswith_same_str(self):
        """Test str_ignorecase_startswith with the same string"""
        result = str_ignorecase_startswith('Narsing', 'Narsing')
        self.assertEqual(result, True)

    # TODO: More _startswith use cases where str1 is a substring of str2, and str2 is a substring of str1

    def test_is_null_or_whitespace_with_whitespace(self):
        """Test is_null_or_whitespace with whitespace strings"""
        result = is_null_or_whitespace(' ')
        self.assertEqual(result, True)
        result = is_null_or_whitespace('  ')
        self.assertEqual(result, True)
        result = is_null_or_whitespace('\n')
        self.assertEqual(result, True)
        result = is_null_or_whitespace('\t')
        self.assertEqual(result, True)
        result = is_null_or_whitespace(' \n')
        self.assertEqual(result, True)
        result = is_null_or_whitespace(' \t')
        self.assertEqual(result, True)
        result = is_null_or_whitespace('\n ')
        self.assertEqual(result, True)
        result = is_null_or_whitespace('\t ')
        self.assertEqual(result, True)

    def test_is_null_or_whitespace_with_non_empty(self):
        """Test is_null_or_whitespace with non-empty strings"""
        result = is_null_or_whitespace('a')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('1')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('False')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('false')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('null')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('None')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('NULL')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('0')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('A')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('a ')
        self.assertEqual(result, False)
        result = is_null_or_whitespace(' a')
        self.assertEqual(result, False)
        result = is_null_or_whitespace(' a ')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('\na')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('a\n')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('\ta')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('a\t')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('a \t')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('a \n')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('\n a')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('\t a')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('^')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('.')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('_')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('+')
        self.assertEqual(result, False)
        result = is_null_or_whitespace('-')
        self.assertEqual(result, False)