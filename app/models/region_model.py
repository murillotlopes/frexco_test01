from importlib import import_module
from app.models import DatabaseConnector
from psycopg2 import sql

class Region:

    region_columns = ['id_region', 'name']


    def __init__(self, name:str):
        self.name = name.lower().strip()

    
    @classmethod
    def serialize(cls, data: tuple):
        return dict(zip(cls.region_columns, data))


    @staticmethod
    def get_id_by_name(name):

        conn, cur = DatabaseConnector.get_conn_cur()

        sql_name = sql.Literal(name)

        query = sql.SQL("""
            select id_region from region WHERE name = {name} AND status = true
        """).format(name = sql_name)
        
        cur.execute(query)

        id_selected = cur.fetchall()

        DatabaseConnector.commit_and_close(conn, cur)

        try:
            return list(id_selected[0])[0]
        except:
            return False

        


    def create_region(self):

        conn, cur = DatabaseConnector.get_conn_cur()

        values = tuple(self.__dict__.values())

        query = "INSERT INTO region (name) VALUES (%s) RETURNING *"

        cur.execute(query, values)

        inserted_region = cur.fetchone()

        DatabaseConnector.commit_and_close(conn, cur)

        return inserted_region
    
    @staticmethod
    def read_all_region():

        conn, cur = DatabaseConnector.get_conn_cur()

        query = "SELECT * FROM region WHERE status = true;"

        cur.execute(query)

        region_selected = cur.fetchall()

        DatabaseConnector.commit_and_close(conn, cur)

        return region_selected

    
    @staticmethod
    def read_region_by_id(id):

        conn, cur = DatabaseConnector.get_conn_cur()

        sql_id = sql.Literal(id)

        query = sql.SQL("SELECT * FROM region WHERE id_region = {id} AND status = true").format(id = sql_id)

        cur.execute(query)

        region_selected = cur.fetchall()

        DatabaseConnector.commit_and_close(conn, cur)

        return region_selected

    
    def update_by_id(id: str, payload: dict):

        conn, cur = DatabaseConnector.get_conn_cur()

        payload = {key: value.lower() for (key, value) in payload.items()}

        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(values) for values in payload.values()]
        sql_id = sql.Literal(id)

        query = sql.SQL("""
            UPDATE region
            SET
                ({columns}) = ROW({values})
            WHERE
                id_region = ({id})
            RETURNING *;
        """).format(
            id = sql_id,
            columns = sql.SQL(',').join(columns),
            values = sql.SQL(',').join(values),
        )

        cur.execute(query)

        update_region = cur.fetchone()

        DatabaseConnector.commit_and_close(conn, cur)

        return update_region

    
    def inactivate_by_id(id):

        conn, cur = DatabaseConnector.get_conn_cur()

        sql_id = sql.Literal(id)

        query = sql.SQL("""
            UPDATE region
            SET status = false
            WHERE id_region = ({id})
            RETURNING *
        """).format(id = sql_id)

        cur.execute(query)

        inactivated = cur.fetchone()

        DatabaseConnector.commit_and_close(conn, cur)

        return inactivated
