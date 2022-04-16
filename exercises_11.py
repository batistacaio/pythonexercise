# -- Desempacotamento

def func(*args):
    print(args)

lista = [1, 2, 3, 4, 5, 6]
print(*lista, sep="-")

func(1, 2, 3, 4, 5)