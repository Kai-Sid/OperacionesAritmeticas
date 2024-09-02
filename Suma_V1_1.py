def ingresoNumeros():
    numero1 = float(input("Ingrese sumando 1: "))
    numero2 = float(input("Ingrese sumando 2: "))
    return numero1, numero2


def suma(numero1, numero2):
    return numero1 + numero2


num1,num2 = ingresoNumeros()

print(f"{num1} + {num2} = {suma(num1, num2)}")
