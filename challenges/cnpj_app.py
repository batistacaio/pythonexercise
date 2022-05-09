import validacnpj

while True:
    cnpj_input = input("Digite um CNPJ, [g] para gerar um ou [s] para sair: ")
    if validacnpj.validate(cnpj_input):
        print(f"{cnpj_input} é válido.")
    elif cnpj_input == "g":
        validacnpj.generator()
    else:
        print(f"{cnpj_input} é inválido.")