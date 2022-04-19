print("\n** Quiz Harry Potter! Acerte ao menos 7 das 10 perguntas para ser aceito em Hogwarts! **\n")

perguntas = {
    "Pergunta 1": {
        "pergunta": "Qual a casa do Harry?",
        "respostas": {
          "a": "Grifinória",
          "b": "Sonserina",
          "c": "Lufa-Lufa",
          "d": "Sonserina"
        },
        "resposta_certa": "a"
    },
    "Pergunta 2": {
        "pergunta": "Qual o feitiço para abrir fechaduras?",
        "respostas": {
          "a": "Malfeito Feito",
          "b": "Expectrum Patronum",
          "c": "Alohomora",
          "d": "Wingardium Leviosa"
        },
        "resposta_certa": "c"
    },
    "Pergunta 3": {
        "pergunta": "Qual o nome do rato do Rony",
        "respostas": {
          "a": "Fofo",
          "b": "Peludo",
          "c": "Hagrid",
          "d": "Perebas"
        },
        "resposta_certa": "d"
    },
    "Pergunta 4": {
        "pergunta": "Onde Hogwarts está localizada?",
        "respostas": {
          "a": "Londres",
          "b": "Moscou",
          "c": "California",
          "d": "Nova York"
        },
        "resposta_certa": "a"
    },
    "Pergunta 5": {
        "pergunta": "Quantos filmes a saga possui?",
        "respostas": {
          "a": "10",
          "b": "7",
          "c": "8",
          "d": "6"
        },
        "resposta_certa": "c"
    },
    "Pergunta 6": {
        "pergunta": "Quantas etapas tinham o torneio tribruxo?",
        "respostas": {
          "a": "2",
          "b": "3",
          "c": "1",
          "d": "5"
        },
        "resposta_certa": "b"
    },
    "Pergunta 7": {
        "pergunta": "Qual o componente mágico da varinha do Harry?",
        "respostas": {
          "a": "Escama de dragão",
          "b": "Pelo de unicórnio",
          "c": "Pena de fênix",
          "d": "Lasca de sabugueiro"
        },
        "resposta_certa": "c"
    },
    "Pergunta 8": {
        "pergunta": "Qual a primeira criatura que os protagonistas enfrentam?",
        "respostas": {
          "a": "Troll",
          "b": "Centauro",
          "c": "Cérbero",
          "d": "Voldemort"
        },
        "resposta_certa": "a"
    },
    "Pergunta 9": {
        "pergunta": "Qual o nome da poção que transforma em outra pessoa?",
        "respostas": {
          "a": "Amortentia",
          "b": "Volubilis",
          "c": "Multissuco",
          "d": "Polissuco"
        },
        "resposta_certa": "d"
    },
    "Pergunta 10": {
        "pergunta": "Qual o patrono do Harry?",
        "respostas": {
          "a": "Lobo",
          "b": "Alce",
          "c": "Corsa",
          "d": "Cachorro"
        },
        "resposta_certa": "c"
    },
}

contador_certas = 0

for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")
    for rk, rv in pv["respostas"].items():
        print(f"{rk}: {rv}")
    resposta = input("Digite a resposta: ")
    if resposta == pv["resposta_certa"]:
        contador_certas += 1
        print("\nVocê acertou!\n")
    else:
        print("Você errou.")

if contador_certas >= 7:
    print("Parabéns! Você foi aceito em Hogwarts!")
else:
    print("Desculpe, tente no próximo ano.")