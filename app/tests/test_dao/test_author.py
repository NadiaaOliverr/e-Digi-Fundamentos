from app.model.author import Author
from app.dao.author_dao import AuthorDao

import unittest

class TestAuthorDatabase(unittest.TestCase):

    def _setup(self, name='Luciano Ramalho', email='luciano@luciano.com.br'):
        return Author(name, email)

    def tearDown(self):
        AuthorDao.list_authors = []
    
    def test_should_throw_an_exception_when_add_email_of_author_already_exists(self):
        dao = AuthorDao()
        with self.assertRaises(ValueError):
            dao.save(self._setup())
            dao.save(self._setup())

    def test_should_throw_an_exception_when_save_other_type_different_of_author(self):
        dao = AuthorDao()
        type_str = 'Type str'
        with self.assertRaises(TypeError):
            dao.save(type_str)
    
    def test_should_return_none_when_the_data_of_author_save(self):
        dao = AuthorDao()
        author_luciano = self._setup()

        self.assertIsNone(dao.save(author_luciano))


if __name__ == '__main__':
    unittest.main()
