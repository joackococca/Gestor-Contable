import sqlite3

class Datab ():
    def __init__(self):
        self.con = sqlite3.connect("mibase.db")
        self.tabla()

    def tabla (self):
        cursor = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS gestor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            monto REAL NOT NULL,
            fecha TEXT NOT NULL,
            cliente TEXT NOT NULL,
            comprobante TEXT NOT NULL,
            estado TEXT NOT NULL,
            descripcion TEXT
        )
        """
        cursor.execute(sql)
        self.con.commit()

    def insertar (self, monto, fecha, cliente, comprobante, estado, descripcion=None):
        cursor = self.con.cursor()
        sql = "INSERT INTO gestor (monto, fecha, cliente, comprobante, estado, descripcion) VALUES (?, ?, ?, ?, ?, ?)"
        data = (monto, fecha, cliente, comprobante, estado, descripcion)
        cursor.execute(sql, data)
        self.con.commit()

    def borrar (self, mi_id):
        cursor = self.con.cursor()
        sql_check = "SELECT * FROM gestor WHERE id = ?"
        cursor.execute(sql_check, (mi_id,))
        if cursor.fetchone() is None:
            raise ValueError(f"No existe un registro con id {mi_id}")

        sql = "DELETE FROM gestor WHERE id = ?"  
        cursor.execute(sql, (mi_id,))
        self.con.commit()
    
    def consultar_todos(self):
        cursor = self.con.cursor()
        sql = "SELECT * FROM gestor ORDER BY id ASC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def consultar(self, fecha=None, comprobante=None, cliente=None, estado=None):
        if not (cliente or comprobante or fecha or estado):
            raise ValueError('Para consultar tiene que llenar al menos un campo')

        cursor = self.con.cursor()
        condiciones = []
        valores = []
        
        if cliente:
            condiciones.append("cliente LIKE ?")
            valores.append(f"%{cliente}%")
        
        if comprobante:
            condiciones.append("comprobante LIKE ?")
            valores.append(f"%{comprobante}%")
        
        if fecha:
            condiciones.append("fecha = ?")
            valores.append(fecha)

        if estado:
            condiciones.append('estado = ?')
            valores.append(estado)
        
        sql = "SELECT * FROM gestor"
        if condiciones:
            sql += " WHERE " + " AND ".join(condiciones)
        
        cursor.execute(sql, valores)
        return cursor.fetchall()
    
    def modificar(self, mi_id, monto, fecha, cliente, comprobante, estado, descripcion=None):
        if not (monto and fecha and cliente and comprobante and estado):
            raise ValueError('Debe seleccionar algun campo para poder modificar el registro')
        
        cursor = self.con.cursor()
        data=(monto, fecha, cliente, comprobante, estado, descripcion, mi_id)
        sql='UPDATE gestor SET monto=?, fecha=?, cliente=?, comprobante=?, estado=?, descripcion=? WHERE id=?'
        cursor.execute(sql, data)
        self.con.commit()
