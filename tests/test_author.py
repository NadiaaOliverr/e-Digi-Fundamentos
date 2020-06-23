import unittest

from model import Author
from dao import AuthorDao


class TestAuthor(unittest.TestCase):

    def _setup(self, name='Luciano Ramalho', email='luciano@luciano.com.br'):
        return Author(name, email)

    def test_should_throw_an_exception_when_the_name_author_is_none(self):
        with self.assertRaises(Exception):
            self._setup(name=None)

    def test_should_throw_an_exception_when_the_name_author_is_empty(self):
        with self.assertRaises(Exception):
            self._setup(name='')

    def test_should_throw_an_exception_when_the_name_author_is_empty_full_spaces(self):
        with self.assertRaises(Exception):
            self._setup(name='     ')

    def test_should_throw_an_exception_when_the_email_author_is_none(self):
        with self.assertRaises(Exception):
            self._setup(email=None)

    def test_should_throw_an_exception_when_the_email_author_is_empty(self):
        with self.assertRaises(Exception):
            self._setup(email='')

    def test_should_throw_an_exception_when_the_name_email_is_empty_full_spaces(self):
        with self.assertRaises(Exception):
            self._setup(email='      ')

    def test_should_throw_an_exception_when_the_email_not_is_valid(self):
        with self.assertRaises(Exception):
            self._setup(email='luciano')

        with self.assertRaises(Exception):
           self._setup(email='luciano@')

    def test_should_throw_an_exception_when_add_email_of_author_already_exists_in_database(self):
        dao = AuthorDao()
        with self.assertRaises(Exception):
            dao.save(self._setup())
            dao.save(self._setup())

    def test_should_throw_an_exception_when_save_in_database_other_type_different_of_author(self):
        dao = AuthorDao()
        type_str = 'Type str'
        with self.assertRaises(Exception):
            dao.save(type_str)


if __name__ == '__main__':
    unittest.main()
