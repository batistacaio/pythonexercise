from pessoa import Pessoa
from carro import Carro

c1 = Carro("BMW", "Z4", 2019)
p1 = Pessoa("Caio", 25)
p2 = Pessoa.por_ano_nascimento("Jessica", 1999)

print(p1.nome)
p1.comer("abacaxi")
p1.comer("pastel")
p1.parar_comer()
p1.falar("Hoje ainda é terça-feira")
p1.falar("Hoje não é quinta")
p1.parar_falar()
p1.get_ano_nascimento()
print(p2.idade)
print(c1.modelo)