import unittest

from model import Category
from dao import CategoryDao


class TestCategory(unittest.TestCase):

    def test_should_throw_an_exception_when_the_name_category__is_none(self):
        with self.assertRaises(ValueError):
            Category(None)

    def test_should_throw_an_exception_when_the_name_category_is_empty(self):
        with self.assertRaises(ValueError):
            Category('')

    def test_should_throw_an_exception_when_the_name_category_is_empty_full_spaces(self):
        with self.assertRaises(ValueError):
            Category('    ')

if __name__ == '__main__':
    unittest.main()
