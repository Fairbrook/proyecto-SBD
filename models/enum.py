from .connection import Connection


class Enum:
    def __init__(self):
        self.conn = Connection()

    def getAll(self):
        return self.conn.query("""
        select enumlabel as label from pg_enum 
        inner join pg_type on pg_type.oid = enumtypid 
        where typname = 'tipo_empleado'
        """)
