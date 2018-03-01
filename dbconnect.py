import mysql.connector
from dbconfig import dbconf


class UseDatabase():
    """Диспетчер контекста для подключения к БД"""
    def __init__(self, dbconfig:dict=dbconf) -> None:
        self.dbconfig = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.dbconfig)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()