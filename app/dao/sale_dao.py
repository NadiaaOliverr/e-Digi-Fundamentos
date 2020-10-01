from app.dao.book_dao import BookDao
from app.model.sale import Sale

from typing import List


class SaleDao:

    def __init__(self, db) -> None:
        self._sale: List = []
        self._id_book = []
        self.db = db
        self._connection = self.db.connect()
        self._cursor = self.db.cursor()


    def add(self, sale: Sale) -> None:
        if not isinstance(sale, Sale):
            raise TypeError('O argumento passado não é do tipo Sale')

        sql_book_exists = 'SELECT id FROM book WHERE title = %s'
        args = (sale.title_sale, )
        self._cursor.execute(sql_book_exists, args)
        result_query = self._cursor.fetchone()
        self._id_book.append(result_query)
        
        if not result_query:
            raise Exception('Impossível adicionar a venda, livro não consta na nossa base de dados')
        
        self._sale.append(sale)

    def checkout(self) -> None:
        sql = 'INSERT INTO sale(book_id, quantity, total) VALUES(%s, %s, %s)'
        total_sale = 0
        informations = '\n--- Venda realizada com sucesso ---\n'

        for index, item in enumerate(self._sale):
            total_sale += item.price_sale*item.quantity_sale
            args = (self._id_book[index]['id'], item.quantity_sale, total_sale)
            self._cursor.execute(sql, args)
            self._connection.commit()
            informations += str(item)

        informations += f'\nPreço total: R$ {total_sale:.2f}'
        
        print(informations)
