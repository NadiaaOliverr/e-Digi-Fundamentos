from connection_database import ConnectionDatabase, ProgrammingError

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
        title VARCHAR(50) NOT NULL UNIQUE KEY, 
        resume VARCHAR(800) NOT NULL, 
        summary VARCHAR(800) NOT NULL,  
        number_of_pages INTEGER UNSIGNED NOT NULL, 
        isbn VARCHAR(17) NOT NULL UNIQUE KEY, 
        edition INTEGER UNSIGNED NOT NULL, 
        price FLOAT UNSIGNED NOT NULL,
        time_registration TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (category_id) REFERENCES category(id),
        FOREIGN KEY (author_id) REFERENCES author(id)
        ON DELETE CASCADE
    )
"""

table_sale = """
    CREATE TABLE IF NOT EXISTS sale(
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        book_id INTEGER NOT NULL,
        quantity INTEGER UNSIGNED NOT NULL, 
        total FLOAT UNSIGNED NOT NULL,
        time_registration TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (book_id) REFERENCES book(id)
        ON DELETE CASCADE
    )
"""

if __name__ == '__main__':

    try:
        db = ConnectionDatabase.connect()
        cursor = db.cursor()
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