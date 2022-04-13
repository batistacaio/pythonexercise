string = "I love Python"

new_string = string[7:13]
print(new_string)

for letra in string:
    print(letra)
    
x = 0

# -----------

while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1
print("Acabou!")

# ------- Calculadora

while True:
    print("Calculadora Python")
    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")
    
    if not num_1.isnumeric() or num_2.isnumeric():
        print("Você precisa digitar um número.")
        
    num_1 = int(num_1)
    num_2 = int(num_2)
    
    # -- + - / *
    
    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == "/":
        print(num_1 / num_2)
    elif operador == "*":
        print(num_1 * num_2)