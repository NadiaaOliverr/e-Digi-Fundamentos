"""Executa as classes de model e dao."""

from model import Category
from dao import CategoryDao

__author__ = "Nádia Oliveira"
__email__ = "nadiaaoliverr@gmail.com"
__status__ = "Em desenvolvimento"


def start():
    categories = CategoryDao()

    category_romance = Category('Romance')
    category_aventura = Category('Aventura')

    categories.add_category(category_romance)
    categories.add_category(category_aventura)


if __name__ == '__main__':

    start()
