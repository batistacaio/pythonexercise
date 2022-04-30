# https://docs.python.org/3/py-modindex.html

import sys
from random import randint as gera
from vendas import calc_precos

print(sys.platform)

for v in range(10):
    print(gera(0, 10))

preco = 59.99
preco_aumentado = calc_precos.aumento(preco, 15)

print(preco_aumentado)