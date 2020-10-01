from app.model.author import Author
from app.dao.author_dao import AuthorDao
from app.config.connection_database import ConnectionDatabase
import mysql.connector.errors as db

import unittest

class TestAuthorDatabase(unittest.TestCase):

    def setUp(self):
        self.db = ConnectionDatabase()
        self.connection = self.db.connect()
        self.cursor = self.db.cursor()


    def _setup(self, name='Luciano Ramalho', email='luciano@luciano.com.br'):
        return Author(name, email)

    def tearDown(self):
        sql_delete = 'DELETE FROM author WHERE email = "luciano@luciano.com.br"'
        self.cursor.execute(sql_delete)
        self.connection.commit()
        self.connection.close()
    
    def test_should_throw_an_exception_when_add_email_of_author_already_exists(self):
        dao = AuthorDao(self.connection)
        with self.assertRaises(db.IntegrityError):
            dao.save(self._setup())
            dao.save(self._setup())

    def test_should_throw_an_exception_when_save_other_type_different_of_author(self):
        dao = AuthorDao(self.connection)
        type_str = 'Type str'
        with self.assertRaises(TypeError):
            dao.save(type_str)
    
    def test_should_add_author_in_database(self):
        dao = AuthorDao(self.connection)
        author_luciano = self._setup()
        dao.save(author_luciano)
        
        sql = 'SELECT email FROM author WHERE email="luciano@luciano.com.br"'
        self.cursor.execute(sql)
        result_query = self.cursor.fetchone()
        
        self.assertEqual('luciano@luciano.com.br', result_query['email'])


if __name__ == '__main__':
    unittest.main()
