from datetime import datetime
from io import open

class Persona:

    def __init__(self,id=None,nombre="", edad="",celular=""):
        self.idp=id
        self.nombre = nombre
        self.edad = edad
        self.celular=celular
        self.list = []
        self.x=0




    def agregarpersona(self,nombre,edad,celular):

                self.x+=1
                self.idp=self.x
                new=Persona(self.idp,nombre,edad,celular)
                return self.list.append(new)

    def actualizarpersona(self,nombre,edad,celular):
        c=0
        e=0
        s=0
        for element in self.list:

          if(element.nombre==nombre):

            g=element.idp
            s=1
          else:
              if (element.idp != ""):
                  if(s==0):
                     c+=1
        if (s == 1):
               d = 0
               new = Persona(g, nombre, edad, celular)
               self.list[c] = new
        e=1
        if (e == 0):
          print("Lo sentimos la Persona no se encuentra Disponible")


    def eliminarpersona(self, nombre=None):
        c = 0
        for element in self.list:

            if (element.nombre == nombre):

                new = Persona(element.idp,element.nombre,element.edad,element.celular)
                self.list.pop(c)

            c += 1

    def verpersonas(self, nombre=None):
        c = 0
        a=0
        if(nombre!=None):

          for element in self.list:

            if (element.nombre == nombre):
                return self.list[c]
                a=1
            c += 1
          if(a==0):
              nombre =""
              edad=""
              idp=""
              celular=""
              new = Persona(idp, nombre, edad, celular)

              return new
        else:
            return self.list

        # Menu
