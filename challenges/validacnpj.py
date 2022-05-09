import re

def validate(cnpj):
    cnpj = remove_dots(cnpj)
    print(cnpj)

def remove_dots(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

cnpj = validate("33.751.438/0001-00")