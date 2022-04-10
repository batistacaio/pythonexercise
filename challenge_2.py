usuario = input("Nome de usuário: ")
senha = input("Senha do usuário: ")

if not usuario:
    print("Usuário deverá ter ao menos 1 caractere.")
elif len(senha) < 8:
    print("Senha deverá ter ao menos 8 dígitos.")
else:
    print("Usuário cadastrado.")