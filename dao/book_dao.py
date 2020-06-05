from helpers import is_not_null
from model import Book
from typing import List


class BookDao:
    """Banco de Dados de Livros"""

    _list_books: List[Book] = []

    def save(self, book: Book) -> None:
        if isinstance(book, Book):
            if book in self._list_books:
                raise Exception('Este título já consta em nossos acervos.')
            self._list_books.append(book)
            print(f'\n---Livro Cadastrado---\n{book}\n')
        else:
            raise Exception('O argumento passado não é do tipo Livro')

    @is_not_null
    def find_by_title(self, title: str) -> List[Book]:
        if len(title) >= 2:
            books_with_title = list(
                filter(lambda books: title in books.title,  self._list_books))
            return books_with_title
        else:
            raise('É necessário ao menos 2 caracteres para fazer a busca')

    def all_books(self) -> list:
        return self._list_books.copy()
