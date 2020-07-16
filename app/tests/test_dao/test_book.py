from app.model.book import Book
from app.model.category import Category
from app.model.author import Author
from app.dao.book_dao import BookDao
from app.dao.category_dao import CategoryDao
from app.dao.author_dao import AuthorDao


import unittest


class TestBookDatabase(unittest.TestCase):

    def _setup(self, title='Python Fluente', resume='Resumo '*80, summary='Sumário do Livro', 
                number_of_page=800,isbn="978-85-08-13196-9", author= Author('Luciano Ramalho',
                'luciano@luciano.com.br'),category=Category('Programação'),
                edition=2, price=120.56):
        
        category_dao = CategoryDao()
        category_dao.save(Category('Programação'))

        author_dao = AuthorDao()
        author_dao.save(Author('Luciano Ramalho','luciano@luciano.com.br'))

        return Book(title, resume, summary, number_of_page, isbn, author, category, edition, price)
    
    def tearDown(self):
        BookDao.list_book = []
        CategoryDao.list_categories = []
        AuthorDao.list_authors = []

    def test_should_throw_an_exception_when_add_isbn_of_book_already_exists(self):
        dao = BookDao()
        with self.assertRaises(ValueError):
            dao.save(self._setup())
            dao.save(self._setup(title="Python Fluent V2"))


    def test_should_throw_an_exception_when_add_title_of_book_already_exists(self):
        dao = BookDao()
        with self.assertRaises(ValueError):
            dao.save(self._setup())
            dao.save(self._setup(isbn="978-95-08-13196-9"))

    def test_should_throw_an_exception_when_save_other_type_different_of_book(self):
        dao = BookDao()
        type_str = 'Type str'
        with self.assertRaises(TypeError):
            dao.save(type_str)
    
    def test_should_throw_an_exception_when_find_by_book_not_exists(self):
        dao = BookDao()
        with self.assertRaises(KeyError):
            dao.find_one('Ciências')
        
        with self.assertRaises(KeyError):
            dao.find_many('Ciências')
    
    def test_should_throw_an_exception_when_find_by_many_book_with_title_less_than_two_charactere(self):
        dao = BookDao()
    
        with self.assertRaises(ValueError):
            dao.find_many('P')

    def test_should_add_book_in_list_books_of_database(self):
        dao = BookDao()
        book_python_fluente = self._setup()
        dao.save(book_python_fluente)
        
        assert book_python_fluente in dao.list_book, "Temos um problema. O livro não foi salvo no database"

    def test_should_return_only_one_instance_the_book_when_find_by_one(self):
        dao = BookDao()
        dao.save(self._setup())
        self.assertIsInstance(dao.find_one('Python Fluente'), Book)
    
    def test_should_return_list_of_many_book_when_find_by_many(self):
        dao = BookDao()
        dao.save(self._setup())
        self.assertIsInstance(dao.find_many('Python Fluente'), list)

if __name__ == '__main__':
    unittest.main()