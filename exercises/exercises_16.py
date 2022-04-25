from itertools import groupby

# - Groupby

alunos = [
    {"nome": "Caio", "nota": "A"},
    {"nome": "João", "nota": "B"},
    {"nome": "Bia", "nota": "A"},
    {"nome": "Lucas", "nota": "D"},
    {"nome": "Marcelo", "nota": "B"},
    {"nome": "Renato", "nota": "C"},
    {"nome": "Solange", "nota": "C"},
    {"nome": "Jéssica", "nota": "A"},
    {"nome": "Joaquim", "nota": "D"},
]
ordena = lambda item: item["nota"]
alunos.sort(key=ordena)
agrupado = groupby(alunos, ordena)

for agrupador, valores_agrupados in agrupado:
    print(f"Nota: {agrupador}")
    for aluno in valores_agrupados:
        print(aluno)
    print()