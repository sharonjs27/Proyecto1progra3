import lista


class Empleado():
    def __int__(self):
        self.cedula = " "
        self.nombre = " "
        self.apellido = " "
        self.ocupacion = " "


class Medicamentos:
    def __int__(self):
        self.nombre = ""
        self.compActivo = ""
        self.unidades = ""


productos = []


def registrarEmpleado():
    print("empleado")

    a = Empleado()
    a.nombre = input("ingrese nombre: ")
    a.cedula = input("ingrese cedula: ")
    a.apellido = input("ingrese apellido: ")
    a.ocupacion = input("ingrese ocupacion: ")


def listaEmpleados():
    print("lista empleado")


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
