# caja_DAO.py
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:20:00 2024

@autors: Carlos Luco Montofré
"""

import mysql.connector

class CajaDAO:
    def __init__(self):
        self.conector = ConectorBD("localhost", "root", "", "mi_base_de_datos")

    def leer_datos(self):
        sql = "SELECT * FROM cajas WHERE activa = 1"
        code, result = self.conector.ejecutarSelectAll(sql)
        if code == 0:
            return result
        else:
            return {}

