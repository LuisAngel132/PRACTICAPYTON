import pandas as pd
class ListaExportada:

    def __init__(self):
        self.importacion=pd.read_csv('Listadepedidos.csv',header=0)
        self.nombre =self.importacion['nombre']
        self.producto =  self.importacion['producto']
    def pasardatospersonas(self):
        return self.nombre,self.producto

