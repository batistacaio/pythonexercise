# -- 1

def greeting(saudacao, nome):
    return f"{saudacao}, {nome}"

print(greeting("Olá", "Caio"))

# -- 2

def numsum(n1, n2, n3):
    return n1 + n2 + n3

print(numsum(4, 3, 5))

# -- 3

def somapercentual(valor, percentual):
    valorpercentual = percentual / 100
    valoradicional = valor * valorpercentual
    somavalores = valor + valoradicional
    return somavalores

print(somapercentual(200, 20))

# -- 4

def fizzbuzz(val):
    if not val % 5 and val % 3:
        return "BuzzFizz"
    elif not val % 3:
        return "Fizz"
    elif not val % 5:
        return "Buzz"
    else:
        return val

print(fizzbuzz(15))