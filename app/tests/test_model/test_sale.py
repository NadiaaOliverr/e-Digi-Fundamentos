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
        self.book_sciences = Book(
            'Ciências Básica', 'Resumo '*80, 'Sumário do Livro',
            700, "978-85-08-22282-8", Author('Luciano Pereira', 'luciano@pereira.com.br'),
            Category('Ciências'), 2, 220.56
        )

    def test_should_throw_an_exception_when_quantity_sale_less_than_zero(self):
        book_sciences = self.book_sciences

        with self.assertRaises(ValueError):
            Sale(book_sciences, -1)

if __name__ == '__main__':
    unittest.main()
