# -- Desempacotamento

def func(*args, **kwargs):
    print(args)
    print(kwargs)

lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 0]

func(*lista, *lista2, nome="Caio", sobrenome="Batista")