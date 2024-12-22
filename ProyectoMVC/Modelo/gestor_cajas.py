class Transaccion:
    def __init__(self, moneda, cantidad, tasa_cambio, ganancia):
        self.moneda = moneda
        self.cantidad = cantidad
        self.tasa_cambio = tasa_cambio
        self.ganancia = ganancia



class GestorCajas:
    def __init__(self):
        self.cajas = [
            {"id": 1, "estado": "habilitada", "pesos": 5000},
            {"id": 2, "estado": "deshabilitada", "pesos": 0},
            {"id": 3, "estado": "habilitada", "pesos": 10000},
        ]
        self.transacciones = []
        self.tipos_de_cambio = {}

    def obtener_pesos_cajas(self):
        """Devuelve la lista de todas las cajas con su ID y pesos."""
        return [{"id": caja["id"], "pesos": caja["pesos"]} for caja in self.cajas]

    def obtener_cajas_habilitadas(self):
        """Filtra las cajas habilitadas y devuelve su ID y pesos."""
        return [{"id": caja["id"], "pesos": caja["pesos"]} for caja in self.cajas if caja["estado"] == "habilitada"]

    def agregar_transaccion(self, moneda, cantidad, tasa_cambio, ganancia):
        nueva_transaccion = Transaccion(moneda, cantidad, tasa_cambio, ganancia)
        self.transacciones.append(nueva_transaccion)

    def calcular_ganancias_por_moneda(self):
        """Calcula las ganancias acumuladas para cada moneda."""
        ganancias_por_moneda = {}
        for transaccion in self.transacciones:
            if transaccion.moneda not in ganancias_por_moneda:
                ganancias_por_moneda[transaccion.moneda] = 0
            ganancias_por_moneda[transaccion.moneda] += transaccion.ganancia
        return ganancias_por_moneda

    def obtener_moneda_mas_vendida(self):
        ventas_por_moneda = {}
        for transaccion in self.transacciones:
            if transaccion.moneda not in ventas_por_moneda:
                ventas_por_moneda[transaccion.moneda] = 0
            ventas_por_moneda[transaccion.moneda] += transaccion.cantidad
        if not ventas_por_moneda:
            return None, 0
        moneda_mas_vendida = max(ventas_por_moneda, key=ventas_por_moneda.get)
        return moneda_mas_vendida, ventas_por_moneda[moneda_mas_vendida]

    def registrar_tipo_cambio(self, moneda, tasa_cambio):
        """Registra un nuevo tipo de cambio."""
        self.tipos_de_cambio[moneda] = tasa_cambio

    def obtener_tipos_de_cambio(self):
        """Devuelve los tipos de cambio registrados."""
        return self.tipos_de_cambio

    def registrar_pesos(self, id_caja, pesos):
        """Registra la cantidad de pesos disponibles en una caja."""
        for caja in self.cajas:
            if caja["id"] == id_caja:
                caja["pesos"] = pesos
                return True
        return False

    def obtener_cajas_habilitadas(self):
        """Devuelve las cajas que están habilitadas."""
        return [caja for caja in self.cajas if caja["estado"] == "habilitada"]