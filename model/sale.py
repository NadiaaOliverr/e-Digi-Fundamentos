from model import Book
from datetime import datetime
from dao import BookDao

class Sale:
    """Modelo de Venda"""

    __attributes = ('_book', '_quantity_sale', '_registration_time')

    book_dao = BookDao()

    def __init__(self, title_book: str, quantity_book: int) -> None:
        self.__set_book_for_sale(title_book)
        self.quantity_sale = quantity_book
        self._registration_time = datetime.now()

    def __str__(self) -> str:
        return f'Livro: {self._book.title} - Quantidade: {self.quantity_sale} - Preço: {self._book.price}'

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, self._book.title, self.quantity_sale)

    @property
    def price_book(self):
        return self._book.price

    @property
    def title_book(self):
        return self._book.title

    @property
    def quantity_sale(self):
        return self._quantity_sale

    @quantity_sale.setter
    def quantity_sale(self, quantity_book: int) -> None:
        if quantity_book <= 0:
            raise Exception('A quantidade de livros deve ser de pelo menos 1')
        self._quantity_sale = quantity_book

    def __set_book_for_sale(self, title_book: str) -> Book:
        book = self.book_dao.find_by_title(title_book)
        self._book = book
