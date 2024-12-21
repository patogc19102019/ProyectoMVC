# gestor_cajas.py
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:25:00 2024

@autors: Carlos Luco Montofré
"""

class GestorCajas:
    
    def __init__(self):
        self.cajas = [
            {"id": 1, "estado": "habilitada", "pesos": 5000},
            {"id": 2, "estado": "deshabilitada", "pesos": 0},
            {"id": 3, "estado": "habilitada", "pesos": 10000},
        ]

    def obtener_pesos_cajas(self):
        return [{"id": caja["id"], "pesos": caja["pesos"]} for caja in self.cajas]

    def obtener_cajas_habilitadas(self):
        return [{"id": caja["id"], "estado": caja["estado"]} for caja in self.cajas if caja["estado"] == "habilitada"]

    def add_event_listener(self, event, listener):
        # Implementar la lógica para añadir el escuchador de eventos
        pass
