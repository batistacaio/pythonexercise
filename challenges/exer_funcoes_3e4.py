# ----- Exercicio 3

def funcao2(nome):
    print(f"Olá, meu nome é {nome}")
    
def funcao1(*func):
    func = funcao2
    
funcao1(funcao2("Caio"))

# ----- Exercicio 4

def funcao3(idade, profissao):
    print(f"Tenho {idade} anos e sou {profissao}")
    
funcao1(funcao2("Caio"), funcao3(25, "desenvolvedor"))