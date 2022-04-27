from dados import pessoas, produtos, lista
from functools import reduce

'''
nova_lista = list(map(lambda x: x * 2, lista))
print(nova_lista)

precos_produtos = map(lambda p: p["preco"], produtos)

for preco in precos_produtos:
    print(preco)
    
# - Alterando valores sem modificar tabela original
    
def aumenta_preco(p):
    p["preco"] = round(p["preco"] * 1.05, 2)
    return p

novos_precos = map(aumenta_preco, produtos)

for produto in novos_precos:
    print(produto)
    
# - Solicitar apenas nomes das pessoas

nomes = map(lambda n: n["nome"], pessoas)

for nome in nomes:
    print(nome)
'''  
# - Filter

busca_nome = filter(lambda n: n["nome"] == "Caio", pessoas)
print(list(busca_nome))

filtra_valor = filter(lambda v: v > 5, lista)
print(list(filtra_valor))

# - Reduce

soma_precos = reduce(lambda acumulador, item: item["preco"] + acumulador, produtos, 0)
print(round(soma_precos, 2))