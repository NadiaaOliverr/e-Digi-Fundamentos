import unittest

from model import Book, Category, Author
from dao import BookDao


class TestBook(unittest.TestCase):

    def _setup(self, title='Python Fluente', resume='Resumo '*80, summary='Sumário do Livro', 
                number_of_page=800,isbn="978-85-08-13196-9", author= Author('Luciano Ramalho',
                'luciano@luciano.com.br'),category=Category('Programação'),
                edition="1254", price=120.56):
        
        return Book(title, resume, summary, number_of_page, isbn, author, category, edition, price)


    def test_should_throw_an_exception_when_the_field_is_none(self):
        with self.assertRaises(ValueError):
            self._setup(title=None)
        
        with self.assertRaises(ValueError):
            self._setup(resume=None)
        
        with self.assertRaises(ValueError):
            self._setup(summary=None)

    def test_should_throw_an_exception_when_the_field_is_empty(self):
        with self.assertRaises(ValueError):
            self._setup(title='')
        
        with self.assertRaises(ValueError):
            self._setup(resume='')
        
        with self.assertRaises(ValueError):
            self._setup(summary='')

    def test_should_throw_an_exception_when_the_field_is_empty_full_spaces(self):
        with self.assertRaises(ValueError):
            self._setup(title='   ')

        with self.assertRaises(ValueError):
            self._setup(resume='   ')

        with self.assertRaises(ValueError):
            self._setup(summary='     ')

    def test_should_throw_an_exception_when_the_number_of_pages_less_than_zero(self):
        with self.assertRaises(ValueError):
            self._setup(number_of_page=-1)

    def test_should_throw_an_exception_when_the_field_not_should_format_valid(self):
        with self.assertRaises(ValueError):
            self._setup(isbn="569-85-08-13196-9")

    def test_should_throw_an_exception_when_the_edition_not_started_with_one(self):
        with self.assertRaises(ValueError):
            self._setup(edition="2354")

    def test_should_throw_an_exception_when_the_price_less_than_zero(self):
        with self.assertRaises(ValueError):
            self._setup(price=-10.90)


if __name__ == '__main__':
    unittest.main()
