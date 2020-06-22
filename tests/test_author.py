import unittest

from model import Author
from dao import AuthorDao


class TestAuthor(unittest.TestCase):

    def test_should_throw_an_exception_when_the_name_author_is_none(self):
        with self.assertRaises(Exception):
            author_name_is_none = Author(None, 'autor@autor.com.br')

    def test_should_throw_an_exception_when_the_name_author_is_empty(self):
        with self.assertRaises(Exception):
            author_name_is_empty = Author('', 'autor@autor.com.br')

    def test_should_throw_an_exception_when_the_name_author_is_empty_full_spaces(self):
        with self.assertRaises(Exception):
            author_name_with_empty_spaces = Author('   ', 'autor@autor.com.br')

    def test_should_throw_an_exception_when_the_email_author_is_none(self):
        with self.assertRaises(Exception):
            author_email_is_none = Author('Luciano Ramalho', None)

    def test_should_throw_an_exception_when_the_email_author_is_empty(self):
        with self.assertRaises(Exception):
            author_email_is_empty = Author('Luciano Ramalho', '')

    def test_should_throw_an_exception_when_the_name_email_is_empty_full_spaces(self):
        with self.assertRaises(Exception):
            author_email_with_empty_spaces = Author('Luciano Ramalho', '     ')

    def test_should_throw_an_exception_when_the_email_not_is_valid(self):
        with self.assertRaises(Exception):
            author_email_not_valid = Author('Luciano Ramalho', 'luciano')

        with self.assertRaises(Exception):
            author_email_not_valid = Author('Luciano Ramalho', 'luciano@')

    def test_should_throw_an_exception_when_add_email_of_author_already_exists_in_database(self):
        dao = AuthorDao()
        author_luciano = Author('Luciano Ramalho', 'luciano@luciano.com')
        author_already_exists_luciano = Author(
            'Luciano Ramalho Souza', 'luciano@luciano.com')
        dao.save(author_luciano)

        with self.assertRaises(Exception):
            dao.save(author_already_exists_luciano)

    def test_should_throw_an_exception_when_save_in_database_other_type_different_of_author(self):
        dao = AuthorDao()
        type_str = 'Type str'
        with self.assertRaises(Exception):
            dao.save(type_str)


if __name__ == '__main__':
    unittest.main()
