import validacnpj

while True:
    cnpj_input = input("Digite um CNPJ ou [s] para sair: ")
    if validacnpj.validate(cnpj_input):
        print(f"{cnpj_input} é válido.")
    else:
        print(f"{cnpj_input} é inválido.")