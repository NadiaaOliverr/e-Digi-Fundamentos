from app.model.sale import Sale
from app.model.book import Book
from app.model.category import Category
from app.model.author import Author
from app.dao.sale_dao import SaleDao
from app.dao.book_dao import BookDao

import unittest



class TestSale(unittest.TestCase):

    def setUp(self):
        self.book_dao = BookDao()

        self.book_sciences = Book(
            'Ciências Básica', 'Resumo '*80, 'Sumário do Livro',
            700, "978-85-08-22282-8", Author('Luciano Pereira', 'luciano@pereira.com.br'),
            Category('Ciências'), "1234", 220.56
        )

        self.book_dao.save(self.book_sciences)

    def tearDown(self):
        BookDao.list_book = []

    def test_should_throw_an_exception_when_quantity_sale_less_than_zero(self):
        book_sciences = 'Ciências Básica'

        with self.assertRaises(ValueError):
            Sale(book_sciences, -1)

if __name__ == '__main__':
    unittest.main()
