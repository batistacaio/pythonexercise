from pessoa import Pessoa

p1 = Pessoa("Caio", 25)

print(p1.nome)
p1.comer("abacaxi")
p1.comer("pastel")
p1.parar_comer()
p1.falar("Hoje ainda é terça-feira")
p1.falar("Hoje não é quinta")
p1.parar_falar()
p1.get_ano_nascimento()