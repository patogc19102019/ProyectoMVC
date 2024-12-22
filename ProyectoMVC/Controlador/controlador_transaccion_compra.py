class ControladorTransaccionCompra:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.set_controlador(self)

        # Cargar las monedas disponibles
        monedas_disponibles = self.modelo.obtener_monedas()
        self.vista.cargar_monedas(monedas_disponibles)

    def calcular_costo(self, id_moneda, monto):
        """Calcula el costo en pesos basado en el tipo de cambio."""
        tipo_cambio = self.modelo.obtener_tipo_cambio(id_moneda)
        return monto * tipo_cambio

    def registrar_transaccion(self, id_moneda, monto):
        """Registra la compra de moneda extranjera."""
        tipo_cambio = self.modelo.obtener_tipo_cambio(id_moneda)
        costo = monto * tipo_cambio
        self.modelo.registrar_compra(id_moneda, monto, costo)
