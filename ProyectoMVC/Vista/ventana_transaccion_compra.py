import tkinter as tk
from tkinter import ttk, messagebox

class VentanaTransaccionCompra:
    def __init__(self, root):
        self.root = root
        self.root.title("Compra de Moneda Extranjera")

        # Frame principal
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Selección de moneda
        ttk.Label(self.frame, text="Seleccione Moneda:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_monedas = ttk.Combobox(self.frame, state="readonly")
        self.combo_monedas.grid(row=0, column=1, padx=5, pady=5)

        # Ingreso del monto en moneda extranjera
        ttk.Label(self.frame, text="Monto en Moneda Extranjera:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_monto = ttk.Entry(self.frame)
        self.entry_monto.grid(row=1, column=1, padx=5, pady=5)

        # Botón para calcular
        self.btn_calcular = ttk.Button(self.frame, text="Calcular en Pesos", command=self.calcular_costo)
        self.btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)

        # Resultado del costo en pesos
        self.label_resultado = ttk.Label(self.frame, text="Costo en Pesos: -")
        self.label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

        # Botón para confirmar compra
        self.btn_comprar = ttk.Button(self.frame, text="Confirmar Compra", command=self.registrar_compra)
        self.btn_comprar.grid(row=4, column=0, columnspan=2, pady=10)

        self.controlador = None

    def set_controlador(self, controlador):
        self.controlador = controlador

    def cargar_monedas(self, monedas):
        """Carga las monedas disponibles en el combo."""
        self.combo_monedas["values"] = [f"{moneda['nombre']} (ID: {moneda['id']})" for moneda in monedas]

    def calcular_costo(self):
        """Calcula el costo en pesos chilenos según el tipo de cambio."""
        if self.controlador:
            try:
                moneda_seleccionada = self.combo_monedas.get()
                if not moneda_seleccionada:
                    raise ValueError("Debe seleccionar una moneda.")
                id_moneda = int(moneda_seleccionada.split()[-1].strip("()"))
                monto = float(self.entry_monto.get())
                costo = self.controlador.calcular_costo(id_moneda, monto)
                self.label_resultado.config(text=f"Costo en Pesos: {costo:.2f}")
            except ValueError as e:
                messagebox.showerror("Error", f"Entrada inválida: {str(e)}")

    def registrar_compra(self):
        """Registra la compra de moneda extranjera."""
        if self.controlador:
            try:
                moneda_seleccionada = self.combo_monedas.get()
                if not moneda_seleccionada:
                    raise ValueError("Debe seleccionar una moneda.")
                id_moneda = int(moneda_seleccionada.split()[-1].strip("()"))
                monto = float(self.entry_monto.get())
                self.controlador.registrar_transaccion(id_moneda, monto)
                messagebox.showinfo("Éxito", "Transacción registrada correctamente.")
                self.entry_monto.delete(0, tk.END)
                self.label_resultado.config(text="Costo en Pesos: -")
            except ValueError as e:
                messagebox.showerror("Error", f"Entrada inválida: {str(e)}")
