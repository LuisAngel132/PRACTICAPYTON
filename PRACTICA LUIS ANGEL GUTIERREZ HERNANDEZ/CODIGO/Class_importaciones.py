import pandas as pd
class Datosexportados:

    def __init__(self):
        self.importacion=pd.read_csv('Personas.csv',header=0)
        self.nombre =self.importacion['nombre']
        self.edad =  self.importacion['edad']
        self.celular =  self.importacion['celular']
    def pasardatospersonas(self):
        return self.nombre,self.edad,self.celular

