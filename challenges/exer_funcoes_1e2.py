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
    return valor + (valor * percentual / 100)

print(somapercentual(200, 20))

# -- 4

def fizzbuzz(val):
    if val % 5 == 0 and val % 3 == 0:
        return "BuzzFizz"
    elif val % 3 == 0:
        return "Fizz"
    elif val % 5 == 0:
        return "Buzz"
    else:
        return val

print(fizzbuzz(15))