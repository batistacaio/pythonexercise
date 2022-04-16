# -- Desempacotamento, args e kwargs

def func(*args, **kwargs):
    print(args)
    print(kwargs)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)

lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 0]

func(*lista, *lista2, nome="Caio", sobrenome="Batista", idade=25)