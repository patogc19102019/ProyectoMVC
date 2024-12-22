import tkinter as tk
from tkinter import ttk, messagebox


class VentanaDisponibilidad:
    def __init__(self, root):
        self.root = root
        self.root.title("Disponibilidad de Pesos")

        # Frame principal
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Botón para consultar la disponibilidad
        self.btn_consultar = ttk.Button(self.frame, text="Consultar Disponibilidad", command=self.mostrar_disponibilidad)
        self.btn_consultar.grid(row=0, column=0, padx=5, pady=5)

        # Área de salida
        self.salida = tk.Text(self.frame, width=50, height=15, state=tk.DISABLED)
        self.salida.grid(row=1, column=0, padx=5, pady=5)

        # Elementos para registrar pesos
        ttk.Label(self.frame, text="Seleccionar Caja:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.combo_cajas = ttk.Combobox(self.frame, state="readonly")
        self.combo_cajas.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.frame, text="Cantidad de Pesos:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_pesos = ttk.Entry(self.frame)
        self.entry_pesos.grid(row=3, column=1, padx=5, pady=5)

        self.btn_registrar = ttk.Button(self.frame, text="Registrar Pesos", command=self.registrar_pesos)
        self.btn_registrar.grid(row=4, column=1, padx=5, pady=10)

        self.controlador = None

    def set_controlador(self, controlador):
        self.controlador = controlador

    def cargar_cajas(self, cajas):
        """Carga las cajas habilitadas en el combo."""
        self.combo_cajas["values"] = [f"Caja {caja['id']}" for caja in cajas]

    def mostrar_disponibilidad(self):
        """Muestra la disponibilidad de pesos por caja."""
        if self.controlador:
            cajas = self.controlador.obtener_disponibilidad()
            self.salida.configure(state=tk.NORMAL)
            self.salida.delete(1.0, tk.END)
            self.salida.insert(tk.END, "=== Disponibilidad de Pesos por Caja ===\n")
            for caja in cajas:
                self.salida.insert(tk.END, f"Caja ID: {caja['id']} | Pesos disponibles: {caja['pesos']}\n")
            self.salida.configure(state=tk.DISABLED)

    def registrar_pesos(self):
        """Registra la cantidad de pesos en la caja seleccionada."""
        if self.controlador:
            try:
                caja_seleccionada = self.combo_cajas.get()
                if not caja_seleccionada:
                    raise ValueError("Debe seleccionar una caja.")
                id_caja = int(caja_seleccionada.split()[-1])
                pesos = float(self.entry_pesos.get())
                self.controlador.registrar_pesos(id_caja, pesos)
                messagebox.showinfo("Éxito", "Pesos registrados correctamente.")
                self.entry_pesos.delete(0, tk.END)
                self.mostrar_disponibilidad()
            except ValueError as e:
                messagebox.showerror("Error", f"Entrada inválida: {str(e)}")
