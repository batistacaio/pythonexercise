class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def comer(self, alimento):
        print(f"{self.nome} está comendo {alimento}")
        self.comendo = True
        
    def falar(self, frase):
        print(f"{self.nome} está falando: '{frase}'")
        self.falando = True