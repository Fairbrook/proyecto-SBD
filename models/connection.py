import psycopg2
import psycopg2.extras


class Connection:
    def __init__(self):
        self.DB_NAME = 'libreria'
        self.USER = 'postgres'
        self.PASSWORD = 'root'
        self.HOST = 'localhost'

    def query(self, query, params=None):
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.USER,
                                password=self.PASSWORD, host=self.HOST)
        result = []

        with conn:
            with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
                cur.execute(query, params)
                result = cur.fetchall()

        conn.close()
        return result

    def noQuery(self, query, params=None):
        conn = psycopg2.connect(dbname=self.DB_NAME, user=self.USER,
                                password=self.PASSWORD, host=self.HOST)
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, params)

        conn.close()
