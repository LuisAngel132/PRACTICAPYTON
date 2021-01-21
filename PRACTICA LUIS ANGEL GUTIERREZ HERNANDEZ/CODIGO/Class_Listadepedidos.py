class Listadepedidos:
    def __init__(self, id=None, nombre="",producto=""):
        self.idp = id
        self.nombre = nombre
        self.producto = producto
        self.list = []
        self.x = 0
    def agregarlistadepedido(self, nombre, producto):
        self.x += 1
        self.idp = self.x
        new = Listadepedidos(self.idp, nombre, producto)
        self.list.append(new)

    def actualizarproducto(self,  nombre, producto):
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
                new = Listadepedidos(g, nombre,producto)
                self.list[c] = new
            e = 1
        if (e == 0):
          print("Lo sentimos la Persona no se encuentra Disponible")

    def eliminarpedido(self, nombre=None):
        c = 0
        for element in self.list:

            if (element.nombre == nombre):
                self.list.pop(c)

            c += 1

    def verlistadepedios(self, nombre=None):
        c = 0
        a = 0
        if (nombre != None):

            for element in self.list:

                if (element.nombre == nombre):
                    return self.list[c]
                    a = 1
                c += 1
            if (a == 0):
                nombre = ""
                idp = ""
                producto = ""
                new = Pedidos(idp, nombre, producto)

                return new

        else:
            return self.list


