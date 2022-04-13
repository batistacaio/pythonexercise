secreto = "paralelepipedo"
digitados = []
tentativas = 0

print(f"Jogo de adivinhação! Adivinhe a palavra secreta. Ela tem {len(secreto)} letras")

while True:
    letra = input("Digite uma letra ou a palavra secreta: ")
    tentativas += 1
    if letra == "bicicleta":
        print("Você acertou a palavra secreta! '{secreto}'")
        break
    elif len(letra) > 1:
        print("Não vale, digite apenas uma letra")
        continue
    else:
        if letra in secreto:
            print(f"Essa letra existe na palavra secreta!")
            digitados.append(letra)
        else:
            print("Essa letra não existe na palavra secreta")
            
    if tentativas == 10:
        print("Você atingiu o número máximo de tentativas")
        break
            
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temp += letra_secreta
        else:
            secreto_temp += "*"
    if not "*" in secreto_temp:
        print(f"Você descobriu a palavra secreta! '{secreto}'")
        break
            
    print(secreto_temp)
    print(f"Número de tentativas: {tentativas}")