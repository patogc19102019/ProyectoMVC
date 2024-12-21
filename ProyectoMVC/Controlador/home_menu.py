# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:03:10 2024

@author: Carlos Luco Montofré
"""

class HomeController:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.register_btn.config(command=self.register)
        self.frame.list_btn.config(command=self.lists)
        self.frame.signout_btn.config(command=self.logout)


    def register(self):
        self.view.switch("register")
        
    def lists(self):
        self.model.gestor_datos.recuperar_datos()

    def logout(self):
        self.model.gestor_usuarios.logout()

    def update_view(self):
        current_user = self.model.gestor_usuarios.saludo_usuario()
        if current_user:
            username = current_user["username"]
        else:
            username = 'Set-up sistema'
        self.frame.greeting.config(text=f"Bienvenido, {username}!")

            
