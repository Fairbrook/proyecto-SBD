import threading
import select
from PySide2 import QtCore, QtGui
import psycopg2
import psycopg2.extras
from models.connection import Connection


class Worker(QtCore.QObject):
    def __init__(self, app, channel):
        super(Worker, self).__init__()
        self.app = app
        conn = Connection().connect()
        conn.set_isolation_level(
            psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(f'Listen {channel};')
        self.conn = conn


    def _listener(self):
        while self.app.exit == False:
            if select.select([self.conn], [], [], 1) != ([], [], []):
                self.conn.poll()
                while self.conn.notifies:
                    notify = self.conn.notifies.pop(0)
                    print(notify.payload)
                    self.app.showMessageBox.emit(notify.payload)
        self.conn.close()
        print('connection close')
        self.app.exitThread.emit()
