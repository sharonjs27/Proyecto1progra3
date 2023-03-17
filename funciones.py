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

    print("lista empleados: ", lista)


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
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor = float(input("Empleado{} DIA {} : ".format(i + 1, j + 1)))
            matriz[i].append(valor)
    print()

    for fila in matriz:
        print("[", end=" ")
        for elemento in fila:
            print("{:8.2f}".format(elemento), end="")

