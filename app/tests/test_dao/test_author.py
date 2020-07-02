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
    
    def test_should_add_author_in_list_authors_of_database(self):
        dao = AuthorDao()
        author_luciano = self._setup()
        dao.save(author_luciano)

        assert author_luciano in dao.list_authors, "Temos um problema. O autor não foi salvo no database"
        

if __name__ == '__main__':
    unittest.main()
