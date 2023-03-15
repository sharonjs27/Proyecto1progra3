import asyncio

import lista


class Empleado:
    def __int__(self,cedula, nombre, apellido, ocupacion):
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
