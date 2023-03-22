import funciones

datos = []
menu = ""

while menu != "6":

    print('\n*** BIENVENIDO A BASE DE DATO ***')
    menu = input('MENU \n1: registrar empleado \n2: mostrar lista de empleados \n3: registrar medicamentos \n4: lista de medicamentos \n5: horas trabajadas \n6: Salir \n\n Escriba la opción que desea: ')

    if menu == "1":
        funciones.registrarEmpleado(datos)
    elif menu == "2":
        funciones.listaEmpleados(datos)
    elif menu == "3":
        funciones.registrarMedicamento()
    elif menu == "4":
        funciones.listaMedicamentos()
    elif menu == "5":
        funciones.horasTrabajo()

