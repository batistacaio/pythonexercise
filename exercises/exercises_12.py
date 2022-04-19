d1 = {"Chave1": "Valor_chave1"}
d1["Chave2"] = "Valor_chave2"

# - Alterar valor forma 1

d1.update({"Chave1": "Valor_alterado"})

# - Alterar valor forma 2

d1["Chave2"] = "Valor2_alterado"

# - Deletar chave

# del d1["Chave2"]

# - Resgatar valores

print("Valor_alterado" in d1.values()) # Retorna true /// .keys() para as chaves

d1["Chave3"] = "Valor_chave3"

for v in d1.values():
    print(v)
    
# - Acessar chave e valor

for c, v in d1.items():
    print(c, v)