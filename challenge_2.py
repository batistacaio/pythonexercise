"""
usuario = input("Nome de usuário: ")
senha = input("Senha do usuário: ")

if not usuario:
    print("Usuário deverá ter ao menos 1 caractere.")
elif len(senha) < 8:
    print("Senha deverá ter ao menos 8 dígitos.")
else:
    print("Usuário cadastrado.")
"""

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Digite apenas números inteiros positivos.")