import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, W



class SeccionCompras:
    def __init__(self, parent, controlador):
        self.objcont = controlador
        fr_new_registro_compras= tk.Frame(parent, width=250, height=330, bd=2, relief="groove")
        fr_registro_compras= tk.Frame(parent, width=850, height=330, bd=2, relief="groove")
        fr_new_registro_compras.grid(row=0, column=0 )
        fr_registro_compras.grid(row=0, column=1)

        fr_new_registro_compras.grid_propagate(False)
        fr_registro_compras.grid_propagate(False)

        label_registro_c=tk.Label(fr_registro_compras, text="REGISTRO", font=("Arial", 10, "bold"))

        label_titulo_c=tk.Label(fr_new_registro_compras, text="NUEVO REGISTRO", font=("Arial", 10, "bold"))
        label_monto_c=tk.Label(fr_new_registro_compras, text="Monto ($)")
        label_fecha_c=tk.Label(fr_new_registro_compras, text="Fecha")
        label_cliente_c=tk.Label(fr_new_registro_compras, text="Vendedor")
        label_descripcion_c=tk.Label(fr_new_registro_compras, text="Descripcion")
        label_comprobante_c=tk.Label(fr_new_registro_compras, text="Comprobante N°")
        label_estado_c=tk.Label(fr_new_registro_compras, text="Estado")

        label_registro_c.grid(row=0, column=1)

        label_titulo_c.grid(row=0, column=1, padx=58)
        label_monto_c.grid(row=1, column=1)
        label_fecha_c.grid(row=3, column=1)
        label_cliente_c.grid(row=5, column=1)
        label_descripcion_c.grid(row=7, column=1)
        label_comprobante_c.grid(row=9, column=1)
        label_estado_c.grid(row=11, column=1)

        self.entry_a_c=tk.Entry(fr_new_registro_compras)
        self.entry_b_c=tk.Entry(fr_new_registro_compras)
        self.entry_c_c=tk.Entry(fr_new_registro_compras)
        self.entry_d_c=tk.Entry(fr_new_registro_compras)
        self.entry_e_c=tk.Entry(fr_new_registro_compras)

        self.entry_a_c.grid(row=2, column=1, ipadx=30)
        self.entry_b_c.grid(row=4, column=1, ipadx=30)
        self.entry_c_c.grid(row=6, column=1, ipadx=30)
        self.entry_d_c.grid(row=8, column=1, ipadx=30)
        self.entry_e_c.grid(row=10, column=1, ipadx=30)

        self.combobox_estado_c=ttk.Combobox(fr_new_registro_compras, values=["", "Pendiente", "Pagado"], state="readonly")
        self.combobox_estado_c.grid(row=12, column=1, ipadx=30)

        self.combobox_estado_c.set("")

        button_guardar_c=tk.Button(fr_new_registro_compras, text="+ Guardar compra", command=lambda:self.alta_vista())
        button_guardar_c.grid(row=13, column=1, padx=50, pady=5)

        self.var_opcion_b = tk.StringVar(value="Todos")

        radio_todos = tk.Radiobutton(fr_registro_compras, text="Todos",
                                     variable=self.var_opcion_b, value="Todos",
                                     command=lambda:self.filtrar_treeview())
        
        radio_pendiente_a = tk.Radiobutton(fr_registro_compras, text="Pendiente",
                                            variable=self.var_opcion_b, value="Pendiente",
                                            command=lambda:self.filtrar_treeview())
        
        radio_cobrado_a = tk.Radiobutton(fr_registro_compras, text="Pagado",
                                            variable=self.var_opcion_b, value="Pagado",
                                            command=lambda:self.filtrar_treeview())

        radio_todos.grid(row=1, column=0)
        radio_pendiente_a.grid(row=1, column=1)
        radio_cobrado_a.grid(row=1, column=2)

        self.tree_compras= ttk.Treeview(fr_registro_compras)
        self.tree_compras["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
        self.tree_compras.column("#0", width=50, anchor=W)
        self.tree_compras.column("col1", width=100)
        self.tree_compras.column("col2", width=100)
        self.tree_compras.column("col3", width=100)
        self.tree_compras.column("col4", width=100)
        self.tree_compras.column("col5", width=100)
        self.tree_compras.column("col6", width=150)
        self.tree_compras.heading("#0", text="ID")
        self.tree_compras.heading("col1", text="Monto")
        self.tree_compras.heading("col2", text="Fecha")
        self.tree_compras.heading("col3", text="Vendedor")
        self.tree_compras.heading("col4", text="Comprobante")
        self.tree_compras.heading("col5", text="Estado")
        self.tree_compras.heading("col6", text="Descripcion")
        self.tree_compras.grid(row=2, column=1, ipady=15)

        self.tree_compras.tag_configure('pendiente', background='#ffcccc') 
        self.tree_compras.tag_configure('pagado', background='#ccffcc')

        self.cargar_treeview()

    def cargar_treeview(self):
        self.tree_compras.delete(*self.tree_compras.get_children())
        resultado=self.objcont.consultar_controlador(tipo="Compra")

        for fila in resultado:
            estado = fila[5]
            tag = 'pendiente' if estado.lower() == 'pendiente' else 'pagado'

            self.tree_compras.insert(
                "",
                "end",
                text=fila[0],
                values=(fila[1], fila[2], fila[3], fila[5], fila[6], fila[4]),
                tags=(tag,)
            )

    def limpiar_campos(self):
        self.entry_a_c.delete(0, tk.END)
        self.entry_b_c.delete(0, tk.END)
        self.entry_c_c.delete(0, tk.END)
        self.entry_d_c.delete(0, tk.END)
        self.entry_e_c.delete(0, tk.END)
        self.combobox_estado_c.set("")

    def alta_vista(self):
        tipo = "Compra"
        monto=self.entry_a_c.get()
        fecha=self.entry_b_c.get()
        cliente=self.entry_c_c.get()
        descripcion=self.entry_d_c.get()
        comprobante=self.entry_e_c.get()
        estado=self.combobox_estado_c.get()

        if not (monto and fecha and cliente and comprobante and estado):
            messagebox.showwarning("Campos incompletos", "Por favor, llene todos los campos obligatorios.")
            return

        try:
            self.objcont.alta_controlador(tipo, monto, fecha, cliente, comprobante, estado, descripcion)
            messagebox.showinfo("Éxito", "El registro se guardó correctamente.")
            self.limpiar_campos()
            self.cargar_treeview()

        except Exception as e:
            messagebox.showerror("Error de sistema", f"No se pudo guardar el registro: {e}")

    def obtener_seleccion(self):
        seleccion=self.tree_compras.selection()

        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, selecciona una fila primero.")
            return None
        return seleccion[0]

    def modificar_tree(self):
        fila_id=self.obtener_seleccion()

        if fila_id is None:
            return messagebox.showerror("Error", "No se selecciono ningun registro. Por favor, selecciona una fila primero.")
        
        item = self.tree_compras.item(fila_id)
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
            label_cliente=tk.Label(fr_modificar_registrov, text="Vendedor")
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
            self.entry_c_modificar.insert(0, datos[2]) #Vendedor
            self.entry_d_modificar.insert(0, datos[5]) #descripcion
            self.entry_e_modificar.insert(0, datos[3]) #comprobante

            estado = datos[4] #estado

            self.combobox_estado_modificar=ttk.Combobox(fr_modificar_registrov, values=["", "Pendiente", "Pagado"], state="readonly")
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
        
        item = self.tree_compras.item(fila_id)
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
            resultado = self.objcont.consultar_controlador(tipo="Compra")
        else:
            resultado = self.objcont.consultar_controlador(tipo="Compra", estado=opcion)

        self.tree_compras.delete(*self.tree_compras.get_children())
        for fila in resultado:
            self.tree_compras.insert("", "end", text=fila[0], values=fila[1:])