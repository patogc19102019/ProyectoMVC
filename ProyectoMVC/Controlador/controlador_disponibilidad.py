class ControladorDisponibilidad:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.set_controlador(self)

    def obtener_disponibilidad(self):
        return self.modelo.obtener_cajas_habilitadas()
