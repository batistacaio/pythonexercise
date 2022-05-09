import validacnpj

while True:
    cnpj_input = input("Digite um CNPJ, [g] para gerar um ou [s] para sair: ")
    if cnpj_input == "s":
        break
    elif cnpj_input == "g":
        validacnpj.generator()
    elif validacnpj.validate(cnpj_input):
        print(f"{cnpj_input} é válido.")
    else:
        print(f"{cnpj_input} é inválido.")