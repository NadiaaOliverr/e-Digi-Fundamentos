import unittest

from model import Category
from dao import CategoryDao


class TestCategory(unittest.TestCase):

    def test_should_throw_an_exception_when_the_name_category__is_none(self):
        with self.assertRaises(Exception):
            category_none = Category(None)

    def test_should_throw_an_exception_when_the_name_category_is_empty(self):
        with self.assertRaises(Exception):
            category_empty = Category('')

    def test_should_throw_an_exception_when_the_name_category_is_empty_full_spaces(self):
        with self.assertRaises(Exception):
            category_empty_spaces = Category('    ')

    def test_should_throw_an_exception_when_add_name_of_category_already_exists_in_database(self):
        dao = CategoryDao()
        category_programming = Category('Programming')
        category_already_exists_programming = Category('Programming')
        dao.save(category_programming)

        with self.assertRaises(Exception):
            dao.save(category_already_exists_programming)

    def test_should_throw_an_exception_when_save_in_database_other_type_different_of_category(self):
        dao = CategoryDao()
        type_str = 'Type str'
        with self.assertRaises(Exception):
            dao.save(type_str)


if __name__ == '__main__':
    unittest.main()
