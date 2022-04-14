variavel = ["João", "Maria", "Luiz"]

for valor in variavel:
    if valor.lower().startswith("j"):
        print("Existe uma palavra que começa com J")
        break
else:
    print("Não existe uma palavra que começa com J\n\n")
    
# ----------------

string = "A poluição gerada e impregnada nas grandes cidades foi em grande parte fruto da urbanização desenfreada ou da atuação de indústrias; porém, deveres não cumpridos pelos homens também proporcionaram toda essa 'sujidade'. Nesse sentido, vale lembrar que pequenos atos podem produzir grandes mudanças se realizados por todos os cidadãos."
lista1 = string.split(" ")
contagem = 0
palavra = ""

for valor in lista1:
    qtd_vezes = lista1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra que mais apareceu é {palavra} ({contagem}x)")

# ----------------

lista = ["A", "B", "C", "D"]
novalista = ", ".join(lista)

print(novalista)

# Testing branches