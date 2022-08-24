#Proyecto Grupo #3 Clase Inventario2

import os
import sys

class inventario:

    cod=["101","102","103","104","105","106","107","108","109","110"]
    nombre=["Pantalon Caballero","Pantalon de Dama","Pantalon Chiquito","Pantalon Chiquita","Blusa Sutida Dama","Camisa Caballero","Camisa para Niño","Blusa para Niñas","Boxer Caballero","Tenis All Star"]
    precio=["28000","23000","19000","20000","15000","17000","12000","13000","10000","35000"]
    proveedor=["De moda S.A.    ","Lontano Jeans    ","Chiquitines S.A.","Chiquitines S.A.","Flor de Liz S.A.","7 Machos S.A.    ","Picaros S.A.    ","Picaros S.A    ","ExtremeCR S.A.","Converse Int S.A."]
    bodega=[34,23,45,12,31,20,27,29,15,19]  

    def getinventario(self): 
        print("                             Inventario Disponible                                    ")
        print("\n        Cod      Descripcion Producto    Precio         Proveedor             stock ")
        for a,b,c,d,e in zip(self.cod,self.nombre,self.precio,self.proveedor,self.bodega):
            print ("\t",a,"\t",b,"\t$",c,"\t",d,"\t",e)
        print("************************************************************************")
    
    def principal(self):
        print("[1] Mirar inventario")
        print("[2] Agregar o rebajar articulos en el Stock")
        print("[3] Eliminar Articulo")
        print("[4] Ingresar producto nuevo")
        print("[5] Salir del programa")
        print("************************************************************************")
        opcion=input("Por favor selecione una opción => ")
        if opcion == "1":
            return self.art_bodega()
        elif opcion == "2":
            return self.set_inventario()
        elif opcion == "3":
            return self.eliminar()
        elif opcion == "4":
            return self.nuevo()
        elif opcion == "5":
            print("************************************************************************")
            print("            Gracias por utilizar nuestro Sistema                        ")
            print("************************************************************************")
        else:
            return self.menu()

    def menu(self):
        os.system("cls")
        print("************************************************************************")
        print("              Bienvenido al Menu de inventario                          ")
        print("************************************************************************")
        self.principal()

    def art_bodega(self):
        os.system("cls")
        print("************************************************************************")
        print("           Este es el inventario actual en la base de datos             ")
        print("************************************************************************")
        self.getinventario()
        print("¿Que desea realizar?")
        print("************************************************************************")
        self.principal()

    def nuevo(self):
        os.system("cls")
        print("***************************************************************************")
        self.getinventario()
        print("Por favor introducir los datos del articulo que desea agregar al inventario")
        print("***************************************************************************")
        self.cod.append(input("Escriba el nuevo código => "))
        self.nombre.append(input("Escriba el nombre del Articulo => "))
        self.precio.append(input("Escriba el precio => "))
        self.proveedor.append(input("Escriba el proveedor del Artículo => ")) 
        self.bodega.append(input("Escriba el stock en Bodega => "))
        print("************************************************************************")
        print("El articulo se agrego exitosamente al inventario")
        print("************************************************************************")
        self.getinventario()
        print("¿Que desea realizar?")
        self.principal()

    def eliminar(self):
        os.system("cls")
        print("************************************************************************")
        self.getinventario()
        cod=input("Ingrese el código del articulo que desea eliminar => ")
        print("************************************************************************")
        for i in range (len(self.cod)-1,-1,-1):
            if self.cod[i] == cod:
                self.cod.pop(i)
                self.nombre.pop(i)
                self.precio.pop(i)
                self.proveedor.pop(i)
                self.bodega.pop(i)
        self.getinventario()
        print("El artículo se elmino exitosamente")
        print("************************************************************************")
        print("¿Que desea realizar?")
        self.principal()

    def set_inventario(self):
        os.system("cls")
        self.getinventario()
        codigo=input("Digite el código para el stock del articulo que desea modificar => ")
        nuevo=input("Digite Stock modificado => ")
        for i in range(len(self.cod)):
            if self.cod[i] == codigo:
                self.bodega[i] = nuevo
        print("************************************************************************")
        self.getinventario() 
        print("El artículo se modifico exitosamente")
        print("************************************************************************")
        print("¿Que desea realizar?")
        self.principal()
#existencia=inventario()
#existencia.menu()
