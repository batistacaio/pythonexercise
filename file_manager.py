import json

# w - write mode; r - read mode, a - append mode

file = open("text.txt", "w+")
file.write("Este é um arquivo de teste do Python\n")
file.write("Esta é uma outra linha\n")

file.seek(0, 0)
print("Lendo linha: ")
print(file.read())
print("#############")

file.seek(0, 0)
for linha in file:
    print(linha, end="")
print("#############")

file.close()

dict = {
    "Pessoa 1": {
        "nome": "Caio",
        "idade": 25
    },
    "Pessoa 2": {
        "nome": "Lucas",
        "idade": 33
    }
}

dict_json = json.dumps(dict)

with open("dict.json", "w+") as file:
    file.write(dict_json)