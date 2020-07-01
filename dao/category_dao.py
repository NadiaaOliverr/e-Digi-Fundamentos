from model import Category
from typing import List


class CategoryDao:
    """Banco de Dados de Categorias"""

    list_categories: List[Category] = []

    def save(self, category: Category) -> str:
        if not isinstance(category, Category):
            raise TypeError('O argumento passado não é do tipo Categoria')

        if category in self.list_categories:
            raise ValueError('Esta categoria já consta na base de dados.')

        self.list_categories.append(category)

        return category
