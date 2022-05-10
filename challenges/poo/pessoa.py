class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def comer(self, alimento):
        self.alimento = alimento
        print(f"{self.nome} está comendo {self.alimento}")
        self.comendo = True
        
    def falar(self, frase):
        self.frase = frase
        print(f"{self.nome} está falando: '{self.frase}'")
        self.falando = True