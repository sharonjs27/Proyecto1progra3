import asyncio

import lista

class Singleton:
    _instance = None

    def __init__(self):
        print("Llamado al metodo Init")
        self.nombre = "Soy Unico"

    def __new__(cls, *args, **kwargs):

        if not isinstance(cls._instance, cls):
            print("Llamado al metodo nueva instancia")
            cls._instance = object.__new__(cls)

        return cls._instance
class Empleado:
    def __int__(self, cedula, nombre, apellido, ocupacion):
        self.cedula = " "
        self.nombre = str
        self.apellido = str
        self.ocupacion = str


class Medicamentos:
    def __int__(self):
        self.nombre = ""
        self.compActivo = ""
        self.unidades = ""


def registrarEmpleado():
    print("empleado")

    a = Empleado()
    a.nombre = input("ingrese nombre: ")
    a.cedula = input("ingrese cedula: ")
    a.apellido = input("ingrese apellido: ")
    a.ocupacion = input("ingrese ocupacion: ")


def listaEmpleados():
    print(" lista empleado ")

    datos = []  # inicializar lista vacía para almacenar los datos

    # pedir al usuario que ingrese datos hasta que decida parar
    while True:
        nombre = input("Ingrese el nombre (o 'fin' para terminar): ")
        if nombre == 'fin':
            break  # si el usuario ingresa 'fin', salir del bucle
        edad = int(input("Ingrese la edad: "))
        datos.append((nombre, edad))  # agregar los datos ingresados a la lista

    # mostrar la lista de datos ingresados
    print("Lista de datos ingresados:")
    for nombre, edad in datos:
        print(f"{nombre}: {edad}")

def registrarMedicamento():
    print(" Registro de medicamentos ")

    a = Medicamentos()
    a.nombre = input("ingrese nombre de medicamento: ")
    a.compActivo = input("ingrese compuesto activo: ")
    a.unidades = input("unidades en inventario: ")


def listaMedicamentos():
    print("lista de medicamento")


def horasTrabajo():

  print("horas de trabajo")
  filas = int(input("introduce numero fila"))
  columnas = int(input("introduce numero de columnas"))
  horas_trabajadas = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]
  for i in range(filas):  # Recorre las filas
     for j in range(columnas):  # Recorre las columnas
        horas_trabajadas[i][j] = int(input(f"Ingrese las horas trabajadas por el empleado {i+1} el día {j+1}: "))

  for i in range(filas):
     total_horas = sum(horas_trabajadas[i])
     print(f"El empleado {i+1} trabajó {total_horas} horas esta semana.")
     total_general = sum(sum(horas_trabajadas, []))
     print(f"En total, los empleados trabajaron {total_general} horas esta semana.")


