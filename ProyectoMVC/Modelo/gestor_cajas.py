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

    def obtener_pesos_cajas(self):
        return [{"id": caja["id"], "pesos": caja["pesos"]} for caja in self.cajas]

    def agregar_transaccion(self, moneda, cantidad, tasa_cambio, ganancia):
        nueva_transaccion = Transaccion(moneda, cantidad, tasa_cambio, ganancia)
        self.transacciones.append(nueva_transaccion)

    def calcular_ganancias_por_moneda(self):
        ganancias_por_moneda = {}
        for transaccion in self.transacciones:
            if transaccion.moneda not in ganancias_por_moneda:
                ganancias_por_moneda[transaccion.moneda] = 0
            ganancias_por_moneda[transaccion.moneda] += transaccion.ganancia
        return ganancias_por_moneda
