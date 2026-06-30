from tkinter import ttk, Tk
import tkinter as tk
from controlador import Controlador 
from Vista.ventas import SeccionVentas

class Ventana():

    def __init__(self):
        ven = Tk()
        ven.title("Gestor Contable")
        ven.geometry("1125x400")

        self.objcont= Controlador()

        self.notebook= ttk.Notebook(ven)
        self.notebook.grid(row=0, column=0, padx=10)

        self.vistas= {}

        tab_compras=ttk.Frame(self.notebook)

        tab_ventas=ttk.Frame(self.notebook)
        self.seccion_ventas_tab= SeccionVentas(tab_ventas, self.objcont)
        self.vistas[1]= self.seccion_ventas_tab

        tab_gastos=ttk.Frame(self.notebook)

        tab_resumen=ttk.Frame(self.notebook)
        tab_buscador=ttk.Frame(self.notebook)
        
        menu = tk.Menu(ven)
        ven.config(menu=menu)

        filemenu = tk.Menu(menu)
        menu.add_cascade(label="Herramientas", menu=filemenu)
        filemenu.add_command(label="Modificar", command=lambda:self.ejecutar_modificacion())
        filemenu.add_command(label="Borrar", command=lambda:self.borrar_vista())
        filemenu.add_separator()

        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Ayuda", menu=helpmenu)
        helpmenu.add_command(label="Tutorial")

        self.notebook.add(tab_compras, text="Compras")
        self.notebook.add(tab_ventas, text="Ventas")
        self.notebook.add(tab_gastos, text="Gastos")
        self.notebook.add(tab_resumen, text="Resumen")
        self.notebook.add(tab_buscador, text="Buscador")

        ven.mainloop()

    def ejecutar_modificacion(self):
            # A. Obtener el índice de la pestaña seleccionada
            indice_actual = self.notebook.index("current")

            # C. Verificar si tenemos una instancia guardada para ese índice
            if indice_actual in self.vistas:
                vista_activa = self.vistas[indice_actual]
                
                # D. Llamar al método específico de esa instancia
                # Asumimos que todas las clases tienen el método 'modificar_registro'
                if hasattr(vista_activa, 'modificar_tree'):
                    vista_activa.modificar_tree()
                else:
                    print("La vista actual no tiene el método 'modificar_tree'")
            else:
                print("No se encontró una vista válida para esta pestaña")