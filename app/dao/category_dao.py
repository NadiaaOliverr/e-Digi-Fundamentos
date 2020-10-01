from app.helpers.decorators import is_not_null
from app.model.category import Category


class CategoryDao:
    """Banco de Dados de Categorias"""

    def __init__(self, db):
        self.db = db
        self._connection = self.db.connect()
        self._cursor = self.db.cursor()

    def save(self, category: Category) -> None:
        if not isinstance(category, Category):
            raise TypeError('O argumento passado não é do tipo Categoria')

        sql = 'INSERT INTO category(name) VALUES (%s)'
        args = (category.name_category, )

        self._cursor.execute(sql, args)
        self._connection.commit()
        print(f'--- Categoria inserida no banco ---\n{category}')
        

    
    @is_not_null
    def find_one(self, name_category: str) -> Category:
        sql = 'SELECT name FROM category WHERE name = %s'
        self._cursor.execute(sql, (name_category,))

        result_query = self._cursor.fetchone()

        if result_query:
            return Category(result_query['name'])
        
        raise KeyError(f'A categoria {name_category} não consta no acervo')
