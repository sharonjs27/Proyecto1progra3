import os

# patrón de diseño
def singleton(cls):
    instances =dict()
    def wrap(*args, **kwargs):
        if cls not in instances:
            print("llamado instancia  ")
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
class User(object):
    def __init__(self, username):
        print("llamado instancia nueva")
        self.username = username



class Empleado:
    def __init__(self, nombre, apellido, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.ocupacion = ocupacion

    def get_Nombre(self):
        return self.nombre

    def get_Apellido(self):
        return self.apellido

    def get_ocupacion(self):
        return self.ocupacion


class Medicamentos:
    def __init__(self, nombre, compActivo, unidades):
        self.nombre = nombre
        self.compActivo = compActivo
        self.unidades = unidades

    def get_nombre(self):
        return self.nombre

    def get_comActivo(self):
        return self.compActivo

    def get_unidades(self):
        return self.unidades


#################################################
def registrarEmpleado(datos):
    print("empleado")

    # el usuario registra los datos
    while True:
        nombre = input("Ingrese el nombre (o '0' para terminar): ")
        if nombre == '0':
            break  # si el usuario ingresa '0', se sale del registrar

        apellido = input("Ingrese el apellido: ")
        ocupacion = input("Ingrese la ocupación: ")
        nuevoEmpleado = Empleado(nombre, apellido, ocupacion)

        datos.append(nuevoEmpleado)  # se guardan los empleados ingresados a la lista
def listaEmpleados(datos):
    print("Lista de datos ingresados:")
    for nuevoEmpleado in datos:
        print(f"Empleado {nuevoEmpleado.nombre} Apellido: {nuevoEmpleado.apellido} Ocupación: ({nuevoEmpleado.ocupacion})")
    os.system('pause')


def registrarMedicamento(inventario):
    print(" Registro de medicamentos ")
    # se registra los datos de los medicamentos
    while True:
        nombre = input("Ingrese el nombre (o '0' para terminar): ")
        if nombre == '0':
            break  # si el usuario ingresa '0', se sale del registrar
        compActivo = input("Ingrese el compuesto activo: ")
        unidades = input("Ingrese la unidades: ")
        nuevoMedicamento = Medicamentos(nombre, compActivo, unidades)

        inventario.append(nuevoMedicamento)  # agregar los datos ingresados a la lista


def listaMedicamentos(inventario):
    print("lista de medicamento")

    for nuevoMedicamento in inventario:
        print(f" Medicamento {nuevoMedicamento.nombre}Compuesto: {nuevoMedicamento.compActivo} Unidades: {nuevoMedicamento.unidades}")
    os.system('pause')


def horasTrabajo():
    print("horas de trabajo")
    filas = int(input("Digite número de empleados: "))
    columnas = int(input("Digite número de días de la semana trabajadas: "))
    horas_trabajadas = [[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
    for i in range(filas):  # Recorre la fila de cada empleado
        for j in range(columnas):  # Recorre la columna de cada día
            horas_trabajadas[i][j] = int(
                input(f"Ingrese las horas trabajadas por el empleado {i + 1} el día {j + 1}: "))

    # se suma las horas trabajadas de cada empleado
    for i in range(filas):
        total_horas = sum(horas_trabajadas[i])
        print(f"El empleado {i + 1} trabajó {total_horas} horas esta semana.")

 # se calcula el salario semanal de cada Empleado
    for i in range(filas):
        salario = sum(horas_trabajadas[i]) * 2000
        print(f"El empleado {i + 1} tiene un salario de: {salario} esta semana.")

        # se calcula el rebajo de seguro
    for i in range(filas):
        salario = sum(horas_trabajadas[i]) * 2000
        seguro = salario - 5000
        print(f"El empleado {i + 1} tiene un salario de: {seguro} con el seguro rebajado ")

    # muestra los las horas ingresadas
    print("Horas trabajas: ")
    for i in range(filas):
        for j in range(columnas):
            print(horas_trabajadas[i][j], end=" ")
        print()

    # Solicita al usuario que elija si desea modificar, eliminar o salir
    accion = input("¿Desea modificar, eliminar un valor o salir? (m/e/s): ")

    # Para modificar un valor, solicitar fila, columna y nuevo valor que desea otorgar
    if accion == "m":
        filas = int(input("Ingrese la fila donde se encuentra el valor que desea modificar: "))
        columnas = int(input("Ingrese la columna donde se encuentra el valor que desea modificar: "))
        nuevo_valor = int(input(f"Ingrese el nuevo valor para la posición [{filas},{columnas}]: "))
        horas_trabajadas[filas - 1][columnas - 1] = nuevo_valor

    # Para eliminar un valor, solicita en que posición el valor que desea eliminar
    elif accion == "e":
        filas = int(input("Ingrese la fila donde se encuentra el valor que desea eliminar: "))
        columnas = int(input("Ingrese la columna donde se encuentra el valor que desea eliminar: "))
        horas_trabajadas[filas-1][columnas-1] = 0

    # Muestra matriz editada con los valores nuevos
    print("Horas actualizadas:")
    for i in range(len(horas_trabajadas)):
        for j in range(len(horas_trabajadas[0])):
            print(horas_trabajadas[i][j], end=" ")
        print()
