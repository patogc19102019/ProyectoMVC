# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:53:53 2024

@author: Carlos Luco Montofré
"""

from .gestor_usuarios import Gestor_Usuarios
from .gestor_datos import Gestor_Datos
from .gestor_cajas import GestorCajas

class Model:
    def __init__(self):
        self.gestor_usuarios = Gestor_Usuarios()
        self.gestor_cajas = GestorCajas()
        self.gestor_datos = Gestor_Datos()
        self.gestor_cajas = GestorCajas()

    def get_pesos_cajas(self): 
        return self.gestor_cajas.obtener_pesos_cajas()