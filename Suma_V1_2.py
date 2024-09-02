class OperacionesAritmeticas:
    pass


class OperacionesAritmeticas():
    def ingresoNumeros(self):
        numero1 = float(input("Ingrese sumando 1: "))
        numero2 = float(input("Ingrese sumando 2: "))
        return numero1, numero2

    def suma(self, numero1, numero2):
        return numero1 + numero2

    operacion = OperacionesAritmeticas()
    num1, num2 = ingresoNumeros()
    print(f"{num1} + {num2} = {operacion, suma(num1, num2)}")
