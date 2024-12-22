# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:01:03 2024

@author: Carlos Luco Montofré
"""

import mysql.connector

class ConectorBD:

    def __init__(self, hostdb, userdb, passwordb, basedatosdb):
        self.__hostdb = hostdb
        self.__userdb = userdb
        self.__passwordb = passwordb
        self.__basedatosdb = basedatosdb

    def activarConexion(self):
        print("Intentando conectar a la base de datos...")  # Mensaje de depuración
        try:
            self.conexion = mysql.connector.connect(
                host=self.getHost(),
                user=self.getUser(),
                password=self.getPassword(),
                database=self.getBasedatos()
            )
            self.cursor = self.conexion.cursor()
            print("Conexión a la base de datos establecida correctamente.")  # Mensaje de éxito
            return 0, "Conexión exitosa"
        except Exception as e:
            print('DRIVER={MySQL};SERVER=' + self.getHost() +
                    ';DATABASE=' + self.getBasedatos() + ';UID=' + self.getUser() +
                    ';PWD=' + self.getPassword(), "Falló Conexión:", str(e))  # Mensaje de error
            return 66, e

    def comprobarConexion(self):
        if self.conexion.is_connected():
            print("Conexión a la base de datos establecida correctamente.")
            return True
        else:
            print("No se pudo establecer la conexión a la base de datos.")
            return False
    def ejecutarSelectOne(self, sql):
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            return 0, datos
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def ejecutarSelectAll(self, sql):
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return 0, datos
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def ejecutarInsert(self, sql):
        try:
            self.cursor.execute(sql)
            self.realizarCommit()
            return 0
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def ejecutarDelete(self, sql):
        try:
            self.cursor.execute(sql)
            self.realizarCommit()
            return 0
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def ejecutarUpdate(self, sql):
        try:
            self.cursor.execute(sql)
            self.realizarCommit()
            return 0
        except Exception as e:
            self.realizarRollback()
            return 1, e

    def getHost(self):
        return self.__hostdb

    def getUser(self):
        return self.__userdb

    def getPassword(self):
        return self.__passwordb

    def getBasedatos(self):
        return self.__basedatosdb

    def realizarCommit(self):
        self.conexion.commit()

    def realizarRollback(self):
        self.conexion.rollback()  

    def desactivarConexion(self):
        self.conexion.close()
