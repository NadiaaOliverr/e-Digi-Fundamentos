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
    
    def tearDown(self):
        CategoryDao.list_categories = []

    def test_should_throw_an_exception_when_save_other_type_different_of_category(self):
        dao = CategoryDao()
        type_str = 'Type str'
        
        with self.assertRaises(TypeError):
            dao.save(type_str)

    def test_should_throw_an_exception_when_find_by_book_not_exists(self):
        dao = CategoryDao()
        with self.assertRaises(KeyError):
            dao.find_one('Ciências')

    def test_should_add_category_in_list_categories_of_database(self):
        dao = CategoryDao()
        category_data_science = Category('Data Science')
        dao.save(category_data_science)
        
        assert category_data_science in dao.list_categories, "Temos um problema. A categoria não foi salva no database"

if __name__ == '__main__':
    unittest.main()
