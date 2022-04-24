# - Dict comprehension

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