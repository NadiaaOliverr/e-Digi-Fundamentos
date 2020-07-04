from app.model.book import Book
from app.model.category import Category
from app.model.author import Author
from app.dao.category_dao import CategoryDao
from app.dao.author_dao import AuthorDao

import unittest



class TestBook(unittest.TestCase):

    def _setup(self, title='Python Fluente', resume='Resumo '*80, summary='Sumário do Livro', 
                number_of_page=800,isbn="978-85-08-13196-9", author= Author('Luciano Ramalho',
                'luciano@luciano.com.br'),category=Category('Programação'),
                edition=2, price=120.56):
        
        category_dao = CategoryDao()
        category_dao.save(Category('Programação'))

        author_dao = AuthorDao()
        author_dao.save(Author('Luciano Ramalho', 'luciano@luciano.com.br'))
        
        return Book(title, resume, summary, number_of_page, isbn, author, category, edition, price)

    def tearDown(self):
        CategoryDao.list_categories = []
        AuthorDao.list_authors = []

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

    def test_should_throw_an_exception_when_the_edition_less_than_or_equal_to_zero(self):
        with self.assertRaises(ValueError):
            self._setup(edition=0)

    def test_should_throw_an_exception_when_the_price_less_than_zero(self):
        with self.assertRaises(ValueError):
            self._setup(price=-10.90)


if __name__ == '__main__':
    unittest.main()
