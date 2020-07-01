import unittest

from model import Book, Category, Author
from dao import BookDao


class TestBookDatabase(unittest.TestCase):

    def _setup(self, title='Python Fluente', resume='Resumo '*80, summary='Sumário do Livro', 
                number_of_page=800,isbn="978-85-08-13196-9", author= Author('Luciano Ramalho',
                'luciano@luciano.com.br'),category=Category('Programação'),
                edition="1254", price=120.56):
        
        return Book(title, resume, summary, number_of_page, isbn, author, category, edition, price)

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

    def test_should_print_the_data_of_book_save(self):
        dao = BookDao()
        book_python_fluente = self._setup()
        
        self.assertEqual(dao.save(book_python_fluente), book_python_fluente)

    def test_should_return_only_one_instance_the_book_when_find_by_one(self):
        dao = BookDao()
        self.assertIsInstance(dao.find_one('Python Fluente'), Book)
    
    def test_should_return_list_of_many_book_when_find_by_many(self):
        dao = BookDao()
        self.assertIsInstance(dao.find_many('Python Fluente'), list)

if __name__ == '__main__':
    unittest.main()
