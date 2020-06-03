"""Executa as classes de model e dao."""

from model import Author
from dao import AuthorDao

__author__ = "Nádia Oliveira"
__email__ = "nadiaaoliverr@gmail.com"
__status__ = "Em desenvolvimento"


def start():
    authors = AuthorDao()

    author_machado = Author('Machado de Assis', 'machado@assis.com.br')
    author_clarice = Author('Clarice Lispector', 'clarice@lispector.com.br')

    authors.add_author(author_machado)
    authors.add_author(author_clarice)


if __name__ == '__main__':

    start()
