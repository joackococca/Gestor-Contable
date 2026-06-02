import tkinter as tk
from tkinter import Tk, W
from tkinter import ttk
from controlador import Controlador
objcont= Controlador()


class Ventana():
    def __init__(self):
        ven = Tk()
        ven.title("Gestor Contable")
        ven.geometry("1050x400")

        notebook= ttk.Notebook(ven)
        notebook.grid(row=0, column=0, padx=10)

        tab_compras=ttk.Frame(notebook)
        tab_ventas=ttk.Frame(notebook)
        tab_gastos=ttk.Frame(notebook)
        tab_resumen=ttk.Frame(notebook)

        notebook.add(tab_compras, text="Compras")
        notebook.add(tab_ventas, text="Ventas")
        notebook.add(tab_gastos, text="Gastos")
        notebook.add(tab_resumen, text="Resumen")

        #################################################################
        ###################### R E S U M E N ############################


        '''
        #################################################################
        ###################### G A S T O S ##############################

        fr_new_registro_gastos= tk.Frame(tab_gastos, width=250, height=320, bd=2, relief="groove")
        fr_registro_gastos= tk.Frame(tab_gastos, width=250, height=350, bd=2, relief="groove")
        fr_new_registro_gastos.grid(row=0, column=0)
        fr_registro_gastos.grid(row=0, column=1)

        fr_new_registro_gastos.grid_propagate(False)

        label_titulo_g=tk.Label(fr_new_registro_gastos, text="NUEVO REGISTRO")
        label_monto_g=tk.Label(fr_new_registro_gastos, text="Monto ($)")
        label_fecha_g=tk.Label(fr_new_registro_gastos, text="Fecha")
        label_descripcion_g=tk.Label(fr_new_registro_gastos, text="Descripcion")
        label_estado_g=tk.Label(fr_new_registro_gastos, text="Estado")

        label_titulo_g.grid(row=0, column=1, padx=50, pady=5)
        label_monto_g.grid(row=1, column=1, padx=50, pady=5)
        label_fecha_g.grid(row=3, column=1, padx=50, pady=5)
        label_descripcion_g.grid(row=5, column=1, padx=50, pady=5)

        entry_a=tk.Entry(fr_new_registro_gastos).grid(row=2, column=1, padx=50, pady=5)
        entry_b=tk.Entry(fr_new_registro_gastos).grid(row=4, column=1, padx=50, pady=5)
        entry_d=tk.Entry(fr_new_registro_gastos).grid(row=6, column=1, padx=50, pady=5)

        tk.Button(fr_new_registro_gastos, text="+ Guardar Gasto").grid(row=13, column=1, padx=50, pady=5)

        ###################################################################
        ###################### C O M P R A S ##############################

        fr_new_registro_compras= tk.Frame(tab_compras, width=250, height=320, bd=2, relief="groove")
        fr_registro_compras= tk.Frame(tab_compras, width=250, height=350, bd=2, relief="groove")
        fr_new_registro_compras.grid(row=0, column=0 )
        fr_registro_compras.grid(row=0, column=1 )

        fr_new_registro_compras.grid_propagate(False)

        notebook_compras=ttk.Notebook(fr_registro_compras)
        notebook_compras.grid(row=1, column=0, padx=10)

        tab_pagado=ttk.Frame(notebook_compras)
        tab_pendiente=ttk.Frame(notebook_compras)
        tab_todos=ttk.Frame(notebook_compras)

        notebook_compras.add(tab_todos, text="Todos")
        notebook_compras.add(tab_pendiente, text="Pendiente")
        notebook_compras.add(tab_pagado, text="Pagado")

        label_registro_c=tk.Label(fr_registro_compras, text="REGISTRO")

        label_titulo_c=tk.Label(fr_new_registro_compras, text="NUEVO REGISTRO")
        label_monto_c=tk.Label(fr_new_registro_compras, text="Monto ($)")
        label_fecha_c=tk.Label(fr_new_registro_compras, text="Fecha")
        label_cliente_c=tk.Label(fr_new_registro_compras, text="Cliente")
        label_descripcion_c=tk.Label(fr_new_registro_compras, text="Descripcion")
        label_comprobante_c=tk.Label(fr_new_registro_compras, text="Comprobante N°")
        label_estado_c=tk.Label(fr_new_registro_compras, text="Estado")

        label_registro_c.grid(row=0, column=0)

        label_titulo_c.grid(row=0, column=1)
        label_monto_c.grid(row=1, column=1)
        label_fecha_c.grid(row=3, column=1)
        label_cliente_c.grid(row=5, column=1)
        label_descripcion_c.grid(row=7, column=1)
        label_comprobante_c.grid(row=9, column=1)
        label_estado_c.grid(row=11, column=1)

        entry_a_c=tk.Entry(fr_new_registro_compras).grid(row=2, column=1)
        entry_b_c=tk.Entry(fr_new_registro_compras).grid(row=4, column=1)
        entry_c_c=tk.Entry(fr_new_registro_compras).grid(row=6, column=1)
        entry_d_c=tk.Entry(fr_new_registro_compras).grid(row=8, column=1)
        entry_e_c=tk.Entry(fr_new_registro_compras).grid(row=10, column=1)

        tk.Button(fr_new_registro_compras, text="Pagado").grid(row=12, column=0)
        tk.Button(fr_new_registro_compras, text="Pendiente").grid(row=12, column=2)
        tk.Button(fr_new_registro_compras, text="+ Guardar compra").grid(row=13, column=1)
        '''
        ###################################################################
        ###################### V E N T A S ################################

        fr_new_registro_ventas= tk.Frame(tab_ventas, width=250, height=330, bd=2, relief="groove")
        fr_registro_ventas= tk.Frame(tab_ventas, width=750, height=330, bd=2, relief="groove")
        fr_new_registro_ventas.grid(row=0, column=0 )
        fr_registro_ventas.grid(row=0, column=1)

        fr_new_registro_ventas.grid_propagate(False)
        fr_registro_ventas.grid_propagate(False)

        notebook_ventas=ttk.Notebook(fr_registro_ventas)
        notebook_ventas.grid(row=1, column=0, padx=50)

        tab_cobrado=ttk.Frame(notebook_ventas)
        tab_pendiente_v=ttk.Frame(notebook_ventas)
        tab_todos_v=ttk.Frame(notebook_ventas)

        notebook_ventas.add(tab_todos_v, text="Todos")
        notebook_ventas.add(tab_pendiente_v, text="Pendiente")
        notebook_ventas.add(tab_cobrado, text="Cobrado")

        label_registro_v=tk.Label(fr_registro_ventas, text="REGISTRO", font=("Arial", 10, "bold"))

        label_titulo_v=tk.Label(fr_new_registro_ventas, text="NUEVO REGISTRO", font=("Arial", 10, "bold"))
        label_monto_v=tk.Label(fr_new_registro_ventas, text="Monto ($)")
        label_fecha_v=tk.Label(fr_new_registro_ventas, text="Fecha")
        label_cliente_v=tk.Label(fr_new_registro_ventas, text="Cliente")
        label_descripcion_v=tk.Label(fr_new_registro_ventas, text="Descripcion")
        label_comprobante_v=tk.Label(fr_new_registro_ventas, text="Comprobante N°")
        label_estado_v=tk.Label(fr_new_registro_ventas, text="Estado")

        label_registro_v.grid(row=0, column=0)

        label_titulo_v.grid(row=0, column=1, padx=58)
        label_monto_v.grid(row=1, column=1)
        label_fecha_v.grid(row=3, column=1)
        label_cliente_v.grid(row=5, column=1)
        label_descripcion_v.grid(row=7, column=1)
        label_comprobante_v.grid(row=9, column=1)
        label_estado_v.grid(row=11, column=1)

        entry_a_v=tk.Entry(fr_new_registro_ventas).grid(row=2, column=1, ipadx=30)
        entry_b_v=tk.Entry(fr_new_registro_ventas).grid(row=4, column=1, ipadx=30)
        entry_c_v=tk.Entry(fr_new_registro_ventas).grid(row=6, column=1, ipadx=30)
        entry_d_v=tk.Entry(fr_new_registro_ventas).grid(row=8, column=1, ipadx=30)
        entry_e_v=tk.Entry(fr_new_registro_ventas).grid(row=10, column=1, ipadx=30)

        v = tk.IntVar()
        tk.Radiobutton(fr_new_registro_ventas, text="Cobrado", variable=v, value=1).grid(row=12, column=1)
        tk.Radiobutton(fr_new_registro_ventas, text="Pendiente", variable=v, value=2).grid(row=13, column=1)
        tk.Button(fr_new_registro_ventas, text="+ Guardar Venta").grid(row=14, column=1)

        self.tree_ventas_todos= ttk.Treeview(tab_todos_v)
        self.tree_ventas_todos["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
        self.tree_ventas_todos.column("#0", width=50, anchor=W)
        self.tree_ventas_todos.column("col1", width=100)
        self.tree_ventas_todos.column("col2", width=100)
        self.tree_ventas_todos.column("col3", width=100)
        self.tree_ventas_todos.column("col4", width=100)
        self.tree_ventas_todos.column("col5", width=100)
        self.tree_ventas_todos.column("col6", width=100)
        self.tree_ventas_todos.heading("#0", text="ID")
        self.tree_ventas_todos.heading("col1", text="Cliente")
        self.tree_ventas_todos.heading("col2", text="Descripcion")
        self.tree_ventas_todos.heading("col3", text="Fecha")
        self.tree_ventas_todos.heading("col4", text="Comprobante")
        self.tree_ventas_todos.heading("col5", text="Monto")
        self.tree_ventas_todos.heading("col6", text="Estado")
        self.tree_ventas_todos.grid(row=0, column=0, ipady=10)


        self.tree_ventas_pendiente= ttk.Treeview(tab_pendiente_v)
        self.tree_ventas_pendiente["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
        self.tree_ventas_pendiente.column("#0", width=50, anchor=W)
        self.tree_ventas_pendiente.column("col1", width=100)
        self.tree_ventas_pendiente.column("col2", width=100)
        self.tree_ventas_pendiente.column("col3", width=100)
        self.tree_ventas_pendiente.column("col4", width=100)
        self.tree_ventas_pendiente.column("col5", width=100)
        self.tree_ventas_pendiente.column("col6", width=100)
        self.tree_ventas_pendiente.heading("#0", text="ID")
        self.tree_ventas_pendiente.heading("col1", text="Cliente")
        self.tree_ventas_pendiente.heading("col2", text="Descripcion")
        self.tree_ventas_pendiente.heading("col3", text="Fecha")
        self.tree_ventas_pendiente.heading("col4", text="Comprobante")
        self.tree_ventas_pendiente.heading("col5", text="Monto")
        self.tree_ventas_pendiente.heading("col6", text="Estado")
        self.tree_ventas_pendiente.grid(row=0, column=0, ipady=10)


        self.tree_ventas_cobrado= ttk.Treeview(tab_cobrado)
        self.tree_ventas_cobrado["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
        self.tree_ventas_cobrado.column("#0", width=50, anchor=W)
        self.tree_ventas_cobrado.column("col1", width=100)
        self.tree_ventas_cobrado.column("col2", width=100)
        self.tree_ventas_cobrado.column("col3", width=100)
        self.tree_ventas_cobrado.column("col4", width=100)
        self.tree_ventas_cobrado.column("col5", width=100)
        self.tree_ventas_cobrado.column("col6", width=100)
        self.tree_ventas_cobrado.heading("#0", text="ID")
        self.tree_ventas_cobrado.heading("col1", text="Cliente")
        self.tree_ventas_cobrado.heading("col2", text="Descripcion")
        self.tree_ventas_cobrado.heading("col3", text="Fecha")
        self.tree_ventas_cobrado.heading("col4", text="Comprobante")
        self.tree_ventas_cobrado.heading("col5", text="Monto")
        self.tree_ventas_cobrado.heading("col6", text="Estado")
        self.tree_ventas_cobrado.grid(row=0, column=0, ipady=10)

        ven.mainloop()
