# https://docs.python.org/3/library/exceptions.html
'''
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print("Erro:")
        return error

print(divide(2, 0))
'''
# Utilizando raise

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("N2 não pode ser 0")
    return n1 / n2

try:
    print(divide(2, 0))
except ValueError as error:
    print(error)
    
# - Utilizando condicionais

def converte(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converte(input("Digite um número: "))
    if numero is not None:
        print(numero * 2)
    else:
        print("Digite um número válido")