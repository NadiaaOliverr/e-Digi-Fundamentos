"""Executa as classes de model e dao."""
from model import Book, Author, Category, Sale
from dao import BookDao, SaleDao

__author__ = "Nádia Oliveira"
__email__ = "nadiaaoliverr@gmail.com"
__status__ = "Em desenvolvimento"



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
    sales_dao.save([
        sale_book_1,
        sale_book_2
    ])


def search_books(title):

    book_dao = BookDao()

    books_found = book_dao.find_by_title(title)
    print('---Resultados da pesquisa---')
    if books_found:
        for book in books_found:
                print(book)
    else:
        print('Não há livros com esse prefixo em nosso acervo')

   
if __name__ == '__main__':

    register_books_database()
    register_sales()
