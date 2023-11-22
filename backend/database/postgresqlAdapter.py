import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

class PostgreSQLAdapter:
    def __init__(self, dbname, user, password, host='localhost', port='5432'):
        self.connection_parameters = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.connection_parameters)
        except psycopg2.DatabaseError as e:
            print(f"Database connection failed: {e}")
            raise e

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None, commit=False, fetch_one=False, fetch_all=False):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            if commit:
                self.connection.commit()
            if fetch_one:
                return cursor.fetchone()
            if fetch_all:
                return cursor.fetchall()

    def create_character(self, character_data):
        query = sql.SQL("""
            INSERT INTO characters ({fields}) VALUES ({values})
            RETURNING id;
        """).format(
            fields=sql.SQL(', ').join(map(sql.Identifier, character_data.keys())),
            values=sql.SQL(', ').join(map(sql.Placeholder, character_data.keys()))
        )
        return self.execute_query(query, character_data, commit=True, fetch_one=True)

    def update_character(self, character_id, character_data):
        assignments = [sql.SQL("{} = {}").format(sql.Identifier(k), sql.Placeholder(k)) for k in character_data.keys()]
        query = sql.SQL("""
            UPDATE characters SET {assignments} WHERE id = %(character_id)s;
        """).format(assignments=sql.SQL(', ').join(assignments))
        params = {'character_id': character_id, **character_data}
        self.execute_query(query, params, commit=True)

    def get_character(self, character_id):
        query = "SELECT * FROM characters WHERE id = %s;"
        return self.execute_query(query, (character_id,), fetch_one=True)

    def delete_character(self, character_id):
        query = "DELETE FROM characters WHERE id = %s;"
        self.execute_query(query, (character_id,), commit=True)

    def create_game_history_entry(self, history_data):
        query = sql.SQL("""
            INSERT INTO game_history ({fields}) VALUES ({values})
            RETURNING id;
        """).format(
            fields=sql.SQL(', ').join(map(sql.Identifier, history_data.keys())),
            values=sql.SQL(', ').join(map(sql.Placeholder, history_data.keys()))
        )
        return self.execute_query(query, history_data, commit=True, fetch_one=True)

    def get_game_history(self, player_id):
        query = "SELECT * FROM game_history WHERE player_id = %s;"
        return self.execute_query(query, (player_id,), fetch_all=True)

    def update_campaign_settings(self, campaign_id, settings_data):
        assignments = [sql.SQL("{} = {}").format(sql.Identifier(k), sql.Placeholder(k)) for k in settings_data.keys()]
        query = sql.SQL("""
            UPDATE campaign_settings SET {assignments} WHERE id = %(campaign_id)s;
        """).format(assignments=sql.SQL(', ').join(assignments))
        params = {'campaign_id': campaign_id, **settings_data}
        self.execute_query(query, params, commit=True)

    def get_campaign_settings(self, campaign_id):
        query = "SELECT * FROM campaign_settings WHERE id = %s;"
        return self.execute_query(query, (campaign_id,), fetch_one=True)

# Example usage:
# adapter = PostgreSQLAdapter('dnd_db', 'user', 'password')
# adapter.connect()
# character = adapter.create_character({'name': 'Aragorn', 'strength': 18, 'intelligence': 12})
# print(character)
# adapter.close()