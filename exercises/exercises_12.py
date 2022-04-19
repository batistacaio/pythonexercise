d1 = {"Chave1": "Valor_chave1"}
d1["Chave2"] = "Valor_chave2"

# - Alterar valor forma 1

d1.update({"Chave1": "Valor_alterado"})

# - Alterar valor forma 2

d1["Chave2"] = "Valor2_alterado"

# - Deletar chave

# del d1["Chave2"]

# - Resgatar valores

print("Valor_alterado" in d1.values()) # Retorna true

