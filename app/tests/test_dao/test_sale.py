from app.model.sale import Sale
from app.model.book import Book
from app.model.category import Category
from app.model.author import Author
from app.dao.sale_dao import SaleDao
from app.dao.book_dao import BookDao
from app.dao.category_dao import CategoryDao
from app.config.connection_database import ConnectionDatabase
from app.dao.author_dao import AuthorDao

import unittest

class TestSale(unittest.TestCase):

    def setUp(self):
        self.db = ConnectionDatabase()
        self.connection = self.db.connect()
        self.cursor = self.db.cursor()

        self.book_sciences = Book(
            'Ciências Básica', 'Resumo '*80, 'Sumário do Livro',
            700, "978-85-08-22282-8", Author('Luciano Pereira', 'luciano@pereira.com.br'),
            Category('Ciências'), 1, 220.56
        )

        dao_author = AuthorDao(self.db)
        dao_author.save(Author('Luciano Pereira', 'luciano@pereira.com.br'))

        dao_category = CategoryDao(self.db)
        dao_category.save(Category('Ciências'))

        dao_book = BookDao(self.db)
        dao_book.save(self.book_sciences)
        self.db.close()

    def tearDown(self):
        sql_author = 'DELETE FROM author WHERE email = "luciano@pereira.com.br"'
        sql_category = 'DELETE FROM category WHERE name = "Ciências"'
        sql_book = 'DELETE FROM book WHERE isbn="978-85-08-22282-8"'
        queries = [sql_author, sql_category, sql_book]
        for query in queries: 
            self.cursor.execute(query)
            self.connection.commit()
        self.db.close()

    def test_should_throw_an_exception_when_try_add_type_different_sale(self):
        dao = SaleDao(self.db)
        type_str = 'Type str'

        with self.assertRaises(TypeError):
            dao.add(type_str)
        self.db.close()

    def test_should_add_sale_in_database(self):
        dao = SaleDao(self.db)
        sale = Sale(self.book_sciences, 4)
        dao.add(sale)
        dao.checkout()

        sql = 'SELECT title FROM sale AS s JOIN book AS b on s.book_id=b.id WHERE title = "Ciências Básica"'
        self.cursor.execute(sql)
        result_query = self.cursor.fetchone()
        
        self.assertEqual('Ciências Básica', result_query['title'])
        self.db.close()



if __name__ == '__main__':
    unittest.main()
