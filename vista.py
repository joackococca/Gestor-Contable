import tkinter as tk
from tkinter import Tk, W, messagebox, Toplevel
from tkinter import ttk
from controlador import Controlador



class Ventana():
    def __init__(self):
        ven = Tk()
        ven.title("Gestor Contable")
        ven.geometry("1100x400")

        self.objcont= Controlador()

        notebook= ttk.Notebook(ven)
        notebook.grid(row=0, column=0, padx=10)

        tab_compras=ttk.Frame(notebook)
        tab_ventas=ttk.Frame(notebook)
        tab_gastos=ttk.Frame(notebook)
        tab_resumen=ttk.Frame(notebook)

        menu = tk.Menu(ven)
        ven.config(menu=menu)

        filemenu = tk.Menu(menu)
        menu.add_cascade(label="Herramientas", menu=filemenu)
        filemenu.add_command(label="Modificar", command=lambda:self.modificar_tree())
        filemenu.add_command(label="Borrar")
        filemenu.add_command(label="Buscar")
        filemenu.add_separator()

        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Ayuda", menu=helpmenu)
        helpmenu.add_command(label="Tutorial")

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
        fr_registro_ventas= tk.Frame(tab_ventas, width=800, height=330, bd=2, relief="groove")
        fr_new_registro_ventas.grid(row=0, column=0 )
        fr_registro_ventas.grid(row=0, column=1)

        fr_new_registro_ventas.grid_propagate(False)
        fr_registro_ventas.grid_propagate(False)

        label_registro_v=tk.Label(fr_registro_ventas, text="REGISTRO", font=("Arial", 10, "bold"))

        label_titulo_v=tk.Label(fr_new_registro_ventas, text="NUEVO REGISTRO", font=("Arial", 10, "bold"))
        label_monto_v=tk.Label(fr_new_registro_ventas, text="Monto ($)")
        label_fecha_v=tk.Label(fr_new_registro_ventas, text="Fecha")
        label_cliente_v=tk.Label(fr_new_registro_ventas, text="Cliente")
        label_descripcion_v=tk.Label(fr_new_registro_ventas, text="Descripcion")
        label_comprobante_v=tk.Label(fr_new_registro_ventas, text="Comprobante N°")
        label_estado_v=tk.Label(fr_new_registro_ventas, text="Estado")

        label_registro_v.grid(row=0, column=1)

        label_titulo_v.grid(row=0, column=1, padx=58)
        label_monto_v.grid(row=1, column=1)
        label_fecha_v.grid(row=3, column=1)
        label_cliente_v.grid(row=5, column=1)
        label_descripcion_v.grid(row=7, column=1)
        label_comprobante_v.grid(row=9, column=1)
        label_estado_v.grid(row=11, column=1)

        self.entry_a_v=tk.Entry(fr_new_registro_ventas)
        self.entry_b_v=tk.Entry(fr_new_registro_ventas)
        self.entry_c_v=tk.Entry(fr_new_registro_ventas)
        self.entry_d_v=tk.Entry(fr_new_registro_ventas)
        self.entry_e_v=tk.Entry(fr_new_registro_ventas)

        self.entry_a_v.grid(row=2, column=1, ipadx=30)
        self.entry_b_v.grid(row=4, column=1, ipadx=30)
        self.entry_c_v.grid(row=6, column=1, ipadx=30)
        self.entry_d_v.grid(row=8, column=1, ipadx=30)
        self.entry_e_v.grid(row=10, column=1, ipadx=30)

        self.var_opcion_a = tk.StringVar()
        self.var_opcion_a.set("Pendiente")
        radio_cobrado=tk.Radiobutton(fr_new_registro_ventas, text="Cobrado", variable=self.var_opcion_a, value="Cobrado")
        radio_pendiente=tk.Radiobutton(fr_new_registro_ventas, text="Pendiente", variable=self.var_opcion_a, value="Pendiente")
        tk.Button(fr_new_registro_ventas, text="+ Guardar Venta", command=lambda:self.alta_vista()).grid(row=14, column=1)

        radio_cobrado.grid(row=12, column=1)
        radio_pendiente.grid(row=13, column=1)

        var_opcion_b = tk.StringVar()
        var_opcion_b.set(1)
        radio_todos=tk.Radiobutton(fr_registro_ventas, text="Todos", variable=var_opcion_b, value=1)
        radio_pendiente_a=tk.Radiobutton(fr_registro_ventas, text="Pendiente", variable=var_opcion_b, value=2)
        radio_cobrado_a=tk.Radiobutton(fr_registro_ventas, text="Cobrado", variable=var_opcion_b, value=3)

        radio_todos.grid(row=1, column=0)
        radio_pendiente_a.grid(row=1, column=1)
        radio_cobrado_a.grid(row=1, column=2)

        self.tree_ventas= ttk.Treeview(fr_registro_ventas)
        self.tree_ventas["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
        self.tree_ventas.column("#0", width=50, anchor=W)
        self.tree_ventas.column("col1", width=100)
        self.tree_ventas.column("col2", width=100)
        self.tree_ventas.column("col3", width=100)
        self.tree_ventas.column("col4", width=100)
        self.tree_ventas.column("col5", width=100)
        self.tree_ventas.column("col6", width=100)
        self.tree_ventas.heading("#0", text="ID")
        self.tree_ventas.heading("col1", text="Monto")
        self.tree_ventas.heading("col2", text="Fecha")
        self.tree_ventas.heading("col3", text="Cliente")
        self.tree_ventas.heading("col4", text="Descripcion")
        self.tree_ventas.heading("col5", text="Comprobante")
        self.tree_ventas.heading("col6", text="Estado")
        self.tree_ventas.grid(row=2, column=1, ipady=15)

        self.cargar_treeview()

        ven.mainloop()

    def cargar_treeview(self):
        self.tree_ventas.delete(*self.tree_ventas.get_children())
        resultado=self.objcont.consultar_todos_controlador()

        for fila in resultado:
            self.tree_ventas.insert("", "end", text=fila[0], values=fila[1:])

    def limpiar_campos(self):
        self.entry_a_v.delete(0, tk.END)
        self.entry_b_v.delete(0, tk.END)
        self.entry_c_v.delete(0, tk.END)
        self.entry_d_v.delete(0, tk.END)
        self.entry_e_v.delete(0, tk.END)

        self.var_opcion_a.set("")

    def alta_vista(self):
        monto=self.entry_a_v.get()
        fecha=self.entry_b_v.get()
        cliente=self.entry_c_v.get()
        descripcion=self.entry_d_v.get()
        comprobante=self.entry_e_v.get()
        estado=self.var_opcion_a.get()

        if not (monto and fecha and cliente and comprobante and estado):
            messagebox.showwarning("Campos incompletos", "Por favor, llene todos los campos obligatorios.")
            return

        try:
            self.objcont.alta_controlador(monto, fecha, cliente, descripcion, comprobante, estado)
            messagebox.showinfo("Éxito", "El registro se guardó correctamente.")
            self.limpiar_campos()
            self.cargar_treeview()

        except Exception as e:
            messagebox.showerror("Error de sistema", f"No se pudo guardar el registro: {e}")

    def obtener_seleccion(self):
        seleccion=self.tree_ventas.selection()

        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, selecciona una fila primero.")
            return None
        return seleccion[0]
    
    def modificar_tree(self):
        fila_id=self.obtener_seleccion()

        if fila_id is None:
            return messagebox.showerror("Error", "No se selecciono ningun registro. Por favor, selecciona una fila primero.")
        
        datos=self.tree_ventas.item(fila_id, "values")
        print(datos)
        self.limpiar_campos()

        def ventana_modificar():
            top=Toplevel()
            top.title("Modificar")

            fr_modificar_registrov= tk.Frame(top, width=250, height=330, bd=2, relief="groove")
            fr_modificar_registrov.grid(row=0, column=0 )

            fr_modificar_registrov.grid_propagate(False)

            label_titulo=tk.Label(fr_modificar_registrov, text="MODIFICAR REGISTRO", font=("Arial", 10, "bold"))
            label_monto=tk.Label(fr_modificar_registrov, text="Monto ($)")
            label_fecha=tk.Label(fr_modificar_registrov, text="Fecha")
            label_cliente=tk.Label(fr_modificar_registrov, text="Cliente")
            label_descripcion=tk.Label(fr_modificar_registrov, text="Descripcion")
            label_comprobante=tk.Label(fr_modificar_registrov, text="Comprobante N°")
            label_estado=tk.Label(fr_modificar_registrov, text="Estado")

            label_titulo.grid(row=0, column=1, padx=58)
            label_monto.grid(row=1, column=1)
            label_fecha.grid(row=3, column=1)
            label_cliente.grid(row=5, column=1)
            label_descripcion.grid(row=7, column=1)
            label_comprobante.grid(row=9, column=1)
            label_estado.grid(row=11, column=1)

            entry_a=tk.Entry(fr_modificar_registrov)
            entry_b=tk.Entry(fr_modificar_registrov)
            entry_c=tk.Entry(fr_modificar_registrov)
            entry_d=tk.Entry(fr_modificar_registrov)
            entry_e=tk.Entry(fr_modificar_registrov)

            entry_a.grid(row=2, column=1, ipadx=30)
            entry_b.grid(row=4, column=1, ipadx=30)
            entry_c.grid(row=6, column=1, ipadx=30)
            entry_d.grid(row=8, column=1, ipadx=30)
            entry_e.grid(row=10, column=1, ipadx=30)

            entry_a.insert(datos[0], "values")
            entry_b.insert(datos[1], "values")
            entry_c.insert(datos[2], "values")
            entry_d.insert(datos[3], "values")
            entry_e.insert(datos[4], "values")

            var_opcion_modificar= tk.StringVar()
            var_opcion_modificar.set(datos[-1], "values")
            radio_cobrado=tk.Radiobutton(fr_modificar_registrov, text="Cobrado", variable=var_opcion_modificar, value="Cobrado")
            radio_pendiente=tk.Radiobutton(fr_modificar_registrov, text="Pendiente", variable=var_opcion_modificar, value="Pendiente")
            tk.Button(fr_modificar_registrov, text="Modificar Venta", command=lambda:self.alta_vista()).grid(row=14, column=1)

            radio_cobrado.grid(row=12, column=1)
            radio_pendiente.grid(row=13, column=1)

            top.mainloop
        
        ventana_modificar()
