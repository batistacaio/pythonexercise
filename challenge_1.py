nome = "Caio"
idade = 25
altura = 1.78
peso = 84
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f"Meu nome é {nome}, tenho {idade} anos, nasci no ano de {ano_nascimento} e meu IMC é {imc:.2f}")

if idade < 16:
    print(f"{nome} não pode votar")
elif idade >= 16 and idade < 18:
    print(f"{nome} pode votar se quiser")
else:
    print(f"{nome} deverá votar obrigatoriamente")