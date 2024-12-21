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

        self.controlador = None

    def set_controlador(self, controlador):
        self.controlador = controlador

    def mostrar_disponibilidad(self):
        if self.controlador:
            cajas = self.controlador.obtener_disponibilidad()
            self.salida.configure(state=tk.NORMAL)
            self.salida.delete(1.0, tk.END)
            self.salida.insert(tk.END, "=== Disponibilidad de Pesos por Caja ===\n")
            for caja in cajas:
                self.salida.insert(tk.END, f"Caja ID: {caja['id']} | Pesos disponibles: {caja['pesos']}\n")
            self.salida.configure(state=tk.DISABLED)