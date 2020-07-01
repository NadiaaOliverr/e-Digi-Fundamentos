from app.helpers.decorators import is_not_null
from app.model.author import Author

from typing import List


class AuthorDao:
    """Banco de Dados de Autores"""

    list_authors: List[Author] = []

    def save(self, author: Author) -> str:
        if not isinstance(author, Author):
            raise TypeError('O argumento passado não é do tipo Autor')

        if author in self.list_authors:
            raise ValueError('Este e-mail já consta na base de dados.')

        self.list_authors.append(author)

        return author

    @is_not_null
    def find_one(self, email: str) -> Author:
        for author in self.list_authors:
            if email.lower() == author.email.lower():
                return author
        raise KeyError('Este autor não está cadastrado')
