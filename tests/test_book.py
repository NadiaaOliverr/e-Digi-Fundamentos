import unittest

from model import Book, Category, Author
from dao import BookDao


class TestBook(unittest.TestCase):

    def _setup(self, title='Python Fluente', resume='Resumo '*80, summary='Sumário do Livro', 
                number_of_page=800,isbn="978-85-08-13196-9", author= Author('Luciano Ramalho',
                'luciano@luciano.com.br'),category=Category('Programação'),
                edition="1254", price=120.56):
        
        return Book(title, resume, summary, number_of_page, isbn, author, category, edition, price)


    def test_should_throw_an_exception_when_the_title_book_is_none(self):
        with self.assertRaises(Exception):
            self._setup(title=None)

    def test_should_throw_an_exception_when_the_title_book_is_empty(self):
        with self.assertRaises(Exception):
            self._setup(title='')

    def test_should_throw_an_exception_when_the_title_book_is_empty_full_spaces(self):
        with self.assertRaises(Exception):
            self._setup(title='   ')

    def test_should_throw_an_exception_when_the_resume_book_is_none(self):
        with self.assertRaises(Exception):
            self._setup(resume=None)

    def test_should_throw_an_exception_when_the_resume_book_is_empty(self):
        with self.assertRaises(Exception):
           self._setup(resume='')

    def test_should_throw_an_exception_when_the_resume_book_is_empty_full_spaces(self):
        with self.assertRaises(Exception):
            self._setup(resume='   ')

    def test_should_throw_an_exception_when_the_summary_book_is_none(self):
        with self.assertRaises(Exception):
            self._setup(summary=None)

    def test_should_throw_an_exception_when_the_summary_book_is_empty(self):
        with self.assertRaises(Exception):
            self._setup(summary='')

    def test_should_throw_an_exception_when_the_summary_book_is_empty_full_spaces(self):
        with self.assertRaises(Exception):
            self._setup(summary='     ')

    def test_should_throw_an_exception_when_the_number_of_pages_less_than_zero(self):
        with self.assertRaises(Exception):
            self._setup(number_of_page=-1)

    def test_should_throw_an_exception_when_the_isbn_not_should_format_valid(self):
        with self.assertRaises(Exception):
            self._setup(isbn="569-85-08-13196-9")

    def test_should_throw_an_exception_when_the_edition_not_started_with_one(self):
        with self.assertRaises(Exception):
            self._setup(edition="2354")

    def test_should_throw_an_exception_when_the_price_less_than_zero(self):
        with self.assertRaises(Exception):
            self._setup(price=-10.90)

    def test_should_throw_an_exception_when_add_isbn_of_book_already_exists_in_database(self):
        dao = BookDao()
        with self.assertRaises(Exception):
            dao.save(self._setup())
            dao.save(self._setup(title="Python Fluent V2"))


    def test_should_throw_an_exception_when_add_title_of_book_already_exists_in_database(self):
        dao = BookDao()
        with self.assertRaises(Exception):
            dao.save(self._setup())
            dao.save(self._setup(isbn="978-95-08-13196-9"))

    def test_should_throw_an_exception_when_save_in_database_other_type_different_of_book(self):
        dao = BookDao()
        type_str = 'Type str'
        with self.assertRaises(Exception):
            dao.save(type_str)


if __name__ == '__main__':
    unittest.main()
