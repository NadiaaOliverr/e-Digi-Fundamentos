from model import Category
from typing import List

class CategoryDao:
    """Banco de Dados de Categorias"""

    _list_categories: List[Category] = []

    def save(self, category: Category) -> None:
        if isinstance(category, Category):
            if category in self._list_categories:
                raise Exception('Esta categoria já consta na base de dados.')
            self._list_categories.append(category)
            print(f'\n---Categoria Cadastrada---\n{category}\n')
        else:
            raise Exception('O argumento passado não é do tipo Categoria')

    def all_categories(self) -> list:
        return self._list_categories.copy()
