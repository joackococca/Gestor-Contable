from modelo import Datab
objmodelo= Datab()

class Controlador():
    def alta_controlador(self, monto, fecha, cliente, comprobante, estado, descripcion=None):
        return objmodelo.insertar(monto, fecha, cliente, comprobante, estado, descripcion)
    
    def eliminar_controlador(self, mi_id):
        return objmodelo.borrar(mi_id)
    
    def consultar_controlador(self, fecha=None, comprobante=None, cliente=None, estado=None):
        return objmodelo.consultar(fecha=fecha, cliente=cliente, comprobante=comprobante, estado=estado)
    
    def consultar_todos_controlador(self, ):
        return objmodelo.consultar_todos()
    
    def modificar_controlador(self, mi_id,monto, fecha, cliente, comprobante, estado,descripcion=None):
        return objmodelo.modificar(mi_id, monto, fecha, cliente, comprobante, estado, descripcion)