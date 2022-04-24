# - Dict comprehension

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

newdict = {x: y for x, y in lista} # - or dict(lista)
print(newdict)