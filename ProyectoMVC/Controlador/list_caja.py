# ventana_list_cajas.py
from tkinter import Label, Listbox, Button, Tk

class VentanaListCajas:
    def __init__(self, *args, **kwargs):
        self.root = Tk()
        self.header = Label(self.root, text="Cajas Activas")
        self.listaDatos = Listbox(self.root)
        self.return_datos = Button(self.root, text="Retornar")

    def listar_datos(self, lista_DTO):
        self.listaDatos.delete(0, 'end')
        for item in lista_DTO:
            self.listaDatos.insert('end', item)

    def run(self):
        self.header.pack()
        self.listaDatos.pack()
        self.return_datos.pack()
        self.root.mainloop()
