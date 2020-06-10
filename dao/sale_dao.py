from model import Sale
from dao import BookDao
from typing import List
from datetime import datetime

class SaleDao:
    """Banco de Dados de Vendas
        Estrutura do banco: 
        (
            livro, 
            venda(titulo do livro, quantidade), 
            momento_do_cadastro
        )
    """

    _list_sales: List[Sale] = []
    _book_dao = BookDao()

    def save(self, books_sale: List[Sale]) -> None:
        self.book_exists(books_sale)
        self.sale_information()
    
    def book_exists(self, books_sale: List[Sale]) -> None:
        for sale in books_sale:
            books = self._book_dao.find_by_title(sale.title_book)
            for book in books:
                if sale.title_book == book.title:
                    self._list_sales.append((book, sale, datetime.now()))
        if not self._list_sales:
            raise Exception('Livro não consta em nosso acervo')

    def sale_information(self):
        print('--- Venda realizada com sucesso ---')
        for item in self._list_sales:
            book, sale, _ = item
            print(f'{sale} - Preço: {book.price}')
        print(f'Preço total: R$ {self.calculate_total():.2f}')

    def calculate_total(self) -> float:
        total = 0
        for item in self._list_sales:
            book, sale, _ = item
            total += book.price * sale.quantity_book
        return total