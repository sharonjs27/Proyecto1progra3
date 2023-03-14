import funciones


print(' *** BIENVENIDOS A BASE DE DATOS ***')
menu = int (input("MENU \n1: registrar empleado \n2: mostrar lista de empleados \n3: registrar medicamento \n4: lista de medicamentos \n5: horas trabajadas \n6: Salir "))

while menu != 6:
    if menu == 1:
       funciones.registrarEmpleado()
    elif menu == 2:
       funciones.listaEmpleados()
    elif menu == 3:
        funciones.registrarMedicamento()
    elif menu == 4:
        funciones.listaMedicamentos()
    elif menu == 5:
        funciones.horasTrabajo()
    else:
        print ("digete la opcion correcta")
    menu = int(input(
        "MENU \n1: registrar empleado \n2: mostrar lista de empleados \n3: registrar medicamento \n4: lista de medicamentos \n5: horas trabajadas \n6: Salir "))





