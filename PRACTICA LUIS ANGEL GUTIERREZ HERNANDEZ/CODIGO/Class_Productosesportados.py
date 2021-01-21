import pandas as pd
class DProductos:

    def __init__(self):
        self.importacion =pd.read_csv('Productos.csv', header=0)
        self.nombre = self.importacion['nombre']
        self.fechadecaducacion = self.importacion['fechadecaducacion']

    def Extraerdatos(self):
        return self.nombre, self.fechadecaducacion
