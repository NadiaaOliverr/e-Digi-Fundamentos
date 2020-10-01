from app.model.book import Book
from app.model.category import Category
from app.model.author import Author
from app.dao.book_dao import BookDao
from app.dao.category_dao import CategoryDao
from app.dao.author_dao import AuthorDao
from app.config.connection_database import ConnectionDatabase
import mysql.connector.errors as db

import unittest


class TestBookDatabase(unittest.TestCase):

    def setUp(self):
        self.db = ConnectionDatabase()
        self.connection = self.db.connect()
        self.cursor = self.db.cursor()

        category_dao = CategoryDao(self.connection)
        category_dao.save(Category('IoT'))

        author_dao = AuthorDao(self.connection)
        author_dao.save(Author('Ramalho Sérgio','sergio@ramalho.com.br'))

    def _setup(self, title='Python Fluente', resume='Resumo '*80, summary='Sumário do Livro', 
                number_of_page=800,isbn="978-85-08-13196-9", author= Author('Ramalho Sérgio','sergio@ramalho.com.br'),
                category=Category('IoT'),edition=2, price=120.56):

        return Book(title, resume, summary, number_of_page, isbn, author, category, edition, price)
    
    def tearDown(self):
        sql_author = 'DELETE FROM author WHERE email = "sergio@ramalho.com.br"'
        sql_category = 'DELETE FROM category WHERE name = "IoT"'
        queries = [sql_author, sql_category]
        for query in queries: 
            self.cursor.execute(query)
            self.connection.commit()
        self.connection.close()

    def test_should_throw_an_exception_when_add_isbn_of_book_already_exists(self):
        dao = BookDao(self.connection)
        with self.assertRaises(db.IntegrityError):
            dao.save(self._setup())
            dao.save(self._setup(title="Python Fluent V2"))


    def test_should_throw_an_exception_when_add_title_of_book_already_exists(self):
        dao = BookDao(self.connection)
        with self.assertRaises(db.IntegrityError):
            dao.save(self._setup())
            dao.save(self._setup(isbn="978-95-08-13196-9"))

    def test_should_throw_an_exception_when_save_other_type_different_of_book(self):
        dao = BookDao(self.connection)
        type_str = 'Type str'
        with self.assertRaises(TypeError):
            dao.save(type_str)
    
    def test_should_throw_an_exception_when_find_by_book_not_exists(self):
        dao = BookDao(self.connection)
        with self.assertRaises(KeyError):
            dao.find_one('C++ Orientado a Objetos')
        
        with self.assertRaises(KeyError):
            dao.find_many('C++')
    
    def test_should_throw_an_exception_when_find_by_many_book_with_title_less_than_two_charactere(self):
        dao = BookDao(self.connection)
    
        with self.assertRaises(ValueError):
            dao.find_many('P')

    def test_should_add_book_in_database(self):
        dao = BookDao(self.connection)
        book_python_fluente = self._setup()
        dao.save(book_python_fluente)

        sql = 'SELECT isbn FROM book WHERE isbn="978-85-08-13196-9"'
        self.cursor.execute(sql)
        result_query = self.cursor.fetchone()
        
        self.assertEqual('978-85-08-13196-9', result_query['isbn'])

    def test_should_return_only_one_instance_the_book_when_find_by_one(self):
        dao = BookDao(self.connection)
        dao.save(self._setup())
        self.assertIsInstance(dao.find_one('Python Fluente'), Book)
    
    def test_should_return_list_of_many_book_when_find_by_many(self):
        dao = BookDao(self.connection)
        dao.save(self._setup())
        self.assertIsInstance(dao.find_many('Python Fluente'), list)

if __name__ == '__main__':
    unittest.main()
