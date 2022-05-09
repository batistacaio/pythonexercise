import re

REGRESSIVES = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def validate(cnpj):
    cnpj = remove_dots(cnpj)
    try:
        if sequence(cnpj):
            print("Sequências não são permitidas.")
            return False
    except:
        return False
    try:
        n_cnpj = calc_digit(cnpj=cnpj, digit=1)
        n_cnpj = calc_digit(cnpj=n_cnpj, digit=2)
    except Exception as e:
        return False

def remove_dots(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def sequence(cnpj):
    seq = cnpj[0] * len(cnpj)
    if seq == cnpj:
        return True
    else:
        return False
    
def calc_digit(cnpj, digit):
    if digit == 1:
        regressives = REGRESSIVES[1:]
        n_cnpj = cnpj[:-2]
    elif digit == 2:
        regressives = REGRESSIVES
        n_cnpj = cnpj
    else:
        return None
    
    total = 0
    for index, reg in enumerate(regressives):
        total += int(cnpj[index]) * reg
    
    digit1 = 11 - (total % 11)
    digit1 = digit1 if digit1 <= 9 else 0
    
    return f'{n_cnpj}{digit1}'    