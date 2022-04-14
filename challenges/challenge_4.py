lista = list(range(10, 1, -1))

for indice, valor in enumerate(lista):
    print(indice, valor)
    
# ---- or

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)