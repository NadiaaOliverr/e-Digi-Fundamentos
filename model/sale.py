from model import Book
from datetime import datetime


class Sale:
    """Modelo de Venda"""

    __attributes = ('_title_book', '_quantity_book')

    def __init__(self, title_book: Book, quantity_book: int) -> None:
        self._title_book = title_book
        self.quantity_book = quantity_book

    def __str__(self) -> str:
        return f'Livro: {self._title_book} - Quantidade: {self.quantity_book}'

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, self._title_book, self.quantity_book)

    @property
    def title_book(self):
        return self._title_book

    @property
    def quantity_book(self):
        return self._quantity_book

    @quantity_book.setter
    def quantity_book(self, quantity_book: int) -> None:
        if quantity_book <= 0:
            raise Exception('A quantidade de livros deve ser de pelo menos 1')
        self._quantity_book = quantity_book
