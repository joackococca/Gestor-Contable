from modelo import Datab
objmodelo= Datab()

class Controlador():
    def alta_controlador(self, monto, fecha, comprobante, nombre, tipo, descripcion=None):
        return objmodelo.insertar(monto, fecha, comprobante, nombre, tipo, descripcion)
    
    def eliminar_controlador(self, mi_id):
        return objmodelo.borrar(mi_id)
    
    def consultar_controlador(self, fecha=None, comprobante=None, nombre=None, tipo=None):
        return objmodelo.consultar(fecha, comprobante, nombre, tipo)
    
    def consultar_todos_controlador(self, ):
        return objmodelo.consultar_todos()
    
    def modificar_controlador(self, mi_id, monto=None, fecha=None, comprobante=None, nombre=None, descripcion=None, tipo=None):
        return objmodelo.modificar(mi_id, monto, fecha, comprobante, nombre, descripcion, tipo)