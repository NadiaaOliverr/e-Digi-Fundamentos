from app.helpers.decorators import is_not_null
from app.model.author import Author
from app.config.setup_db import Connection

from typing import List


class AuthorDao:
    """Banco de Dados de Autores"""

    def __init__(self):
        self.connection = Connection.connect()
        self.db = self.connection.cursor(dictionary=True)

    def save(self, author: Author) -> None:
        if not isinstance(author, Author):
            raise TypeError('O argumento passado não é do tipo Autor')

        sql = 'INSERT INTO author(name, email) VALUES (%s, %s)'
        args = (author.name, author.email)

        self.db.execute(sql, args)
        self.connection.commit()

        print(f'\n---Autor inserido no banco---\n{author}')

    @is_not_null
    def find_one(self, email: str) -> Author:
        sql = 'SELECT name, email FROM author WHERE email = %s'
        self.db.execute(sql, (email, ))

        result_query = self.db.fetchone()

        if result_query:
            return Author(result_query['name'], result_query['email'])

        raise KeyError('Este autor não está cadastrado')

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()