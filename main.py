import funciones


print(' *** BIENVENIDOS A BASE DE DATOS ***')
print('1: sumas')
print('2: resta')
print('3: divicion')
print('6: multiplicación')
print('5: tablas de multiplicar')
print('0: Salir')

opcion = input('opcion')
print(opcion + 'hla')
N1 = float (input("numero 1"))
N2 = float (input("numero 2"))

while opcion == 1:
    print("la suma es" + funciones.S(N1+N2))
while opcion == 2:
    print("la resta es",+ funciones.R(N1,N2))
while  opcion == 3:
    print("la multiplicacion es", + funciones.M(N1,N2))
while opcion == 4:
    print("la divicion es", + funciones.D(N1,N2))




