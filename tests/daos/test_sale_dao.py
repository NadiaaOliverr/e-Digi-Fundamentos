import unittest

from model import Sale, Book, Category, Author
from dao import SaleDao, BookDao


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
