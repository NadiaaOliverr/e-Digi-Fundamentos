from model import Author
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

        return f'\n---Autor Cadastrado---\n{author}\n'


