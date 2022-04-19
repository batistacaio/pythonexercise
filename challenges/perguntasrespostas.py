perguntas = {
    "Pergunta 1": {
        "pergunta": "Quanto é 2 + 2?",
        "respostas": {
          "a": "3",
          "b": "4",
          "c": "6",
          "d": "1"
        },
        "resposta_certa": "b"
    },
    "Pergunta 2": {
        "pergunta": "Quanto é 3 * 2?",
        "respostas": {
          "a": "2",
          "b": "10",
          "c": "6",
          "d": "0"
        },
        "resposta_certa": "c"
    },
    "Pergunta 3": {
        "pergunta": "Quanto é 10 / 5?",
        "respostas": {
          "a": "2",
          "b": "4",
          "c": "15",
          "d": "3"
        },
        "resposta_certa": "a"
    },
}

for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")
    for rk, rv in pv["respostas"].items():
        print(f"{rk}: {rv}")
    resposta = input("Digite a resposta: ")
    if resposta == pv["resposta_certa"]:
        print("Você acertou!")
    else:
        print("Você errou.")