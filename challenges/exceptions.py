# https://docs.python.org/3/library/exceptions.html

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print("Erro:")
        return error

print(divide(2, 0))