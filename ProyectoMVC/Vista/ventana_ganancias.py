import tkinter as tk
from tkinter import ttk, messagebox

class VentanaGanancias:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Ganancias")

        # Frame principal
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Botones
        self.btn_agregar = ttk.Button(self.frame, text="Agregar Transacción", command=self.solicitar_datos_transaccion)
        self.btn_agregar.grid(row=0, column=0, padx=5, pady=5)

        self.btn_ver_ganancias = ttk.Button(self.frame, text="Ver Ganancias por Moneda", command=self.mostrar_ganancias)
        self.btn_ver_ganancias.grid(row=0, column=1, padx=5, pady=5)

        self.btn_ver_pesos = ttk.Button(self.frame, text="Ver Pesos por Caja", command=self.mostrar_pesos_cajas)
        self.btn_ver_pesos.grid(row=0, column=2, padx=5, pady=5)

        self.salida = tk.Text(self.frame, width=80, height=20, state=tk.DISABLED)
        self.salida.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.controlador = None

    def set_controlador(self, controlador):
        self.controlador = controlador

    def solicitar_datos_transaccion(self):
        def agregar():
            moneda = entry_moneda.get()
            cantidad = float(entry_cantidad.get())
            tasa_cambio = float(entry_tasa.get())
            ganancia = float(entry_ganancia.get())
            self.controlador.agregar_transaccion(moneda, cantidad, tasa_cambio, ganancia)
            ventana_transaccion.destroy()

        ventana_transaccion = tk.Toplevel(self.root)
        ventana_transaccion.title("Agregar Transacción")

        ttk.Label(ventana_transaccion, text="Moneda:").grid(row=0, column=0, padx=5, pady=5)
        entry_moneda = ttk.Entry(ventana_transaccion)
        entry_moneda.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(ventana_transaccion, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5)
        entry_cantidad = ttk.Entry(ventana_transaccion)
        entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(ventana_transaccion, text="Tasa de cambio:").grid(row=2, column=0, padx=5, pady=5)
        entry_tasa = ttk.Entry(ventana_transaccion)
        entry_tasa.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(ventana_transaccion, text="Ganancia:").grid(row=3, column=0, padx=5, pady=5)
        entry_ganancia = ttk.Entry(ventana_transaccion)
        entry_ganancia.grid(row=3, column=1, padx=5, pady=5)

        btn_guardar = ttk.Button(ventana_transaccion, text="Guardar", command=agregar)
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)

    def mostrar_ganancias(self):
        ganancias = self.controlador.obtener_ganancias_por_moneda()
        self.salida.configure(state=tk.NORMAL)
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, "=== Ganancias por Moneda ===\n")
        for moneda, ganancia in ganancias.items():
            self.salida.insert(tk.END, f"Moneda: {moneda} | Ganancia: {ganancia:.2f}\n")
        self.salida.configure(state=tk.DISABLED)

    def mostrar_pesos_cajas(self):
        pesos_cajas = self.controlador.obtener_pesos_cajas()
        self.salida.configure(state=tk.NORMAL)
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, "=== Pesos por Caja ===\n")
        for caja in pesos_cajas:
            self.salida.insert(tk.END, f"Caja ID: {caja['id']} | Pesos: {caja['pesos']:.2f}\n")
        self.salida.configure(state=tk.DISABLED)

    def mostrar_moneda_mas_vendida(self):
        moneda, cantidad = self.controlador.obtener_moneda_mas_vendida()
        self.salida.configure(state=tk.NORMAL)
        self.salida.delete(1.0, tk.END)
        self.salida.insert(tk.END, "=== Moneda Más Vendida ===\n")
        if moneda:
            self.salida.insert(tk.END, f"Moneda: {moneda} | Cantidad vendida: {cantidad:.2f}\n")
        else:
            self.salida.insert(tk.END, "No hay transacciones registradas.\n")
        self.salida.configure(state=tk.DISABLED)