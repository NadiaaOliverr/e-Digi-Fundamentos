from app.model.sale import Sale
from app.model.book import Book
from app.model.category import Category
from app.model.author import Author
from app.dao.sale_dao import SaleDao
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
            Category('Ciências'), "1234", 220.56
        )

        self.book_dao.save(self.book_sciences)

    def tearDown(self):
        BookDao.list_book = []
        CategoryDao.list_categories = []
        AuthorDao.list_authors = []

    def test_should_throw_an_exception_when_try_add_type_different_sale(self):
        dao = SaleDao()
        type_str = 'Type str'

        with self.assertRaises(TypeError):
            dao.add(type_str)

    def test_should_print_the_data_of_sale_save(self):
        dao = SaleDao()
        sale = Sale('Ciências Básica', 4)
        total_sale = self.book_sciences.price * sale.quantity_sale
        expected_result = f'\n--- Venda realizada com sucesso ---\n{sale}\nPreço total: R$ {total_sale:.2f}'
        dao.add(sale)

        self.assertEqual(dao.checkout(), expected_result)


if __name__ == '__main__':
    unittest.main()
