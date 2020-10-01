from app.helpers.decorators import is_not_null
from app.model.author import Author
from app.config.connection_database import ConnectionDatabase

from typing import List


class AuthorDao:
    """Banco de Dados de Autores"""

    def __init__(self, db):
        self.db = db
        self._connection = self.db.connect()
        self._cursor = self.db.cursor()

    def save(self, author: Author) -> None:
        if not isinstance(author, Author):
            raise TypeError('O argumento passado não é do tipo Autor')

        sql = 'INSERT INTO author(name, email) VALUES (%s, %s)'
        args = (author.name, author.email)

        self._cursor.execute(sql, args)
        self._connection.commit()
        print(f'\n---Autor inserido no banco---\n{author}')

    @is_not_null
    def find_one(self, email: str) -> Author:
        sql = 'SELECT name, email FROM author WHERE email = %s'
        self._cursor.execute(sql, (email, ))

        result_query = self._cursor.fetchone()

        if result_query:
            return Author(result_query['name'], result_query['email'])

        raise KeyError('Este autor não está cadastrado')
