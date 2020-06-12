from dao import BookDao
from typing import List
from datetime import datetime

class SaleDao:

    list_sales: List['Sale'] = []

    def __init__(self) -> None:
        self._sale = []

    def add(self, sale: 'Sale') -> None:
        "Adiciona a venda. É similar ao insert do banco"
        self._sale.append(sale)
        self.list_sales.append(sale)
    
    def save(self):
        "Salva a venda, enviando para o banco."
        self.__print_sale_information()
    
    def __print_sale_information(self):
        "Printa as informações do banco. É similar a um select * com um sum"
        print('--- Venda realizada com sucesso ---')
        total_sale = 0
        for item in self._sale:
            total_sale += item.price_book*item.quantity_sale
            print(item)
        print(f'Preço total: R$ {total_sale:.2f}')
        self._sale = []