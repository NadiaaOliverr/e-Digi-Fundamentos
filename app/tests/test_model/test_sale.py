from app.model.sale import Sale
from app.model.book import Book
from app.model.category import Category
from app.model.author import Author
from app.dao.book_dao import BookDao
from app.dao.category_dao import CategoryDao
from app.dao.author_dao import AuthorDao

import unittest



class TestSale(unittest.TestCase):

    def setUp(self):
        self.book_dao = BookDao()

        category_dao = CategoryDao()
        category_dao.save(Category('Ciências'))

        author_dao = AuthorDao()
        author_dao.save(Author('Luciano Pereira', 'luciano@pereira.com.br'))

        self.book_sciences = Book(
            'Ciências Básica', 'Resumo '*80, 'Sumário do Livro',
            700, "978-85-08-22282-8", Author('Luciano Pereira', 'luciano@pereira.com.br'),
            Category('Ciências'), 2, 220.56
        )

        self.book_dao.save(self.book_sciences)

    def tearDown(self):
        BookDao.list_book = []
        CategoryDao.list_categories = []
        AuthorDao.list_authors = []

    def test_should_throw_an_exception_when_quantity_sale_less_than_zero(self):
        book_sciences = 'Ciências Básica'

        with self.assertRaises(ValueError):
            Sale(book_sciences, -1)

if __name__ == '__main__':
    unittest.main()
