from app.model.author import Author
from app.dao.author_dao import AuthorDao

import unittest



class TestAuthor(unittest.TestCase):

    def _setup(self, name='Luciano Ramalho', email='luciano@luciano.com.br'):
        return Author(name, email)

    def test_should_throw_an_exception_when_the_field_is_none(self):
        with self.assertRaises(ValueError):
            self._setup(name=None)
        
        with self.assertRaises(ValueError):
            self._setup(email=None)
        
    def test_should_throw_an_exception_when_the_field_is_empty(self):
        with self.assertRaises(ValueError):
            self._setup(name='')
        
        with self.assertRaises(ValueError):
            self._setup(email='')

    def test_should_throw_an_exception_when_the_field_is_empty_full_spaces(self):
        with self.assertRaises(ValueError):
            self._setup(name='     ')

        with self.assertRaises(ValueError):
            self._setup(email='      ')

    def test_should_throw_an_exception_when_the_email_not_is_valid(self):
        with self.assertRaises(ValueError):
            self._setup(email='luciano')

        with self.assertRaises(ValueError):
           self._setup(email='luciano@')

if __name__ == '__main__':
    unittest.main()
