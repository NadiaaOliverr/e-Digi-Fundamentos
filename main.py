"""Executa as classes de model e dao."""
from app.model.author import Author
from app.model.book import Book
from app.model.category import Category
from app.model.sale import Sale
from app.dao.book_dao import BookDao
from app.dao.sale_dao import SaleDao
from app.dao.category_dao import CategoryDao
from app.dao.author_dao import AuthorDao
from app.config.connection_database import ConnectionDatabase




__author__ = "Nádia Oliveira"
__email__ = "nadiaaoliverr@gmail.com"
__status__ = "Em desenvolvimento"


def register_categories_database(): 
    
    connection = ConnectionDatabase.connect()

    dao = CategoryDao(connection)

    frontend = Category('Front-End')
    backend = Category('Back-end')
    
    dao.save(frontend)
    dao.save(backend)

    connection.close()


def register_authors_database():
    
    connection = ConnectionDatabase.connect()

    authors = AuthorDao(connection)

    kessia_rod = Author('Késsia Rodrigues', 'kessia@kessia.com.br')
    lucas_souza = Author('Lucas Souza', 'lucas@lucas.com.br')

    authors.save(kessia_rod)
    authors.save(lucas_souza)

    connection.close()

def register_books_database():

    connection = ConnectionDatabase.connect()

    book_dao = BookDao(connection)

    javascript = Book(
        'JavaScript', 'Resumo '*80, 'Sumário do Livro',
        800, "978-85-08-13296-9", Author('Lucas Souza', 'lucas@lucas.com.br'),
        Category('Front-end'), 2, 120.56
    )

    flask = Book(
        'Flask', 'Resumo '*80, 'Sumário do Livro',
        700, "978-85-08-14196-9", Author('Késsia Rodrigues', 'kessia@kessia.com.br'),
        Category('Back-end'), 1, 220.56
    )

    book_dao.save(javascript)
    book_dao.save(flask)

    connection.close()


def register_sales():

    connection = ConnectionDatabase.connect()

    sales_dao = SaleDao(connection)
    
    book_1 = Book(
        'JavaScript', 'Resumo '*80, 'Sumário do Livro',
        800, "978-85-08-13296-9", Author('Lucas Souza', 'lucas@lucas.com.br'),
        Category('Front-end'), 2, 120.56
    )

    book_2 = Book(
        'Flask', 'Resumo '*80, 'Sumário do Livro',
        700, "978-85-08-14196-9", Author('Késsia Rodrigues', 'kessia@kessia.com.br'),
        Category('Back-end'), 1, 220.56
    )
    
    sale_book_1 = Sale(book_1, 2)
    sale_book_2 = Sale(book_2, 5)

    sales_dao.add(sale_book_1)
    sales_dao.add(sale_book_2)
    sales_dao.checkout()

    connection.close()

def search_books(title):

    connection = ConnectionDatabase.connect()

    book_dao = BookDao(connection)

    books_found = book_dao.find_many(title)
    print('---Resultados da pesquisa---')
    if books_found:
        for book in books_found:
            print(book)

    connection.close()


if __name__ == '__main__':
    
    register_authors_database()
    register_categories_database()
    register_books_database()
    search_books('Python')
    register_sales()
