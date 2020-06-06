"""Executa as classes de model e dao."""
from model import Book, Author, Category
from dao import BookDao

__author__ = "Nádia Oliveira"
__email__ = "nadiaaoliverr@gmail.com"
__status__ = "Em desenvolvimento"


def start():
    dao = BookDao()

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

    dao.save(python_fluente)
    dao.save(ciencias_basica)

    books_found = dao.find_by_title('py')
    print('---Resultados da pesquisa---')
    if books_found:
        for book in books_found:
                print(book)
    else:
        print('Não há livros com esse prefixo em nosso acervo')

if __name__ == '__main__':

    start()