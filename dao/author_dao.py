from model import Author
from typing import List

class AuthorDao:
    """Banco de Dados de Autores"""

    _list_authors: List[Author] = []

    def add_author(self, author: Author) -> None:
        if author in self._list_authors:
            raise Exception('Este e-mail já consta na base de dados.')
        self._list_authors.append(author)
        print(f'\n---Autor Cadastrado---\n{author}\n')

    def all_authors(self) -> list:
        return self._list_authors.copy()
