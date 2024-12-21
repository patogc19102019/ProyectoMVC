class CajasController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def update_view(self):
        cajas_habilitadas = self.model.get_habilitadas_cajas()
        self.view.show_cajas_habilitadas(cajas_habilitadas)
