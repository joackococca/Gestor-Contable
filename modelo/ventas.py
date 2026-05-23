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
            comprobante TEXT NOT NULL,
            nombre TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descripcion TEXT
        )
        """
        cursor.execute(sql)
        self.con.commit()

    def insertar (self, monto, fecha, comprobante, nombre, tipo, descripcion=None):
        cursor = self.con.cursor()
        sql = "INSERT INTO gestor (monto, fecha, comprobante, nombre, tipo, descripcion) VALUES (?, ?, ?, ?, ?, ?)"
        data = (monto, fecha, comprobante, nombre, tipo, descripcion)
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
    
    def consultar(self, nombre=None, comprobante=None, fecha=None, tipo=None):
        if not nombre or comprobante or fecha or tipo:
            raise ValueError('Para consultar tiene que llenar al menos un campo')

        cursor = self.con.cursor()
        condiciones = []
        valores = []
        
        if nombre:
            condiciones.append("nombre LIKE ?")
            valores.append(f"%{nombre}%")
        
        if comprobante:
            condiciones.append("comprobante LIKE ?")
            valores.append(f"%{comprobante}%")
        
        if fecha:
            condiciones.append("fecha = ?")
            valores.append(fecha)

        if tipo:
            condiciones.append('tipo = ?')
            valores.append(tipo)
        
        sql = "SELECT * FROM gestor"
        if condiciones:
            sql += " WHERE " + " AND ".join(condiciones)
        
        cursor.execute(sql, valores)
        return cursor.fetchall()
    
    def modificar(self, mi_id, monto=None, fecha=None, comprobante=None, nombre=None, descripcion=None, tipo=None):
        if not monto or fecha or comprobante or nombre or descripcion or tipo:
            raise ValueError('Debe seleccionar algun campo para poder seleccionarlo')

        cursor = self.con.cursor()
        data=(monto, fecha, comprobante, nombre, descripcion, mi_id)
        sql='UPDATE gestor SET monto=?, fecha=?, comprobante=?, nombre=?, descripcion=?, tipo=? WHERE id=?'
        cursor.execute(sql, data)
        self.con.commit()

    def actualizar_estado(self, tipo, mi_id):
        if not tipo:
            raise ValueError('Debe especificar el tipo de registro para actualizar')
        
        if tipo == 'Gasto':
            raise ValueError('Un gasto no tiene una actualizacion de estado')
        
        cursor = self.con.cursor()
        data = (tipo, mi_id)
        sql='UPDATE gestor SET tipo=? WHERE id?'
        cursor.execute(sql, data)
        self.con.commit