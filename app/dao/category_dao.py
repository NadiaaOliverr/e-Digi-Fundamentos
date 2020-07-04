from app.helpers.decorators import is_not_null
from app.model.category import Category

from typing import List


class CategoryDao:
    """Banco de Dados de Categorias"""

    list_categories: List[Category] = []

    def save(self, category: Category) -> None:
        if not isinstance(category, Category):
            raise TypeError('O argumento passado não é do tipo Categoria')

        if category in self.list_categories:
            raise ValueError('Esta categoria já consta na base de dados.')

        self.list_categories.append(category)

        print(f'\n---Categoria Cadastrada---\n{category}')
    
    @is_not_null
    def find_one(self, name_category: str) -> Category:
        for category in self.list_categories:
            if name_category.lower() == category.name_category.lower():
                return category
        raise KeyError('Esta categoria não consta no acervo')

