from mysql.connector import connect, ProgrammingError

class Connection:

    @staticmethod
    def connect():
        configurations = {
            "host": 'localhost',
            "user": 'root',
            "password": 'root',
            "port": 3306,
            "database": 'edigi'
        }

        try:
            db = connect(**configurations)
            return db
        except ProgrammingError as error:
            print(f'Erro ao conectar: {error}')
