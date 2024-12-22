import tkinter as tk
from tkinter import ttk, messagebox

class VentanaTiposCambio:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar Tipos de Cambio")

        # Frame principal
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Etiquetas y entradas
        ttk.Label(self.frame, text="Moneda:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_moneda = ttk.Entry(self.frame)
        self.entry_moneda.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame, text="Tasa de Cambio:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_tasa = ttk.Entry(self.frame)
        self.entry_tasa.grid(row=1, column=1, padx=5, pady=5)

        # Botones
        self.btn_guardar = ttk.Button(self.frame, text="Guardar Tipo de Cambio", command=self.guardar_tipo_cambio)
        self.btn_guardar.grid(row=2, column=0, columnspan=2, pady=10)

        self.btn_ver_tipos = ttk.Button(self.frame, text="Ver Tipos de Cambio", command=self.mostrar_tipos_cambio)
        self.btn_ver_tipos.grid(row=3, column=0, columnspan=2, pady=10)

        # Área de salida
        self.salida = tk.Text(self.frame, width=50, height=10, state=tk.DISABLED)
        self.salida.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.controlador = None

    def set_controlador(self, controlador):
        self.controlador = controlador

    def guardar_tipo_cambio(self):
        if self.controlador:
            moneda = self.entry_moneda.get()
            tasa = self.entry_tasa.get()
            try:
                tasa = float(tasa)
                self.controlador.registrar_tipo_cambio(moneda, tasa)
                messagebox.showinfo("Éxito", "Tipo de cambio registrado con éxito.")
                self.entry_moneda.delete(0, tk.END)
                self.entry_tasa.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Ingrese una tasa de cambio válida.")

    def mostrar_tipos_cambio(self):
        if self.controlador:
            tipos_cambio = self.controlador.obtener_tipos_cambio()
            self.salida.configure(state=tk.NORMAL)
            self.salida.delete(1.0, tk.END)
            self.salida.insert(tk.END, "=== Tipos de Cambio ===\n")
            for moneda, tasa in tipos_cambio.items():
                self.salida.insert(tk.END, f"Moneda: {moneda} | Tasa de cambio: {tasa:.2f}\n")
            self.salida.configure(state=tk.DISABLED)
