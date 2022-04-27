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