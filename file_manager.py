file = open("text.txt", "w+")
file.write("Este é um arquivo de teste do Python\n")
file.write("Esta é uma outra linha")

file.seek(0, 0)
print("Lendo linha: ")
print(file.read())
print("#############")

file.seek(0, 0)
for linha in file:
    print(linha, end="")

file.close()