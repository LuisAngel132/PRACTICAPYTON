from datetime import datetime
from io import open


class Pedidos:
    def __init__(self, id=None, nombre="", fecha=""):
        self.idp = id
        self.nombre = nombre
        self.fechacaducacion = fecha
        self.list = []
        self.x = 0

    def agregarproducto(self, nombre, fecha):
        self.x += 1
        self.idp = self.x
        new = Pedidos(self.idp, nombre, fecha)
        self.list.append(new)

    def actualizarproducto(self,  nombre, fecha):
        c = 0
        e = 0
        s = 0
        for element in self.list:

            if (element.nombre == nombre):

                g = element.idp
                s = 1
            else:
                if (element.idp != ""):
                    if (s == 0):
                        c += 1
            if (s == 1):
                d = 0
                new = Pedidos(g, nombre,fecha)
                self.list[c] = new
            e = 1
        if (e == 0):
          print("Lo sentimos la Persona no se encuentra Disponible")

    def eliminarproducto(self, nombre=None):
        c = 0
        for element in self.list:

            if (element.nombre == nombre):
                new = Pedidos(element.idp,  nombre, element.fechacaducacion)
                self.list.pop(c)

            c += 1

    def verproductos(self, nombre=None):
        c = 0
        a=0
        if (nombre != None):

            for element in self.list:

                if (element.nombre == nombre):
                    return self.list[c]
                    a=1
                c += 1
            if (a == 0):
                nombre = ""
                idp = ""
                fecha = ""
                new = Pedidos(idp, nombre, fecha )

                return new

        else:
           return self.list


