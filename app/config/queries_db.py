from setup_db import Connection, ProgrammingError

database_edigi = """
    CREATE DATABASE IF NOT EXISTS edigi
"""

table_category = """
    CREATE TABLE IF NOT EXISTS category(
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL, 
        time_registration TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        UNIQUE KEY (name)
    )
"""

table_author = """
    CREATE TABLE IF NOT EXISTS author(
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL, 
        email VARCHAR(50) NOT NULL, 
        time_registration TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        UNIQUE KEY (email)
    )
"""

table_book = """
    CREATE TABLE IF NOT EXISTS book(
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        category_id INTEGER NOT NULL,
        author_id INTEGER NOT NULL,
        title VARCHAR(50) NOT NULL, 
        resume VARCHAR(800) NOT NULL, 
        summary VARCHAR(800) NOT NULL,  
        number_of_pages INTEGER UNSIGNED NOT NULL, 
        isbn VARCHAR(11) NOT NULL, 
        edition INTEGER UNSIGNED NOT NULL, 
        price FLOAT UNSIGNED NOT NULL,
        time_registration TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (category_id) REFERENCES category(id),
        FOREIGN KEY (author_id) REFERENCES author(id),
        UNIQUE KEY (isbn),
        UNIQUE KEY(title)
    )
"""

table_sale = """
    CREATE TABLE IF NOT EXISTS sale(
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        category_id INTEGER NOT NULL,
        author_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        quantity INTEGER UNSIGNED NOT NULL, 
        total FLOAT UNSIGNED NOT NULL,
        time_registration TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (category_id) REFERENCES category(id),
        FOREIGN KEY (author_id) REFERENCES author(id),
        FOREIGN KEY (book_id) REFERENCES book(id)
    )
"""

if __name__ == '__main__':

    try:
        db = Connection.connect()
        cursor = db.cursor()
        cursor.execute(database_edigi)
        cursor.execute(table_category)
        cursor.execute(table_author)
        cursor.execute(table_book)
        cursor.execute(table_sale)
        cursor.execute('SHOW TABLES')
        
        print('Tabelas criadas com sucesso!')
        for i, table in enumerate(cursor, start=1):
            print(f'Tabela {i}: {table[0]}')

    except ProgrammingError as e:
        print(f'Erro: {e.msg}')