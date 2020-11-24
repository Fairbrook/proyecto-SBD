import psycopg2
import psycopg2.extras
import threading
import select


class Connection:
    def __init__(self):
        self.DB_NAME = 'libreria'
        self.USER = 'postgres'
        self.PASSWORD = 'root'
        self.HOST = 'localhost'
        self.threads = []
        self.event = threading.Event()

    def connect(self):
        return psycopg2.connect(dbname=self.DB_NAME, user=self.USER,
                                password=self.PASSWORD, host=self.HOST)

    def query(self, query, params=None):
        conn = self.connect()
        result = []

        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(query, params)
                result = cur.fetchall()

        conn.close()
        return result

    def noQuery(self, query, params=None):
        conn = self.connect()
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, params)

        conn.close()
