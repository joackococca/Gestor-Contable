import tkinter as tk

class Resumen:
    def __init__(self, parent, con):
        self.objcon=con
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

        frame1=tk.Frame(parent, bd=2, background="lightpink", relief="groove")
        frame1.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)

        frame2=tk.Frame(parent, bd=2, background="lightblue", relief="groove")
        frame2.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure(1, weight=1)

        frame3=tk.Frame(parent, bd=2, background="lightyellow", relief="groove")
        frame3.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        
        frame3.grid_rowconfigure(0, weight=1)
        frame3.grid_columnconfigure(2, weight=1)

        frame4=tk.Frame(parent, bd=2, background="lightgreen", relief="groove")
        frame4.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        frame4.grid_rowconfigure(0, weight=1)
        frame4.grid_columnconfigure(1, weight=1)

        label1=tk.Label(parent, text="Resumen de la contabilidad", font=("Arial", 18, "bold"))

        label2=tk.Label(frame1, text="Total de compras: ", font=("Arial", 12))
        label3=tk.Label(frame2, text="Total de ventas: ", font=("Arial", 12))
        label4=tk.Label(frame3, text="Total de gastos: ", font=("Arial", 12))
        label5=tk.Label(frame4, text="Balance: ", font=("Arial", 12))

        label6=tk.Label(frame1, text="Total pendiente: ", font=("Arial", 12))#compras
        label7=tk.Label(frame2, text="Total pendiente: ", font=("Arial", 12))#ventas
        label8=tk.Label(frame3, text="Total pendiente: ", font=("Arial", 12))#gastos

        label9=tk.Label(frame1, text="Total pagado: ", font=("Arial", 12))#compras
        label10=tk.Label(frame3, text="Total pagado: ", font=("Arial", 12))#gastos
        label11=tk.Label(frame2, text="Total cobrado: ", font=("Arial", 12))#ventas

        label1.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        label2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        label3.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        label4.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        label6.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        label7.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        label8.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

        label9.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
        label10.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
        label11.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

        label5.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

        self.obtener_datos()
        self.label12=tk.Label(frame1, text="", font=("Arial", 10, "bold"), bg="white")
        self.label12.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.label13=tk.Label(frame2, text="", font=("Arial", 10, "bold"), bg="white")
        self.label13.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        self.label14=tk.Label(frame3, text="", font=("Arial", 10, "bold"), bg="white")
        self.label14.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        self.label15=tk.Label(frame1, text="", font=("Arial", 10, "bold"), bg="white")
        self.label15.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        self.label16=tk.Label(frame2, text="", font=("Arial", 10, "bold"), bg="white")
        self.label16.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        self.label17=tk.Label(frame3, text="", font=("Arial", 10, "bold"), bg="white")
        self.label17.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

        self.label18=tk.Label(frame1, text="", font=("Arial", 10, "bold"), bg="white")
        self.label18.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
        self.label19=tk.Label(frame2, text="", font=("Arial", 10, "bold"), bg="white")
        self.label19.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")
        self.label20=tk.Label(frame3, text="", font=("Arial", 10, "bold"), bg="white")
        self.label20.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

        self.label21=tk.Label(frame4, text="", font=("Arial", 10, "bold"), bg="white")
        self.label21.grid(row=8, column=1, padx=5, pady=5, sticky="nsew")
        self.actualizar_datos()

    def obtener_datos(self):
        total_compras = self.objcon.consultar_controlador(tipo="Compra")
        self.monto_total_compras = sum([compra[1] for compra in total_compras])

        total_ventas = self.objcon.consultar_controlador(tipo="Venta")
        self.monto_total_ventas = sum([venta[1] for venta in total_ventas])

        total_gastos = self.objcon.consultar_controlador(tipo="Gasto")
        self.monto_total_gastos = sum([gasto[1] for gasto in total_gastos])

        total_compras_pendiente = self.objcon.consultar_controlador(tipo="Compra", estado="Pendiente")
        self.monto_total_compras_pendiente = sum([compra[1] for compra in total_compras_pendiente])

        total_ventas_pendiente = self.objcon.consultar_controlador(tipo="Venta", estado="Pendiente")
        self.monto_total_ventas_pendiente = sum([venta[1] for venta in total_ventas_pendiente])

        total_gastos_pendiente = self.objcon.consultar_controlador(tipo="Gasto", estado="Pendiente")
        self.monto_total_gastos_pendiente = sum([gasto[1] for gasto in total_gastos_pendiente])

        total_compras_pagado = self.objcon.consultar_controlador(tipo="Compra", estado="Pagado")
        self.monto_total_compras_pagado = sum([compra[1] for compra in total_compras_pagado])

        total_ventas_cobrado = self.objcon.consultar_controlador(tipo="Venta", estado="Cobrado")
        self.monto_total_ventas_cobrado = sum([venta[1] for venta in total_ventas_cobrado])

        total_gastos_pagado = self.objcon.consultar_controlador(tipo="Gasto", estado="Pagado")
        self.monto_total_gastos_pagado = sum([gasto[1] for gasto in total_gastos_pagado])

        self.balance = self.monto_total_ventas - (self.monto_total_compras + self.monto_total_gastos)

    def actualizar_datos(self):
        self.obtener_datos()

        self.label12.config(text=f"{self.monto_total_compras}$")
        self.label13.config(text=f"{self.monto_total_ventas}$")
        self.label14.config(text=f"{self.monto_total_gastos}$")
        self.label15.config(text=f"{self.monto_total_compras_pendiente}$")
        self.label16.config(text=f"{self.monto_total_ventas_pendiente}$")
        self.label17.config(text=f"{self.monto_total_gastos_pendiente}$")
        self.label18.config(text=f"{self.monto_total_compras_pagado}$")
        self.label19.config(text=f"{self.monto_total_ventas_cobrado}$")
        self.label20.config(text=f"{self.monto_total_gastos_pagado}$")
        self.label21.config(text=f"{self.balance}$")