class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2


def operacion_calculadora(num1, num2, operacion):
    calc = Calculadora(num1, num2)
    if operacion == 'suma':
        resultado = calc.suma()
    elif operacion == 'resta':
        resultado = calc.resta()
    else:
        resultado = None
        print('Operación no válida')
    return resultado
