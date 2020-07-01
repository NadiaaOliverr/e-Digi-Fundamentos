from dao import BookDao
import model.sale as class_sale
from typing import List


class SaleDao:

    list_sales: List['Sale'] = []

    def __init__(self) -> None:
        self._sale = []

    def add(self, sale: 'Sale') -> None:
        if not isinstance(sale, class_sale.Sale):
            raise TypeError('O argumento passado não é do tipo Sale')

        self._sale.append(sale)
        self.list_sales.append(sale)

    def checkout(self) -> str:
        informations = '\n--- Venda realizada com sucesso ---\n'
        total_sale = 0
        for item in self._sale:
            total_sale += item.price_book*item.quantity_sale
            informations += str(item)
        informations += f'\nPreço total: R$ {total_sale:.2f}'
        self._sale = []
        return informations
