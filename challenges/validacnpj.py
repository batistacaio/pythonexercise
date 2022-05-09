import re
import random

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

def generator():
    first_cluster = random.randint(10, 99)
    second_cluster = random.randint(100, 999)
    third_cluster = random.randint(100, 999)
    after_slash = '0001'
    b_cnpj = f"{first_cluster}{second_cluster}{third_cluster}{after_slash}00"
    
    n_cnpj = calc_digit(cnpj=b_cnpj, digit=1)
    n_cnpj = calc_digit(cnpj=n_cnpj, digit=2)
    f_cnpj = f"{n_cnpj[:2]}.{n_cnpj[2:5]}.{n_cnpj[5:8]}/{n_cnpj[8:12]}-{n_cnpj[12:14]}"

    print(f_cnpj)