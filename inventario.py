#Proyecto Grupo #3 Clase Inventario2

from io import open
import os
import sys

class inventario:
    
    #Información sobre prouctos que van estar en el inventario
    cod=["101","102","103","104","105","106","107","108","109","110"]
    nombre=["Pantalon Caballero","Pantalon de Dama","Pantalon Chiquito","Pantalon Chiquita","Blusa Sutida Dama","Camisa Caballero","Camisa para Niño","Blusa para Niñas","Boxer Caballero","Tenis All Star"]
    precio=["28000","23000","19000","20000","15000","17000","12000","13000","10000","35000"]
    proveedor=["De moda S.A.    ","Lontano Jeans    ","Chiquitines S.A.","Chiquitines S.A.","Flor de Liz S.A.","7 Machos S.A.    ","Picaros S.A.    ","Picaros S.A    ","ExtremeCR S.A.","Converse Int S.A."]
    bodega=[34,23,45,12,31,20,27,29,15,19]  

    def getinventario(self):  #Función para mostrar los productos qeu hay en el inventario
        print("                             Inventario Disponible                                    ")
        print("\n        Cod      Descripcion Producto    Precio         Proveedor             stock ")
        for a,b,c,d,e in zip(self.cod,self.nombre,self.precio,self.proveedor,self.bodega):
            print ("\t",a,"\t",b,"\t$",c,"\t",d,"\t",e)
        print("************************************************************************")
    
    def principal(self): #Menu principal del inventario
        print("[1] Mirar inventario")
        print("[2] Modificar disponble de articulos en el Stock")
        print("[3] Eliminar Articulo")
        print("[4] Ingresar producto nuevo")
        print("[5] Salir del programa")
        print("************************************************************************")
        opcion=input("Por favor selecione una opción => ")
        if opcion == "1":
            return self.art_bodega() # En caso de que desee mirar lo que hay en inventario
        elif opcion == "2":
            return self.set_inventario() # En caso de que se desee modificar la cantidad de articulos en el inventario
        elif opcion == "3":
            return self.eliminar() # Eliminar una linea de articulo del inventario
        elif opcion == "4":
            return self.nuevo() # En caso de que desee salir del inventario
        elif opcion == "5":
            print("************************************************************************")
            print("            Gracias por utilizar nuestro Sistema                        ")
            print("************************************************************************")
        else:
            return self.menu() #Si la opcion no es valida me devuelve al menu

    def menu(self):
        os.system("cls") # limpia lo que esta en pantalla
        print("************************************************************************")
        print("              Bienvenido al Menu de inventario                          ")
        print("************************************************************************")
        self.principal() #Me devuelve al menu principal

    def art_bodega(self):
        os.system("cls") #Limpia la pantalla
        print("************************************************************************")
        print("           Este es el inventario actual en la base de datos             ")
        print("************************************************************************")
        self.getinventario() #Muestra el inventario
        print("¿Que desea realizar?")
        print("************************************************************************")
        self.principal() # me devuelve al menu principal

    def nuevo(self): #Permite agregar linea nueva de articulo
        os.system("cls") #limpia lo que esta en pantalla
        print("***************************************************************************")
        self.getinventario() #Permitir ver el inventario actual
        print("Por favor introducir los datos del articulo que desea agregar al inventario")
        print("***************************************************************************")
        self.cod.append(input("Escriba el nuevo código => ")) #Agrega codigo nuevo
        self.nombre.append(input("Escriba el nombre del Articulo => ")) #Agrega descripcion del artículo
        self.precio.append(input("Escriba el precio => ")) #Agrega el precio del artículo
        self.proveedor.append(input("Escriba el proveedor del Artículo => ")) #Agrega al proveedor
        self.bodega.append(input("Escriba el stock en Bodega => ")) #Agrega cuanto hay en bodega
        print("************************************************************************")
        print("El articulo se agrego exitosamente al inventario")
        print("************************************************************************")
        self.getinventario() #Muestra el inventario con los cambios realizados
        print("¿Que desea realizar?")
        self.principal() # Permite saber si deseo realizar algo más o salir

    def eliminar(self): #Permite eliminar una linea existente en el inventario
        os.system("cls") #limpia la pantalla
        print("************************************************************************")
        self.getinventario() #Muestra el inventario
        cod=input("Ingrese el código del articulo que desea eliminar => ") #Codigo del articulo que voy a eliminar
        print("************************************************************************")
        for i in range (len(self.cod)-1,-1,-1): #lee los articulos en el inventario
            if self.cod[i] == cod: #se ubica en el codigo del articulo
                self.cod.pop(i) #Elimina esta codigo
                self.nombre.pop(i) #Elimina esta escripción
                self.precio.pop(i) #Elimina el precio 
                self.proveedor.pop(i) #elimino el proveedor
                self.bodega.pop(i) #elimina lo que hay en bodega
        self.getinventario() #Me muestra el inventario actualizado
        print("El artículo se elmino exitosamente")
        print("************************************************************************")
        print("¿Que desea realizar?")
        self.principal() #Devuelve menu principal

    def set_inventario(self):
        os.system("cls") #Limpia la pantalla
        self.getinventario() #Muestra el inventario actual
        codigo=input("Digite el código para el stock del articulo que desea modificar => ") #Codigo e articulo que deseo eliminar
        nuevo=input("Digite Stock modificado => ") #Stock modificado en el inventario
        for i in range(len(self.cod)): #Lee la lista buscano la posion del codigo
            if self.cod[i] == codigo: #se posi bciona en la ubicacion del codigo
                self.bodega[i] = nuevo # Modifica el stock en esa posición
        print("************************************************************************")
        self.getinventario() #Inventario Modificado
        print("El artículo se modifico exitosamente")
        print("************************************************************************")
        print("¿Que desea realizar?")
        self.principal() #Devuelve menu principal
#existencia=inventario()
#existencia.menu()
