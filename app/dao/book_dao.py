from app.helpers.decorators import is_not_null
from app.model.book import Book
from app.model.author import Author
from app.model.category import Category

from typing import List


class BookDao:
    """Banco de Dados de Livros"""

    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor(dictionary=True, buffered=True)

    def save(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError('O argumento passado não é do tipo Livro')

        sql_category_id = 'SELECT id FROM category WHERE name = %s'
        self._cursor.execute(sql_category_id, (book.category_name,))
        category_id = self._cursor.fetchone()

        sql_author_id = 'SELECT id FROM author WHERE name = %s'
        self._cursor.execute(sql_author_id, (book.author_name,))
        author_id = self._cursor.fetchone()

        sql = """INSERT INTO book(
                category_id, author_id, title, 
                resume, summary, number_of_pages,
                isbn,edition, price) VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        args = (
            category_id['id'], author_id['id'], book.title,
            book.resume, book.summary, book.number_of_pages,
            book.isbn, book.edition, book.price
        )

        self._cursor.execute(sql, args)
        self._connection.commit()

        print(f'\n---Livro inserido no banco---\n{book}')

    @is_not_null
    def find_many(self, title: str) -> List[Book]:

        list_book = []

        if len(title) < 2:
            raise ValueError('É necessário ao menos 2 caracteres para fazer a busca')

        sql = 'SELECT * FROM book WHERE title LIKE %s'
        self._cursor.execute(sql, (f'%{title}%', ))
        result_query_book = self._cursor.fetchall()

        if not result_query_book:
            raise KeyError('Este título não consta no acervo')

        for item in result_query_book:
            book = Book(item['title'], item['resume'], item['summary'], item['number_of_pages'],
                        item['isbn'], self.__search_author_for_id(item['author_id']),
                        self.__search_category_for_id(item['category_id']),
                        item['edition'], item['price'])

            list_book.append(book)

        return list_book

    @is_not_null
    def find_one(self, title: str) -> Book:
        sql = 'SELECT * FROM book WHERE title = %s'
        self._cursor.execute(sql, (title, ))
        result_query = self._cursor.fetchone()

        if not result_query:
            raise KeyError('Este título não consta no acervo')

        author = self.__search_author_for_id(result_query['author_id'])
        category = self.__search_category_for_id(result_query['category_id'])
        
        return Book(result_query['title'], result_query['resume'], result_query['summary'],
                    result_query['number_of_pages'], result_query['isbn'], author, category,
                    result_query['edition'], result_query['price'])

    def __search_category_for_id(self, id) -> Category:
        sql_category = 'SELECT * FROM category WHERE id = %s'
        self._cursor.execute(sql_category, (id,))
        category = self._cursor.fetchone()

        return Category(category['name'])

    def __search_author_for_id(self, id) -> Author:
        sql_author = 'SELECT * FROM author WHERE id = %s'
        self._cursor.execute(sql_author, (id,))
        author = self._cursor.fetchone()

        return Author(author['name'], author['email'])
