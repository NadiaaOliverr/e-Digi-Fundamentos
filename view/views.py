class ViewBook:

    def show_books(self, items):
        if items:
            for item in items:
                print(item)
        else:
            print('Não há livros com esse prefixo em nosso acervo')
