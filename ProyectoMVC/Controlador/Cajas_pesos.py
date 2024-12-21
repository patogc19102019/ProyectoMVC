class CajasController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def update_view(self):
        cajas_con_pesos = self.model.get_pesos_cajas()
        self.view.show_cajas_con_pesos(cajas_con_pesos)


class ControladorGanancias:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.set_controlador(self)

    def agregar_transaccion(self, moneda, cantidad, tasa_cambio, ganancia):
        self.modelo.agregar_transaccion(moneda, cantidad, tasa_cambio, ganancia)
        messagebox.showinfo("Éxito", "Transacción agregada con éxito.")

    def obtener_ganancias_por_moneda(self):
        return self.modelo.calcular_ganancias_por_moneda()

    def obtener_pesos_cajas(self):
        return self.modelo.obtener_pesos_cajas()
