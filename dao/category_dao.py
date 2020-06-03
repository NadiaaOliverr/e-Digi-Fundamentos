from model import Category
from typing import List

class CategoryDao:
    """Banco de Dados de Categorias"""

    _list_categories: List[Category] = []

    def add_category(self, category: Category) -> None:
        if category in self._list_categories:
            raise Exception('Esta categoria já consta na base de dados.')
        self._list_categories.append(category)
        print(f'\n---Categoria Cadastrada---\n{category}\n')

    def all_categories(self) -> list:
        return self._list_categories.copy()
