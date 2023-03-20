import asyncio

import lista

class Empleado:
    def __init__(self, nombre, apellido, ocupacion ):
        self.nombre = nombre
        self.apellido = apellido
        self.ocupacion = ocupacion

    def __str__(self):
        return f"El empleado {self.nombre} apellido {self.apellido} ocupacion {self.ocupacion}."


class Medicamentos:
    def __init__(self, nombre, compActivo, unidades):
        self.nombre = nombre
        self.compActivo = compActivo
        self.unidades = unidades

    def __str__(self):
        return f"El medicamento {self.nombre} componente activo {self.compActivo} ingreso {self.unidades}."



#################################################
def registrarEmpleado():
    print("empleado")
    datos = []  # matriz en 0

    # el usuario registra los datos
    while True:
        nombre = input("Ingrese el nombre (o '0' para terminar): ")
        if nombre == '0':
            break  # si el usuario ingresa '0', se sale del registrar
        edad = int(input("Ingrese la edad: "))
        datos.append((nombre, edad))  # agregar los datos ingresados a la lista

    # mostrar la lista de datos ingresados
    print("Lista de datos ingresados:")
    for nombre, edad in datos:
        print(f"{nombre}: {edad}")

def listaEmpleados():
    print(" lista empleado ")


def registrarMedicamento():
    print(" Registro de medicamentos ")



def listaMedicamentos():
    print("lista de medicamento")


def horasTrabajo():

  print("horas de trabajo")
  filas = int(input("introduce numero de empleados"))
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


  # Imprimir la matriz original

  print("Matriz original:")
  for i in range(filas):
      for j in range(columnas):
          print(horas_trabajadas[i][j], end=" ")
      print()

  # Pedir al usuario que elija si desea modificar o eliminar un valor de la matriz
  accion = input("¿Desea modificar o eliminar un valor? (m/e): ")

  # Si elige modificar un valor, pedir al usuario que indique la posición y el nuevo valor
  if accion == "m":
      filas = int(input("Ingrese la fila donde se encuentra el valor que desea modificar: "))
      columnas = int(input("Ingrese la columna donde se encuentra el valor que desea modificar: "))
      nuevo_valor = int(input("Ingrese el nuevo valor para la posición [{},{}]: ".format(i+1, j+1)))
      horas_trabajadas[filas][columnas] = nuevo_valor

  # Si elige eliminar un valor, pedir al usuario que indique la posición
  elif accion == "e":
      filas = int(input("Ingrese la fila donde se encuentra el valor que desea eliminar: "))
      columnas = int(input("Ingrese la columna donde se encuentra el valor que desea eliminar: "))
      del horas_trabajadas[i][j]

  # Imprimir la matriz modificada
  print("Matriz modificada:")
  for i in range(len(horas_trabajadas)):
      for j in range(len(horas_trabajadas[0])):
          print(horas_trabajadas[i][j], end=" ")
      print()
