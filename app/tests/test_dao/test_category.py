from app.model.category import Category
from app.dao.category_dao import CategoryDao
from app.config.connection_database import ConnectionDatabase
import mysql.connector.errors as db

import unittest

class TestCategoryDatabase(unittest.TestCase):

    def setUp(self):
        self.db = ConnectionDatabase()
        self.connection = self.db.connect()
        self.cursor = self.db.cursor()

    def tearDown(self):
        sql_delete = 'DELETE FROM category WHERE name = "Programming" OR name="Data Science"'
        self.cursor.execute(sql_delete)
        self.connection.commit()
        self.connection.close()

    def test_should_throw_an_exception_when_add_name_of_category_already_exists(self):
        
        dao = CategoryDao(self.connection)
        category_programming = Category('Programming')
        category_already_exists_programming = Category('Programming')
        dao.save(category_programming)

        with self.assertRaises(db.IntegrityError):
            dao.save(category_already_exists_programming)
    

    def test_should_throw_an_exception_when_save_other_type_different_of_category(self):
        dao = CategoryDao(self.connection)
        type_str = 'Type str'
        
        with self.assertRaises(TypeError):
            dao.save(type_str)

    def test_should_throw_an_exception_when_find_by_book_not_exists(self):
        dao = CategoryDao(self.connection)

        with self.assertRaises(KeyError):
            dao.find_one('Ciências Avançadas')

    def test_should_add_category_in_database(self):
        dao = CategoryDao(self.connection)
        category_data_science = Category('Data Science')
        dao.save(category_data_science)

        sql = 'SELECT name FROM category WHERE name="Data Science"'
        self.cursor.execute(sql)
        result_query = self.cursor.fetchone()
        
        self.assertEqual('Data Science', result_query['name'])

if __name__ == '__main__':
    unittest.main()
