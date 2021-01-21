from Class_Deportiva import Persona
from Class_Pedidos import  Pedidos as Pe
from Class_Listadepedidos import Listadepedidos as L
from Class_importaciones import Datosexportados as D
from Class_Productosesportados import  DProductos
from Class_DatoslistaImportados import ListaExportada as Li
import pandas as pd
import  csv


if __name__ == "__main__":
 Datos=DProductos()
 E=D()
 l=L()
 P=Pe()
 Ll=Li()
 lista = Persona()
accion=0
E.pasardatospersonas()
Datos.Extraerdatos()
Ll.pasardatospersonas()
for j in range(len(E.nombre)):
     nombre2=''.join(E.nombre[j])
     edad2=str( E.edad[j])
     celular2=str(E.celular[j])
     lista.agregarpersona(nombre2, edad2, celular2)
for j in range(len(Datos.nombre)):
     nombre2=''.join(Datos.nombre[j])
     fechadecaducacion2=str( Datos.fechadecaducacion[j])
     P.agregarproducto(nombre2, fechadecaducacion2)
for j in range(len(Ll.nombre)):
     nombre2=''.join(Ll.nombre[j])
     producto2=str( Ll.producto[j])
l.agregarlistadepedido(nombre2,producto2)



while accion >=0 and accion <=16:
    print("***********************************************************************************************************")
    print("| Centro Deportivo                        ||  9.- Eliminar Producto                                       |")
    print("| 1.  Usuario nuevo                       ||  10.- Reporte en especial Por Producto                       |")
    print("| 2.- Ver usuarios                        ||  11.  Rentar producto                                        |")
    print("| 3.- Actualizar Usuario                  ||  12.- Ver Los productos rentados                             |")
    print("| 4.- Eliminar Usuario                    ||  13.- Eliminar productos rentados                            |")
    print("| 5.- Reporte en especial Por usuario     ||  14  Actualizar productos rentados                           |")
    print("| 6.  Producto nuevo                      ||  15  Consulta de la persona o el producto de los pedidos     |")
    print("| 7.- Ver Productos                       ||  16 Salir                                                    |")
    print("| 8.- Actualizar Producto                 ||                                                              |")
    print("***********************************************************************************************************")

    accion = int(input("Seleccione una opcion:"))
    if accion == 1:
        nombre = input("Ingrese su nombre: ")
        edad = input("su edad: ")
        celular = input("ingrese su celular:")
        lista.agregarpersona(nombre,edad,celular)
    elif accion == 2:
        objeto = lista.verpersonas()
        for i in objeto:
            print(str(i.idp) + " " + i.nombre + " " + i.edad + " " + i.celular)
    elif accion == 3:
        objeto = lista.verpersonas()
        for i in objeto:
            print(str(i.idp) + " " + i.nombre + " " + i.edad + " " + i.celular)
        numero = input("ingrese su nombre:")
        edad = input("su nueva edad: ")
        celular = input("su nuevo celular:")
        lista.actualizarpersona(numero,edad,celular)
    elif accion == 4:
        objeto = lista.verpersonas()
        for i in objeto:
            print(str(i.idp) + " " + i.nombre + " " + i.edad + " " + i.celular)
        numero = input("Ingresa el nombre de usuario a eliminar:")
        lista.eliminarpersona(numero)
    elif accion == 5:
        nombre = input("Ingresa al usuario que deseas ver:")
        i = lista.verpersonas(nombre)
        if(i.nombre!=""):
            print(str(i.idp) + " " + i.nombre + " " + i.edad + " " + i.celular)
    elif accion == 6:
        nombre = input("Ingrese el Producto: ")
        fecha = input("fecha de caducacion: ")
        P.agregarproducto(nombre,fecha)
    elif accion == 7:
        objeto2 = P.verproductos()
        for i in objeto2:
            if (i.nombre != ""):
                 print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
    elif accion == 8:
        objeto2 = P.verproductos()
        for i in objeto2:
            print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
        nombre = input("Ingrese el Producto: ")
        fecha = input("fecha de caducacion: ")
        P.actualizarproducto(nombre,fecha)
    elif accion == 9:
        objeto2 = P.verproductos()
        for i in objeto2:
            print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
        nombre = input("Ingrese el Producto a eliminar: ")
        P.eliminarproducto(nombre)
    elif accion == 10:
        nombre = input("Ingrese el Producto a ver: ")
        i = P.verproductos(nombre)
        if (i.nombre != ""):
             print(str(i.idp) + " " + i.nombre + " " + i.fechacaducacion)
    elif accion == 11:
        s=0
        f=0
        print("-----------------USUARIOS A SELECCIONAR--------------------")
        objeto = lista.verpersonas()
        for i in objeto:
            print("||"+str(i.idp) + " " + i.nombre + " " + i.edad +" "+i.celular+"||")
        print("-----------------PRODUCTOS A SELECCIONAR--------------------")
        objeto2 = P.verproductos()
        for i in objeto2:
            print("||"+str(i.idp) + " " + i.nombre + " " + i.fechacaducacion+"||")
        print("***********************************************************")
        name = input("Ingresa al usuario de la lista:")
        objeto = lista.verpersonas()
        for i in objeto:
          if (i.nombre==name):
               s=1
               persona=i.nombre
        if(s==1):
            producto = input("Ingrese el Producto a ver: ")
            i = P.verproductos(producto)
            if (i.nombre != ""):
               l.agregarlistadepedido(persona,i.nombre)
            else:
              f=1
        if(f==1):
            print("no se encuentra el producto")
        if(s==0):
         print("no existe el usuario")
    elif accion==12:
        objeto3=l.verlistadepedios()
        for i in objeto3:
            if (i.nombre != ""):
                print(str(i.idp) +" "+i.nombre+" "+i.producto)
    elif accion==13:
        objeto3=l.verlistadepedios()
        for i in objeto3:
            print(str(i.idp) + " " + i.nombre + " " + i.producto)
        nombre = input("Ingrese el Producto a eliminar: ")
        l.eliminarpedido(nombre)
    elif accion == 14:

        print("-----------------USUARIOS Y SUS PRODUCTOS A SELECCIONAR--------------------")
        objeto3 = l.verlistadepedios()
        for i in objeto3:
            s=0
            print("||" + str(i.idp) + " " + i.nombre + " " + i.producto + "||")
        print("***********************************************************")

        name = input("Ingresa al usuario que cambiara su producto:")
        objeto3 = lista.verpersonas()
        for i in objeto3:
            if (i.nombre == name):
                 s = 1
        if (s == 1):
            print("-----------------PRODUCTOS A SELECCIONAR--------------------")
            objeto2 = P.verproductos()
            for i in objeto2:
                print("||" + str(i.idp) + " " + i.nombre + " " + i.fechacaducacion + "||")
            print("***********************************************************")
            producto = input("Ingrese el Producto nuevo: ")
            i = P.verproductos(producto)
            if(i.nombre!=""):
               l.actualizarproducto(name,i.nombre)
        if (s == 0):
                print("no existe el usuario")



    elif accion == 15:
        print("1.  Busqueda por persona")
        print("2.- Busqueda por producto")
        seleccion = int(input("Seleccione una opcion:"))
        if seleccion==1:

            objeto3 = l.verlistadepedios()
            for i in objeto3:
                s = 0
                print("||"  + i.nombre  + "||")
            print("***********************************************************")
            name = input("Ingresa al usuario que desea ver:")
            i = l.verlistadepedios(name)
            if(i.nombre!=""):
                f=lista.verpersonas(i.nombre)
                if(f.nombre!=""):
                    print(str(f.idp) + " " + f.nombre + " " + f.edad + " " + f.celular)
        elif seleccion==2:
            objeto3 = l.verlistadepedios()
            for i in objeto3:
                s = 0
                print("||" +i.nombre+"=>" + i.producto + "||")
            print("***********************************************************")
            name = input("Ingresa el usuario:")
            i = l.verlistadepedios(name)
            if (i.producto != ""):
                f = P.verproductos(i.producto)
                if (f.nombre != ""):
                    print(str(f.idp) + " " + f.nombre + " " + f.fechacaducacion)
    elif accion == 16:
       personas=open("Personas.csv","r+",newline="")
       texto="idp"+","+"nombre"+","+"edad"+","+"celular"
       personas.write(texto)
       objeto = lista.verpersonas()
       for i in objeto:
           personas.write('\n'+str(i.idp)+","+ i.nombre +","+i.edad+","+i.celular)
       personas.close()



       listadeproductos = open("Listadepedidos.csv", "r+", newline="")
       texto = "idp" + "," + "nombre" + "," + "producto"
       listadeproductos.write(texto)
       objeto = l.verlistadepedios()
       for i in objeto:
           listadeproductos.write('\n'+str(i.idp) + ","+i.nombre+","+i.producto)
       listadeproductos.close()

       listadeproductos = open("Producto.csv", "r+", newline="")
       texto = "idp" + "," + "nombre" + "," + "fechadecaducacion"
       listadeproductos.write(texto)
       objeto = P.verproductos()
       for i in objeto:
           listadeproductos.write('\n'+str(i.idp) +","+i.nombre+","+i.fechacaducacion)
       listadeproductos.close()
       accion=20