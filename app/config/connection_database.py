from mysql.connector import connect, ProgrammingError
from contextlib import contextmanager


class ConnectionDatabase:

    def connect(self):
        configurations = {
            "host": 'localhost',
            "user": 'root',
            "password": 'root',
            "port": 3306,
            "database": 'edigi'
        }

        try:
            self.db = connect(**configurations)
            return self.db
        except ProgrammingError as error:
            print(f'Erro ao conectar: {error}')

    def cursor(self):
        cursor = self.db.cursor(dictionary=True, buffered=True)
        return cursor

    def close(self):
        self.db.close()
