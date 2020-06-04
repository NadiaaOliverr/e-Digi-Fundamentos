"""Executa as classes de model e dao."""

from model import Category
from dao import CategoryDao

__author__ = "Nádia Oliveira"
__email__ = "nadiaaoliverr@gmail.com"
__status__ = "Em desenvolvimento"


def start():
    dao = CategoryDao()

    romance = Category('Romance')
    aventura = Category('Aventura')
    
    dao.save(romance)
    dao.save(aventura)


if __name__ == '__main__':

    start()
