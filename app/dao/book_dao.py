from app.helpers.decorators import is_not_null
from app.model.book import Book
from app.model.author import Author
from app.model.category import Category

from typing import List


class BookDao:
    """Banco de Dados de Livros"""

    def __init__(self, db):
        self.db = db
        self._connection = self.db.connect()
        self._cursor = self.db.cursor()

    def save(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError('O argumento passado não é do tipo Livro')

        sql = """INSERT INTO book(
                category_id, author_id, title, 
                resume, summary, number_of_pages,
                isbn,edition, price) VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        args = (
            book.id_category, book.id_author, book.title,
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

        sql = """
                SELECT title, resume, summary, number_of_pages, isbn, edition, price, c.name as 'name_category', a.name as 'name_author', a.email 
                FROM book as b join category as c join author as a on b.category_id=c.id and b.author_id = a.id 
                WHERE title LIKE %s
            """
        
        self._cursor.execute(sql, (f'%{title}%', ))
        result_query_book = self._cursor.fetchall()

        if not result_query_book:
            raise KeyError('Este título não consta no acervo')

        for item in result_query_book:
            book = Book(item['title'], item['resume'], item['summary'], item['number_of_pages'],
                        item['isbn'], Author(item['name_author'], item['email']),
                        Category(item['name_category']),
                        item['edition'], item['price'])

            list_book.append(book)

        return list_book

    @is_not_null
    def find_one(self, title: str) -> Book:
        sql = """
                SELECT title, resume, summary, number_of_pages, isbn, edition, price, c.name as 'name_category', a.name as 'name_author', a.email 
                FROM book as b join category as c join author as a on b.category_id=c.id and b.author_id = a.id 
                WHERE title = %s
            """
        self._cursor.execute(sql, (title, ))
        result_query = self._cursor.fetchone()

        if not result_query:
            raise KeyError('Este título não consta no acervo')
        
        return Book(result_query['title'], result_query['resume'], result_query['summary'],
                    result_query['number_of_pages'], result_query['isbn'], Author(result_query['name_category'], result_query['email']),
                    Category(result_query['name_category']), result_query['edition'], result_query['price'])
