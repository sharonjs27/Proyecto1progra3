def funcion1():
    datos = []
    for i in range(1, 11):
        datos.append(i)
    return datos

def funcion2(lista):
    for dato in lista:
        print(dato)

# llamada a las funciones
lista_datos = funcion1()
funcion2(lista_datos)

