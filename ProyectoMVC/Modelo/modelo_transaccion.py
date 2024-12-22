class ModeloTransaccion:
    def __init__(self):
        # Simula la base de datos
        self.monedas = [
            {"id": 1, "nombre": "USD", "tipo_cambio": 850},
            {"id": 2, "nombre": "EUR", "tipo_cambio": 900},
        ]
        self.transacciones = []

    def obtener_monedas(self):
        """Devuelve la lista de monedas disponibles."""
        return self.monedas

    def obtener_tipo_cambio(self, id_moneda):
        """Obtiene el tipo de cambio para una moneda específica."""
        for moneda in self.monedas:
            if moneda["id"] == id_moneda:
                return moneda["tipo_cambio"]
        raise ValueError("Moneda no encontrada.")

    def registrar_compra(self, id_moneda, monto, costo):
        """Registra una compra en el sistema."""
        transaccion = {"id_moneda": id_moneda, "monto": monto, "costo": costo}
        self.transacciones.append(transaccion)
