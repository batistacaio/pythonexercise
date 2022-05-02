file = open("text.txt", "w+")
file.write("Este é um arquivo de teste do Python")

file.seek(0, 0)
print("Lendo linha: ")
print(file.read())

file.close()