# Desafio 1

num1 = input("Digite um número: ")

if num1.isdigit():
    num1 = int(num1)
    if num1 % 2:
        print("O número é impar")
    else:
        print("O número é par")
else:
    print("Digite apenas números inteiros positivos.")

# Desafio 2

hora_atual = input("Digite a hora atual (0-23): ")

if hora_atual.isdigit():
    hora_atual = int(hora_atual)
    if hora_atual < 12:
        print("Bom dia!")
    elif 12 <= hora_atual < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")
else:
    print("Digito inválido.")

# Desafio 3

nome = input("Digite seu nome: ")

tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("Seu nome é curto.")
elif 4 < tamanho_nome < 7:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")