# - Sets --> não ordenado e não aceita elementos duplicados

s1 = {1, 2, 3, "Caio", "Batista"}

s1.discard("Batista")
s1.update("Tiao") # - Itera sobre cada elemento

print(s1)

# --- Exemplos

s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8, 9}

set_unido = s2 | s3 # Remove os duplicados
set_intersec = s2 & s3 # Mostra os presentes em ambos sets
set_diff = s2 - s3 # Mostra os que são diferentes dependendo da ordem do set
set_symdiff = s2 ^ s3 # Remove os presentes em ambos

print(set_unido)
print(set_intersec)
print(set_diff)
print(set_symdiff)