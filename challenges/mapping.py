from dados import pessoas, produtos, lista

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