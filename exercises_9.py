contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    
    acumulador = acumulador + contador
    contador += 1
else:
    print(f"Contamos até {contador} e acumulamos {acumulador}\n\n")
    
frase = "O rato roeu a roupa do rei de roma"
tamanho_frase = len(frase)
counter = 0
nova_string = ""

while counter < tamanho_frase:
    letra = frase[counter]
    if letra == "r":
        nova_string += "R"
    else:
        nova_string += letra
    counter += 1
    
print(nova_string)