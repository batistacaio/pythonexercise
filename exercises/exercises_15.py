import time
from itertools import zip_longest, count

# - Dict comprehension
'''
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

newdict = {x: y for x, y in lista} # - or dict(lista)
print(newdict)

upperdict = {x.upper(): y.upper() for x, y in lista}
print(upperdict)

d1 = {f"chave_{x}": x**2 for x in range(5)}
print(d1)

# - Iteraveis, iteradores e geradores

# Gerador

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)

# or

gerador = (x for x in range(1000))
print(gerador)

# - Zip

indice = count()
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Uberlandia"]
estados = ["SP", "RJ", "BH"]

cidades_estados = zip(indice, estados, cidades)

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)
'''

# - Count

contador = count(start=10)

for v in contador:
    print(v)
    if v == 20:
        break