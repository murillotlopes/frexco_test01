from app.models import DatabaseConnector
from app.models import DatabaseCreator

from psycopg2 import sql
from psycopg2.errors import UndefinedColumn

from app.models.region_model import Region


class Fruit(DatabaseCreator):
    
    fruit_columns = ['id_fruit', 'name', 'region']

    def __init__(self, name: str, region: str):
        self.name = name.lower()
        self.id_region = Region.get_id_by_name(region.lower())


    @classmethod
    def serialize(cls, data: tuple):
        return dict(zip(cls.fruit_columns, data))

    @staticmethod
    def get_all_fruits():

        conn, cur = DatabaseConnector.get_conn_cur()

        query = """
            select f.id_fruit as id, f.name as name, r.name as region 
                from fruit as f 
                inner join region as r 
                on f.id_region = r.id_region
        """

        cur.execute(query)

        fruits_selected = cur.fetchall()

        DatabaseConnector.commit_and_close(conn, cur)

        return fruits_selected


    @staticmethod
    def get_fruit_by_id(id):

        conn, cur = DatabaseConnector.get_conn_cur()

        sql_id = sql.Literal(id)

        query = sql.SQL("""
            select f.id_fruit as id, f.name as name, r.name as region 
                from fruit as f 
                inner join region as r 
                on f.id_region = r.id_region
                WHERE id_fruit = {id}
        """).format(id = sql_id)
        
        cur.execute(query)

        fruit_selected = cur.fetchall()

        DatabaseConnector.commit_and_close(conn, cur)

        return fruit_selected

    
    def create_fruit(self):

        conn, cur = DatabaseConnector.get_conn_cur()

        values = tuple(self.__dict__.values())

        query = "INSERT INTO fruit (name, id_region) VALUES (%s, %s) RETURNING *"

        cur.execute(query, values)
 
        inserted_fruit = cur.fetchone()

        DatabaseConnector.commit_and_close(conn, cur)

        return inserted_fruit

    
    def update_by_id(id: str, payload: dict):

        conn, cur = DatabaseConnector.get_conn_cur()

        payload = {key: value.lower() for (key, value) in payload.items()}

        region_name = (payload.get('region'))
        id_region = Region.get_id_by_name(region_name)

        payload['id_region'] = id_region
        del payload['region']

        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]
        sql_id = sql.Literal(id)

        query = sql.SQL("""
            UPDATE fruit 
            SET
                ({columns}) = ROW({values})
            WHERE
                id_fruit = ({id})
            RETURNING *;
        """
        ).format(
            id = sql_id,
            columns = sql.SQL(",").join(columns),
            values = sql.SQL(",").join(values),
        )

        cur.execute(query)

        update_fruit = cur.fetchone()

        DatabaseConnector.commit_and_close(conn, cur)

        return update_fruit


    def delete_by_id(id):

        conn, cur = DatabaseConnector.get_conn_cur()

        sql_id = sql.Literal(id)

        query = sql.SQL('DELETE FROM fruit WHERE id_fruit = {id} RETURNING *').format(id = sql_id)

        cur.execute(query)

        deleted_fruit = cur.fetchone()

        print("=" * 50)
        print(deleted_fruit)
        print("=" * 50)

        DatabaseConnector.commit_and_close(conn, cur)

        return deleted_fruit




