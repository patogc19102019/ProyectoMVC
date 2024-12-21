class CajasController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def update_view(self):
        cajas_con_pesos = self.model.get_pesos_cajas()
        self.view.show_cajas_con_pesos(cajas_con_pesos)
