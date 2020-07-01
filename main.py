"""Executa as classes de model e dao."""
from app.model.author import Author
from app.model.book import Book
from app.model.category import Category
from app.model.sale import Sale
from app.dao.book_dao import BookDao
from app.dao.sale_dao import SaleDao
from app.dao.category_dao import CategoryDao
from app.dao.author_dao import AuthorDao



__author__ = "Nádia Oliveira"
__email__ = "nadiaaoliverr@gmail.com"
__status__ = "Em desenvolvimento"


def register_categories_database():
    
    dao = CategoryDao()

    programming = Category('Programação')
    ciencias = Category('Ciências')
    
    dao.save(programming)
    dao.save(ciencias)


def register_authors_database():
    
    authors = AuthorDao()

    luciano_ramalho = Author('Luciano Ramalho', 'luciano@luciano.com.br')
    luciano_pereira = Author('Luciano Pereira', 'luciano@pereira.com.br')

    authors.save(luciano_ramalho)
    authors.save(luciano_pereira)

def register_books_database():

    book_dao = BookDao()

    python_fluente = Book(
        'Python Fluente', 'Resumo '*80, 'Sumário do Livro',
        800, "978-85-08-13196-9", Author('Luciano Ramalho', 'luciano@luciano.com.br'),
        Category('Programação'), "1254", 120.56
    )

    ciencias_basica = Book(
        'Ciências Básica', 'Resumo '*80, 'Sumário do Livro',
        700, "978-85-08-22232-8", Author('Luciano Pereira', 'luciano@pereira.com.br'),
        Category('Ciências'), "1234", 220.56
    )

    book_dao.save(python_fluente)
    book_dao.save(ciencias_basica)


def register_sales():

    book_1 = 'Ciências Básica'

    book_2 = 'Python Fluente'

    
    sale_book_1 = Sale(book_1, 2)
    sale_book_2 = Sale(book_2, 5)


    sales_dao = SaleDao()
    sales_dao.add(sale_book_1)
    sales_dao.add(sale_book_2)
    sales_dao.checkout()

def search_books(title):

    book_dao = BookDao()

    books_found = book_dao.find_many(title)
    print('---Resultados da pesquisa---')
    if books_found:
        for book in books_found:
            print(book)
    else:
        print('Não há livros com esse prefixo em nosso acervo')

   
if __name__ == '__main__':
    
    register_authors_database()
    register_categories_database()
    register_books_database()
    register_sales()
