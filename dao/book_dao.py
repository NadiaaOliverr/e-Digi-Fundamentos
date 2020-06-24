from helpers import is_not_null
from model import Book
from typing import List


class BookDao:
    """Banco de Dados de Livros"""

    list_book: List[Book] = []

    def save(self, book: Book) -> None:
        if isinstance(book, Book):
            if book in self.list_book:
                raise ValueError('Este título já consta em nossos acervos.')
            self.list_book.append(book)
            return f'\n---Livro Cadastrado---\n{book}\n'
        else:
            raise TypeError('O argumento passado não é do tipo Livro')

    @is_not_null
    def find_many(self, title: str) -> List[Book]:
        if len(title) >= 2:
            books_with_title = list(
                filter(lambda books: title.lower() in books.title.lower(),  self.list_book))
            if books_with_title:
                return books_with_title
            else:
                KeyError('Este título não consta no acervo')
        else:
            raise ValueError('É necessário ao menos 2 caracteres para fazer a busca')

    
    @is_not_null
    def find_one(self, title: str) -> Book:
        for book in self.list_book:
            if title.lower() == book.title.lower():
                return book
        raise KeyError('Este título não consta no acervo')
        
