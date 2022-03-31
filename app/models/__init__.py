import psycopg2
import os


configs = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

class DatabaseConnector:

    @staticmethod
    def get_conn_cur():

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        return conn, cur

    
    @staticmethod
    def commit_and_close(conn, cur):
        conn.commit()
        cur.close()
        conn.close()


class DatabaseCreator():

    @staticmethod
    def create_table(table_name, table_column):

        conn, cur = DatabaseConnector.get_conn_cur()

        query = f'CREATE TABLE IF NOT EXISTS {table_name} ({table_column})'

        cur.execute(query)

        DatabaseConnector.commit_and_close(conn, cur)

