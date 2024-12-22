class ControladorTiposCambio:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.set_controlador(self)

    def registrar_tipo_cambio(self, moneda, tasa_cambio):
        """Registra un tipo de cambio en el modelo."""
        self.modelo.registrar_tipo_cambio(moneda, tasa_cambio)

    def obtener_tipos_cambio(self):
        """Obtiene los tipos de cambio registrados."""
        return self.modelo.obtener_tipos_de_cambio()
