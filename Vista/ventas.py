import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, W



class SeccionVentas:
    def __init__(self, parent, controlador):
        self.objcont = controlador
        fr_new_registro_ventas= tk.Frame(parent, width=250, height=330, bd=2, relief="groove")
        fr_registro_ventas= tk.Frame(parent, width=850, height=330, bd=2, relief="groove")
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

        self.combobox_estado_v=ttk.Combobox(fr_new_registro_ventas, values=["", "Pendiente", "Cobrado"], state="readonly")
        self.combobox_estado_v.grid(row=12, column=1, ipadx=30)

        self.combobox_estado_v.set("")

        button_guardar_v=tk.Button(fr_new_registro_ventas, text="+ Guardar venta", command=lambda:self.alta_vista())
        button_guardar_v.grid(row=13, column=1, padx=50, pady=5)

        self.var_opcion_b = tk.StringVar(value="Todos")

        radio_todos = tk.Radiobutton(fr_registro_ventas, text="Todos",
                                     variable=self.var_opcion_b, value="Todos",
                                     command=lambda:self.filtrar_treeview())
        
        radio_pendiente_a = tk.Radiobutton(fr_registro_ventas, text="Pendiente",
                                            variable=self.var_opcion_b, value="Pendiente",
                                            command=lambda:self.filtrar_treeview())
        
        radio_cobrado_a = tk.Radiobutton(fr_registro_ventas, text="Cobrado",
                                            variable=self.var_opcion_b, value="Cobrado",
                                            command=lambda:self.filtrar_treeview())

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
        self.tree_ventas.column("col6", width=150)
        self.tree_ventas.heading("#0", text="ID")
        self.tree_ventas.heading("col1", text="Monto")
        self.tree_ventas.heading("col2", text="Fecha")
        self.tree_ventas.heading("col3", text="Cliente")
        self.tree_ventas.heading("col4", text="Comprobante")
        self.tree_ventas.heading("col5", text="Estado")
        self.tree_ventas.heading("col6", text="Descripcion")
        self.tree_ventas.grid(row=2, column=1, ipady=15)

        self.cargar_treeview()

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
        self.combobox_estado_v.set("")

    def alta_vista(self):
        monto=self.entry_a_v.get()
        fecha=self.entry_b_v.get()
        cliente=self.entry_c_v.get()
        descripcion=self.entry_d_v.get()
        comprobante=self.entry_e_v.get()
        estado=self.combobox_estado_v.get()

        if not (monto and fecha and cliente and comprobante and estado):
            messagebox.showwarning("Campos incompletos", "Por favor, llene todos los campos obligatorios.")
            return

        try:
            self.objcont.alta_controlador(monto, fecha, cliente, comprobante, estado, descripcion)
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
        
        item = self.tree_ventas.item(fila_id)
        self.registro_id = item["text"]
        datos = item["values"]

        self.limpiar_campos()

        def ventana_modificar(datos):
            self.top=Toplevel()
            self.top.title("Modificar")

            fr_modificar_registrov= tk.Frame(self.top, width=250, height=330, bd=2, relief="groove")
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

            self.entry_a_modificar=tk.Entry(fr_modificar_registrov)
            self.entry_b_modificar=tk.Entry(fr_modificar_registrov)
            self.entry_c_modificar=tk.Entry(fr_modificar_registrov)
            self.entry_d_modificar=tk.Entry(fr_modificar_registrov)
            self.entry_e_modificar=tk.Entry(fr_modificar_registrov)

            self.entry_a_modificar.grid(row=2, column=1, ipadx=30)
            self.entry_b_modificar.grid(row=4, column=1, ipadx=30)
            self.entry_c_modificar.grid(row=6, column=1, ipadx=30)
            self.entry_d_modificar.grid(row=8, column=1, ipadx=30)
            self.entry_e_modificar.grid(row=10, column=1, ipadx=30)

            self.entry_a_modificar.insert(0, datos[0]) #monto
            self.entry_b_modificar.insert(0, datos[1]) #fecha
            self.entry_c_modificar.insert(0, datos[2]) #cliente
            self.entry_d_modificar.insert(0, datos[-1]) #descripcion
            self.entry_e_modificar.insert(0, datos[3]) #comprobante

            estado = datos[4] #estado

            self.combobox_estado_modificar=ttk.Combobox(fr_modificar_registrov, values=["", "Pendiente", "Cobrado"], state="readonly")
            self.combobox_estado_modificar.grid(row=12, column=1, ipadx=30)
            self.combobox_estado_modificar.set(estado)

            button_guardar=tk.Button(fr_modificar_registrov, text="Guardar cambios", command=lambda: self.modificar_vista() )
            button_guardar.grid(row=13, column=1, padx=50, pady=5)

            self.top.mainloop
        
        ventana_modificar(datos)
    
    def modificar_vista(self,):
        
        monto=self.entry_a_modificar.get()
        fecha=self.entry_b_modificar.get()
        cliente=self.entry_c_modificar.get()
        descripcion=self.entry_d_modificar.get()
        comprobante=self.entry_e_modificar.get()
        estado=self.combobox_estado_modificar.get()

        if not (monto and fecha and cliente and comprobante and estado):
            messagebox.showwarning("Campos incompletos", "Por favor, llene todos los campos obligatorios.")
            return
        
        try:
            self.objcont.modificar_controlador(self.registro_id, monto, fecha, cliente, comprobante, estado, descripcion)
            messagebox.showinfo("Éxito", "El registro se modificó correctamente.")
            self.limpiar_campos()
            self.cargar_treeview()
            self.top.destroy()

        except Exception as e:
            messagebox.showerror("Error de sistema", f"No se pudo modificar el registro: {e}")

    def borrar_vista(self):
        fila_id=self.obtener_seleccion()

        if fila_id is None:
            return messagebox.showerror("Error", "No se selecciono ningun registro. Por favor, selecciona una fila primero.")
        
        item = self.tree_ventas.item(fila_id)
        self.registro_id = item["text"]

        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas borrar este registro?")

        if confirmacion:
            try:
                self.objcont.eliminar_controlador(self.registro_id)
                messagebox.showinfo("Éxito", "El registro se borró correctamente.")
                self.cargar_treeview()
            except Exception as e:
                messagebox.showerror("Error de sistema", f"No se pudo borrar el registro: {e}")

    def filtrar_treeview(self):
        opcion = self.var_opcion_b.get()

        if opcion == "Todos":
            resultado = self.objcont.consultar_todos_controlador()
        else:
            resultado = self.objcont.consultar_controlador(estado=opcion)

        self.tree_ventas.delete(*self.tree_ventas.get_children())
        for fila in resultado:
            self.tree_ventas.insert("", "end", text=fila[0], values=fila[1:])