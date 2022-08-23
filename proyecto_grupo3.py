import os
import sys

class inventario:

    cod=["101","102","103","104","105","106","107","108","109","110"]
    nombre=["Pantalon Caballero","Pantalon de Dama","Pantalon Chiquito","Pantalon Chiquita","Blusa Sutida Dama","Camisa Caballero","Camisa para Niño","Blusa para Niñas","Boxer Caballero","Tenis All Star"]
    precio=["28000","23000","19000","20000","15000","17000","12000","13000","10000","35000"]
    proveedor=["De moda S.A.    ","Lontano Jeans    ","Chiquitines S.A.","Chiquitines S.A.","Flor de Liz S.A.","7 Machos S.A.    ","Picaros S.A.    ","Picaros S.A    ","ExtremeCR S.A.","Converse Int S.A."]
    bodega=[34,23,45,12,31,20,27,29,15,19]   

    def menu(self):
        os.system("cls")
        print("************************************************************************")
        print("              Bienvenido al Menu de inventario                          ")
        print("************************************************************************")
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
            return self.agregar_rebajar()
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

    def art_bodega(self):
        os.system("cls")
        print("************************************************************************")
        print("           Este es el inventario actual en la base de datos             ")
        print("************************************************************************")
        print(        "\n        Cod      Descripcion Producto    Precio         Proveedor             stock ")
        for c,d,p,q,s in zip(self.cod,self.nombre,self.precio,self.proveedor,self.bodega):
            print ("\t",c,"\t",d,"\t",p,"\t",q,"\t",s)
        print("************************************************************************")
        print("¿Que desea realizar?")
        print("[m] Volver al menu")
        print("[s] Salir")
        print("************************************************************************")
        opcion=input("Selecciones una opcion => ")
        if opcion == "m":
            return self.menu()
        elif opcion == "s":
            print("************************************************************************")
            print ("Gracias por utilizar nuestro sistema")
        else:
            return self.art_bodega()

    def nuevo(self):
        os.system("cls")
        print("***************************************************************************")
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
        print("\n        Cod      Descripcion Producto    Precio         Proveedor             stock ")
        for a,b,c,d,e in zip(self.cod,self.nombre,self.precio,self.proveedor,self.bodega):
            print ("\t",a,"\t",b,"\t$",c,"\t",d,"\t",e)
        print("************************************************************************")
        print("¿Que desea realizar?")
        print("[a] Agregar más articulos")
        print("[m] Volver al menu")
        print("[s] Salir")
        print()  
        opcion=input("Selecciones una opcion => ")
        if opcion == "a":
            return self.nuevo()
        elif opcion == "m":
            return self.menu()
        elif opcion == "s":
            print("************************************************************************")
            print ("Gracias por utilizar nuestro sistema")
            print("************************************************************************")

    def eliminar(self):
        os.system("cls")
        print("************************************************************************")
        cod=input("Ingrese el código del articulo que desea eliminar => ")
        for i in range (len(self.cod)-1,-1,-1):
            if self.cod[i] == cod:
                self.cod.pop(i)
                self.nombre.pop(i)
                self.precio.pop(i)
                self.proveedor.pop(i)
                self.bodega.pop(i)
        print("\n        Cod      Descripcion Producto    Precio         Proveedor             stock ")
        for a,b,c,d,e in zip(self.cod,self.nombre,self.precio,self.proveedor,self.bodega):
            print ("\t",a,"\t$",b,"\t",c,"\t",d,"\t",e)
        print("************************************************************************")
        print("El artículo seleccionado se elimino exitosamente")
        print("************************************************************************")
        print("¿Que desea realizar?")
        print("[e] Eliminar más artículos")
        print("[m] Volver al menu")
        print("[s] Salir")
        print("************************************************************************")
        opcion=input("Selecciones una opcion => ")
        if opcion == "e":
            return self.eliminar()
        if opcion == "m":
            return self.menu()
        elif opcion == "s":
            print ("Gracias por utilizar nuestro sistema")
            print("************************************************************************")
        else:
            return self.nuevo()

    def agregar_rebajar(self):
        os.system("cls")
        print("************************************************************************")
        print("            Desea Agregar o Restar producto del Stock?                  ")
        print("************************************************************************")
        print("[1] Agregar")
        print("[2] Eliminar")
        print("************************************************************************")
        opcion=input("Por Favor seleccione una opción => ")
        if opcion == "1":
            os.system("cls")
            print("************************************************************************")
            cod=input("Por Favor ingrese Código del Artículo => ")
            adicion=int(input("Por Favor ingrese la cantidad que se va a agregar al Stock => "))
        if opcion == "2":
            print("************************************************************************")
            print("\n        Cod      Descripcion Producto    Precio         Proveedor             stock ")
            for a,b,c,d,e in zip(self.cod,self.nombre,self.precio,self.proveedor,self.bodega):
                print ("\t",a,"\t$",b,"\t",c,"\t",d,"\t",e)
            print("************************************************************************")
            cod=input("Ingrese el código del articulo => ")
            cant=int(input("Ingrese la cantidad que se va a rebajar => "))
            for i in range (len(self.cod)):
                self.bodega[i] == cod
        print("************************************************************************")
        print("Se rebajo exitosamente la existencia en el inventario")
        print("************************************************************************")
        print("¿Que desea realizar?")
        print("[e] Eliminar/agergar artículos")
        print("[m] Volver al menu")
        print("[s] Salir")
        print("************************************************************************")
        opcion=input("Selecciones una opcion => ")
        if opcion == "e":
            return self.agregar_rebajar()
        if opcion == "m":
            return self.menu()
        elif opcion == "s":
            print("************************************************************************")
            print ("Gracias por utilizar nuestro sistema")
            print("************************************************************************")

existencia=inventario()
existencia.menu()

