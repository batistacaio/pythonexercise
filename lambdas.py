a = lambda x, y: x * y
print(a(4, 3))

# --------------

lista_produtos = [
    ["Produto 1", 25],
    ["Produto 2", 4],
    ["Produto 3", 21],
    ["Produto 4", 9],
    ["Produto 5", 101]
]

print(sorted(lista_produtos, key=lambda i: i[1]))