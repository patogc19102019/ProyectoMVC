class ControladorDisponibilidad:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.set_controlador(self)

        # Cargar las cajas habilitadas en la vista
        cajas_habilitadas = self.modelo.obtener_cajas_habilitadas()
        self.vista.cargar_cajas(cajas_habilitadas)

    def obtener_disponibilidad(self):
        """Devuelve la disponibilidad de pesos desde el modelo."""
        return self.modelo.cajas

    def registrar_pesos(self, id_caja, pesos):
        """Registra la disponibilidad de pesos en el modelo."""
        if self.modelo.registrar_pesos(id_caja, pesos):
            print(f"Pesos registrados: Caja {id_caja}, {pesos} pesos disponibles.")
        else:
            messagebox.showerror("Error", "No se pudo registrar la disponibilidad de pesos.")
