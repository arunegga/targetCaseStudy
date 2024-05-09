import unittest
from src.common.validations import is_integer

class TestIsIntegerFunction(unittest.TestCase):

    def test_integer_value(self):
        self.assertTrue(is_integer(5))

    def test_float_value(self):
        self.assertFalse(is_integer(5.0))

    def test_string_value(self):
        self.assertFalse(is_integer("5"))

    def test_boolean_value(self):
        self.assertFalse(is_integer(True))

    def test_none_value(self):
        self.assertFalse(is_integer(None))

    def test_list_value(self):
        self.assertFalse(is_integer([5]))

if __name__ == '__main__':
    unittest.main()
