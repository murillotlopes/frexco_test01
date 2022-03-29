import psycopg2
import os

host = os.getenv('DB_HOST'),
database = os.getenv('DB_NAME'),
user = os.getenv('DB_USER'),
password = os.getenv('DB_PASSWORD')


config = {
    'host': host,
    'database': database,
    'user': user,
    'password': password
}

class DatabaseConnector:

    @staticmethod
    def get_conn_cur():
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        return conn, cur

    
    @staticmethod
    def commit_and_close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


class DatabaseCreator():

    con, cur = DatabaseConnector.get_conn_cur()

    @staticmethod
    def create_database(self):

        query = f'CREATE DATABASE IF NOT EXISTS {database}'

        self.cur.execute(query)

        DatabaseConnector.commit_and_close()

    
    @staticmethod
    def create_table(self, table_name, table_column):

        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({table_column})'

        self.cur.execute(query)

        DatabaseConnector.commit_and_close()

