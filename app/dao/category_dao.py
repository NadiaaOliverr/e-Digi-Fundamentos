from app.helpers.decorators import is_not_null
from app.model.category import Category
from app.config.connection_database import ConnectionDatabase

from typing import List


class CategoryDao:
    """Banco de Dados de Categorias"""

    def __init__(self):
        self.connection = ConnectionDatabase.connect()
        self.db = self.connection.cursor(dictionary=True)

    def save(self, category: Category) -> None:
        if not isinstance(category, Category):
            raise TypeError('O argumento passado não é do tipo Categoria')

        sql = 'INSERT INTO category(name) VALUES (%s)'
        args = (category.name_category, )
        
        self.db.execute(sql, args)
        self.connection.commit()

        print(f'--- Categoria inserida no banco ---\n{category}')

    
    @is_not_null
    def find_one(self, name_category: str) -> Category:
        sql = 'SELECT name FROM category WHERE name = %s'
        self.db.execute(sql, (name_category,))

        result_query = self.db.fetchone()

        if result_query:
            return Category(result_query['name'])
        
        raise KeyError(f'A categoria {name_category} não consta no acervo')

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

