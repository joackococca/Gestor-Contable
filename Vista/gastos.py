import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, W



class SeccionGastos:
    def __init__(self, parent, controlador):
        self.objcont = controlador
        fr_new_registro_gastos= tk.Frame(parent, width=250, height=330, bd=2, relief="groove")
        fr_registro_gastos= tk.Frame(parent, width=700, height=330, bd=2, relief="groove")
        fr_new_registro_gastos.grid(row=0, column=0, padx=50)
        fr_registro_gastos.grid(row=0, column=1)

        fr_new_registro_gastos.grid_propagate(False)
        fr_registro_gastos.grid_propagate(False)

        label_registro_g=tk.Label(fr_registro_gastos, text="REGISTRO", font=("Arial", 10, "bold"))

        label_titulo_g=tk.Label(fr_new_registro_gastos, text="NUEVO REGISTRO", font=("Arial", 10, "bold"))
        label_monto_g=tk.Label(fr_new_registro_gastos, text="Monto ($)")
        label_fecha_g=tk.Label(fr_new_registro_gastos, text="Fecha")
        label_cliente_g=tk.Label(fr_new_registro_gastos, text="Proveedor")
        label_descripcion_g=tk.Label(fr_new_registro_gastos, text="Descripcion")
        label_estado_g=tk.Label(fr_new_registro_gastos, text="Estado")

        label_registro_g.grid(row=0, column=1)

        label_titulo_g.grid(row=0, column=1, padx=58)
        label_monto_g.grid(row=1, column=1)
        label_fecha_g.grid(row=3, column=1)
        label_cliente_g.grid(row=5, column=1)
        label_descripcion_g.grid(row=7, column=1)
        label_estado_g.grid(row=11, column=1)

        self.entry_a_g=tk.Entry(fr_new_registro_gastos)
        self.entry_b_g=tk.Entry(fr_new_registro_gastos)
        self.entry_c_g=tk.Entry(fr_new_registro_gastos)
        self.entry_d_g=tk.Entry(fr_new_registro_gastos)

        self.entry_a_g.grid(row=2, column=1, ipadx=30)
        self.entry_b_g.grid(row=4, column=1, ipadx=30)
        self.entry_c_g.grid(row=6, column=1, ipadx=30)
        self.entry_d_g.grid(row=10, column=1, ipadx=30)

        self.combobox_estado_g=ttk.Combobox(fr_new_registro_gastos, values=["", "Pendiente", "Pagado"], state="readonly")
        self.combobox_estado_g.grid(row=12, column=1, ipadx=30)

        self.combobox_estado_g.set("")

        button_guardar_c=tk.Button(fr_new_registro_gastos, text="+ Guardar Gasto", command=lambda:self.alta_vista())
        button_guardar_c.grid(row=13, column=1, padx=50, pady=5)

        self.var_opcion_b = tk.StringVar(value="Todos")

        radio_todos = tk.Radiobutton(fr_registro_gastos, text="Todos",
                                     variable=self.var_opcion_b, value="Todos",
                                     command=lambda:self.filtrar_treeview())
        
        radio_pendiente_a = tk.Radiobutton(fr_registro_gastos, text="Pendiente",
                                            variable=self.var_opcion_b, value="Pendiente",
                                            command=lambda:self.filtrar_treeview())
        
        radio_cobrado_a = tk.Radiobutton(fr_registro_gastos, text="Pagado",
                                            variable=self.var_opcion_b, value="Pagado",
                                            command=lambda:self.filtrar_treeview())

        radio_todos.grid(row=1, column=0)
        radio_pendiente_a.grid(row=1, column=1)
        radio_cobrado_a.grid(row=1, column=2)

        self.tree_gastos= ttk.Treeview(fr_registro_gastos)
        self.tree_gastos["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.tree_gastos.column("#0", width=50, anchor=W)
        self.tree_gastos.column("col1", width=100)
        self.tree_gastos.column("col2", width=100)
        self.tree_gastos.column("col3", width=100)
        self.tree_gastos.column("col4", width=100)
        self.tree_gastos.column("col5", width=100)
        self.tree_gastos.heading("#0", text="ID")
        self.tree_gastos.heading("col1", text="Monto")
        self.tree_gastos.heading("col2", text="Fecha")
        self.tree_gastos.heading("col3", text="Proveedor")
        self.tree_gastos.heading("col4", text="Estado")
        self.tree_gastos.heading("col5", text="Descripcion")
        self.tree_gastos.grid(row=2, column=1, ipady=15)

        self.tree_gastos.tag_configure('pendiente', background='#ffcccc') 
        self.tree_gastos.tag_configure('pagado', background='#ccffcc')

        self.cargar_treeview()

    def cargar_treeview(self):
        self.tree_gastos.delete(*self.tree_gastos.get_children())
        resultado=self.objcont.consultar_controlador(tipo="Gasto")

        for fila in resultado:
            estado = fila[5]
            tag = 'pendiente' if estado.lower() == 'pendiente' else 'pagado'

            self.tree_gastos.insert(
                "",
                "end",
                text=fila[0],
                values=(fila[1], fila[2], fila[3], fila[5], fila[6]),
                tags=(tag,)
            )

    def limpiar_campos(self):
        self.entry_a_g.delete(0, tk.END)
        self.entry_b_g.delete(0, tk.END)
        self.entry_c_g.delete(0, tk.END)
        self.entry_d_g.delete(0, tk.END)
        self.combobox_estado_g.set("")

    def alta_vista(self):
        tipo = "Gasto"
        monto=self.entry_a_g.get()
        fecha=self.entry_b_g.get()
        cliente=self.entry_c_g.get()
        descripcion=self.entry_d_g.get()
        estado=self.combobox_estado_g.get()

        if not (monto and fecha and cliente and estado):
            messagebox.showwarning("Campos incompletos", "Por favor, llene todos los campos obligatorios.")
            return

        try:
            self.objcont.alta_controlador(tipo, monto, fecha, cliente, "", estado, descripcion)
            messagebox.showinfo("Éxito", "El registro se guardó correctamente.")
            self.limpiar_campos()
            self.cargar_treeview()

        except Exception as e:
            messagebox.showerror("Error de sistema", f"No se pudo guardar el registro: {e}")

    def obtener_seleccion(self):
        seleccion=self.tree_gastos.selection()

        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, selecciona una fila primero.")
            return None
        return seleccion[0]

    def modificar_tree(self):
        fila_id=self.obtener_seleccion()

        if fila_id is None:
            return messagebox.showerror("Error", "No se selecciono ningun registro. Por favor, selecciona una fila primero.")
        
        item = self.tree_gastos.item(fila_id)
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
            label_cliente=tk.Label(fr_modificar_registrov, text="Prooveedor")
            label_descripcion=tk.Label(fr_modificar_registrov, text="Descripcion")
            label_estado=tk.Label(fr_modificar_registrov, text="Estado")

            label_titulo.grid(row=0, column=1, padx=58)
            label_monto.grid(row=1, column=1)
            label_fecha.grid(row=3, column=1)
            label_cliente.grid(row=5, column=1)
            label_descripcion.grid(row=7, column=1)
            label_estado.grid(row=9, column=1)

            self.entry_a_modificar=tk.Entry(fr_modificar_registrov)
            self.entry_b_modificar=tk.Entry(fr_modificar_registrov)
            self.entry_c_modificar=tk.Entry(fr_modificar_registrov)
            self.entry_d_modificar=tk.Entry(fr_modificar_registrov)

            self.entry_a_modificar.grid(row=2, column=1, ipadx=30)
            self.entry_b_modificar.grid(row=4, column=1, ipadx=30)
            self.entry_c_modificar.grid(row=6, column=1, ipadx=30)
            self.entry_d_modificar.grid(row=8, column=1, ipadx=30)

            self.entry_a_modificar.insert(0, datos[0]) #monto
            self.entry_b_modificar.insert(0, datos[1]) #fecha
            self.entry_c_modificar.insert(0, datos[2]) #Proveedor
            self.entry_d_modificar.insert(0, datos[4]) #descripcion

            estado = datos[3] #estado

            self.combobox_estado_modificar=ttk.Combobox(fr_modificar_registrov, values=["", "Pendiente", "Pagado"], state="readonly")
            self.combobox_estado_modificar.grid(row=10, column=1, ipadx=30)
            self.combobox_estado_modificar.set(estado)

            button_guardar=tk.Button(fr_modificar_registrov, text="Guardar cambios", command=lambda: self.modificar_vista() )
            button_guardar.grid(row=11, column=1, padx=50, pady=5)

            self.top.mainloop
        
        ventana_modificar(datos)
    
    def modificar_vista(self,):
        
        monto=self.entry_a_modificar.get()
        fecha=self.entry_b_modificar.get()
        cliente=self.entry_c_modificar.get()
        descripcion=self.entry_d_modificar.get()
        estado=self.combobox_estado_modificar.get()

        if not (monto and fecha and cliente and estado):
            messagebox.showwarning("Campos incompletos", "Por favor, llene todos los campos obligatorios.")
            return
        
        try:
            self.objcont.modificar_controlador(self.registro_id, monto, fecha, cliente, "", estado, descripcion)
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
        
        item = self.tree_gastos.item(fila_id)
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
            resultado = self.objcont.consultar_controlador(tipo="Gasto")
        else:
            resultado = self.objcont.consultar_controlador(tipo="Gasto", estado=opcion)

        self.tree_gastos.delete(*self.tree_gastos.get_children())
        for fila in resultado:
            self.tree_gastos.insert(
                "",
                "end",
                text=fila[0],
                values=(fila[1], fila[2], fila[3], fila[5], fila[6])
            )