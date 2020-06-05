"""Executa as integrações entre model, dao e view."""

from model import Book, Category, Author
from dao import BookDao
from view import ViewBook

__author__ = "Nádia Oliveira"
__email__ = "nadiaaoliverr@gmail.com"
__status__ = "Em desenvolvimento"

class Controller:

    dao = BookDao()
    view = ViewBook()

    def insert_book(self, book: Book) -> None:
        self.dao.save(book)

    def show_books(self, title: str) -> None:
        items = self.dao.find_by_title(title)
        self.view.show_books(items)


def books_collections():

    controller = Controller()

    python_basico = Book(
        'Python Básico', 'Resumo '*80, 'Sumário do Livro',
        700, "978-85-08-22232-8", Author('Luciano Pereira', 'luciano@pereira.com.br'),
        Category('Programação'), "1234", 220.56
    )

    controller.insert_book(python_basico)

def search_book(title):
    controller = Controller()
    controller.show_books(title)

if __name__ == "__main__":
    
    books_collections()
    search_book('Ciências')

