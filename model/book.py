from helpers import is_not_null
from model import Author, Category
from datetime import datetime
import re


class Book:
    """Modelo de Livros"""

    __attributes = (
        '_title', '_resume', '_summary', '_number_of_pages',
        '_isbn', '_author', '_category', '_edition', '_price'
    )

    def __init__(
            self, title: str, resume: str, summary: str, number_of_pages: int,
            isbn: str, author: Author, category: Category, edition: str, price: float
        ) -> None:

        self.__set_title(title)
        self.__set_resume(resume)
        self.__set_summary(summary)
        self.__set_number_of_pages(number_of_pages)
        self.__set_isbn(isbn)
        self._author = author
        self._category = category
        self.__set_edition(edition)
        self.__set_price(price)
        self._registration_time = datetime.now()

    def __str__(self) -> None:
        return (
            f'Título: {self._title}\n'
            f'Resumo: {self._resume}\n'
            f'Sumário: {self._sumary}\n'
            f'Número de Páginas: {self._number_of_pages}\n'
            f'ISBN: {self._isbn}\n'
            f'Autor: {self._author.name}\n'
            f'Categoria: {self._category.name_category}\n'
            f'Edição: {self._edition}\n'
            f'Preço: R$ {self._price}\n'
        )

    def __repr__(self) -> None:
        class_name = type(self).__name__
        return (
                '{}({!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(
                    class_name,
                    self._title,
                    self._resume,
                    self._sumary,
                    self._number_of_pages,
                    self._isbn,
                    self._author.name,
                    self._category.name_category,
                    self._edition,
                    self._price,
                    self._registration_time
            )
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title or self.isbn == other.isbn

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @ is_not_null
    def __set_title(self, title: str) -> None:
        self._title=title

    @is_not_null
    def __set_resume(self, resume: str) -> None:
        if len(resume) < 500:
            raise Exception('O resumo precisa conter mais de 500 caracteres')
        self._resume=resume

    @ is_not_null
    def __set_summary(self, summary: str) -> None:
        self._sumary=summary

    def __set_number_of_pages(self, number_of_pages: int) -> None:
        if number_of_pages < 0:
            raise Exception('O número de páginas precisa ser maior que zero')
        self._number_of_pages=number_of_pages

    def __set_isbn(self, isbn: str) -> None:
        pattern=r"978-[0-9]{2}-[0-9]{2}-[0-9]{5}-[0-9]{1}"
        isbn_is_valid=re.search(pattern, isbn)
        if not isbn_is_valid:
            raise Exception('O ISBN passado não possui um formato válido')
        self._isbn=isbn
            

    def __set_edition(self, edition: str) -> None:
        pattern=r"1[0-9]*"
        edition_is_valid=re.search(pattern, edition)
        if not edition_is_valid:
            raise Exception('A edição digitada não possui formato válido')
        self._edition=edition
        

    def __set_price(self, price: float) -> None:
        if not price >= 0:
            raise Exception('O preço deve ser maior que zero')
        self._price=price
        
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def price(self) -> float:
        return self._price