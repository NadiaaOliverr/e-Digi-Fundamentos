from app.model.category import Category
from app.dao.category_dao import CategoryDao

import unittest

class TestCategoryDatabase(unittest.TestCase):

    def test_should_throw_an_exception_when_add_name_of_category_already_exists(self):
        dao = CategoryDao()
        category_programming = Category('Programming')
        category_already_exists_programming = Category('Programming')
        dao.save(category_programming)

        with self.assertRaises(ValueError):
            dao.save(category_already_exists_programming)

    def test_should_throw_an_exception_when_save_other_type_different_of_category(self):
        dao = CategoryDao()
        type_str = 'Type str'
        
        with self.assertRaises(TypeError):
            dao.save(type_str)

    def test_should_print_the_data_of_category_save(self):
        dao = CategoryDao()
        category_data_science = Category('Data Science')
        
        self.assertEqual(dao.save(category_data_science), category_data_science)

if __name__ == '__main__':
    unittest.main()
