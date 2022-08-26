# El siguiente programa es diseñado para el Proyecto Final de Python en Main
# Estudiantes: Maria Milena, Eduarth, Josebeth y Maria Paz
print("INICIAR SECCION ")
ingresar=input("Digite [si] para entrar o [no] para salir:  ")

while ingresar == "si":   #metodo while para entrar 
    usuario1=input("Digite su Usuario: ") #El login nos da Error y no pasa el while para avanzar
    contraseña=input("Digite su contraseña: ")
    if usuario1=="administrador" and contraseña == "adm123": #entrar al menú verificando su contraseña
        print("-------------------------------------------------------------------------------")
        print("                    BIENVENIDO AL SISTEMA                             ")
        menu=input("Si desea entrar al menu digite [ M ] o [ S ] para salir:  ")
        print("-------------------------------------------------------------------------------")
        while menu== "M":        #metodo para escoger la opcion e ingresar al modulo
            if menu == "M":
                print("----------------------------------------------------")
                print("               MENU PRINCIPAL DE OPERACIONES        ")
                print("----------------------------------------------------")
                print("  [ 1 ] INVENTARIO                 [ 3 ] CLIENTE    ")
                print("  [ 2 ] PROVEEDORES                [ 4 ] FACTURACIÓN ")
                print("                [ S ] SALIR DEL SISTEMA                ")
                modulo=input("Ingrese el número para entrar al modúlo: ")
                if modulo== "1":
                    from inventario import inventario #importación del Grupo de inventario
                    existencia=inventario() #llamado de impresion 
                    existencia.menu()
                elif modulo == "2":
                    from proveedores import proveedores  #importacion del Grupo de Proveedores
                    imprecion_Menu=proveedores() 
                    imprecion_Menu() #llamado de impresion 
                    print("\n""\t\t\t\t\t""Provedores""\t\t\t\t\t""\n")#Rotúlos del Menú.
                    print("\n""Identidad","Nombre","\t","Representante","\t\t","Telefono","\t","Correo""\n")
                    imprimir_proveedores=proveedores
                    imprimir_proveedores()
                    seleccion_de_Menu=proveedores
                    seleccion_de_Menu() 
                elif modulo == "3":
                    from cliente import Cliente #importacion de la clase y funcion del grupo Clientes
                elif modulo == "4":
                    from facturacion import facturacion #importacion del Grupo de facturacíon, el llamado no se logro porque no funciona
                else:
                    print("Se cerro su sección exitosamente") #metodo para cerrar
            else:
                print("Cerro su seccion exitosamente")
    else:
        print("-----------------------------------")
        print(" Usuario o contraseña incorrecta")
        print("INICIAR SECCION ")
        usuario1=input("Digite su Usuario: ") #El login nos da Error y no pasa el while para avanzar
        contraseña=input("Digite su contraseña: ")
print ("su seccion se cerro")
