from socios import Socios
from controlador import Controlador
from datetime import datetime


controlador = Controlador()


while True:

    print("Actualmente hay ",controlador.numSocios()," socios")
    print("1.- Añadir Socio")
    print("2.- Eliminar Socio")
    print("3.- Listar Socios")
    print("4.- Registrar Productos")
    print("5.- Actualizar Saldo")
    print("6.- Ficha de Socio")
    print("7.- Salir")


    while True:
        try:

            op=int(input("Introduce opción:"))

            if op>=1 and op<=7:
                break
            else: 
                print("Introduce un numero del 1 al 7!")

        except ValueError:
            print("Introduce un numero!")


    if op==7:
        break


    if op==1:
        print()
        id_socio=input("Introduce el id del socio: ")
        dni=input("Introduce el dni del socio: ")
        nombre=input("Introduce el nombre del socio: ")
        apellidos=input("Introduce los apellidos del socio: ")
        fecha= datetime.now()
        hoy = str(fecha.strftime("%d-%m-%Y"))

        socio = Socios(id_socio,dni,nombre,apellidos,hoy)

        if controlador.addSocio(socio):
            print("Socio añadido correctamente!")
        else:
            print("Error al añadir el socio!")

        print()


    if op==2:
        print()
        id_socio=input("Introduce el id del socio a eliminar: ")


        if controlador.delSocio(id_socio):
            print("Socio eliminado correctamente!")
        else:
            print("Error al eliminar el socio!")

        print()


    if op ==3:
        print()
        print("Socios: ")

        for i in controlador.listarSocios():
            print(i)

        print()



    if op ==4:
        print()
        print("Registrando productos...")
        id_socio=input("Introduce el id del socio: ")

        print("Productos:")
        print(controlador.getProductos())
        producto=input("Introduce el nombre del producto: ")

        kilos=input("Introduce el numero de kilos: ")

        if controlador.addProducto(id_socio,producto,kilos):
            print("Producto añadido correctamente!")
        else:
            print("Error al añadir el producto!")

        print()

    if op ==5:
        print()

        id_socio=input("Introduce el id del socio: ")
        if controlador.actualizaSaldo(id_socio):
            print("Saldo actualizado correctamente!")
        else:
            print("Error al actualizar saldo!")



        print()


    if op==6:
        print()


        id_socio=input("Introduce el id del socio: ")

        print(controlador.fichaSocio(id_socio))


        print()

